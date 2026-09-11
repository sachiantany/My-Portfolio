#!/usr/bin/env python3
"""Fetch GitHub contribution data and activity for the portfolio site."""

import json
import os
import sys
import urllib.request
from datetime import datetime, timezone

USERNAME = "sachiantany"
API_URL = "https://api.github.com/graphql"

QUERY = """
query {
  user(login: "%s") {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            date
            contributionCount
            contributionLevel
          }
        }
      }
    }
    pullRequests(first: 20, orderBy: {field: CREATED_AT, direction: DESC}) {
      nodes {
        title
        number
        state
        url
        createdAt
        additions
        deletions
        bodyText
        comments { totalCount }
        repository { nameWithOwner isPrivate }
      }
    }
    issues(first: 15, orderBy: {field: CREATED_AT, direction: DESC}) {
      nodes {
        title
        number
        state
        url
        createdAt
        bodyText
        comments { totalCount }
        repository { nameWithOwner isPrivate }
      }
    }
    repositories(first: 10, orderBy: {field: CREATED_AT, direction: DESC}, ownerAffiliations: OWNER) {
      nodes {
        nameWithOwner
        url
        createdAt
        primaryLanguage { name }
        isPrivate
        isFork
      }
    }
  }
}
""" % USERNAME

LEVEL_MAP = {
    "NONE": 0,
    "FIRST_QUARTILE": 1,
    "SECOND_QUARTILE": 2,
    "THIRD_QUARTILE": 3,
    "FOURTH_QUARTILE": 4,
}


def main():
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Set GH_TOKEN or GITHUB_TOKEN env var", file=sys.stderr)
        sys.exit(1)

    req = urllib.request.Request(
        API_URL,
        data=json.dumps({"query": QUERY}).encode(),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req) as resp:
        raw = json.loads(resp.read())

    if "errors" in raw:
        print(f"GraphQL errors: {json.dumps(raw['errors'], indent=2)}", file=sys.stderr)
        sys.exit(1)

    user = raw["data"]["user"]
    cal = user["contributionsCollection"]["contributionCalendar"]

    weeks = []
    for w in cal["weeks"]:
        days = []
        for d in w["contributionDays"]:
            days.append({
                "d": d["date"],
                "c": d["contributionCount"],
                "l": LEVEL_MAP.get(d["contributionLevel"], 0),
            })
        weeks.append(days)

    activity = []

    for pr in user["pullRequests"]["nodes"]:
        if pr["repository"]["isPrivate"]:
            continue
        activity.append({
            "type": "pr",
            "repo": pr["repository"]["nameWithOwner"],
            "title": pr["title"],
            "number": pr["number"],
            "state": pr["state"].lower(),
            "url": pr["url"],
            "date": pr["createdAt"],
            "additions": pr["additions"],
            "deletions": pr["deletions"],
            "comments": pr["comments"]["totalCount"],
            "body": (pr["bodyText"] or "")[:180],
        })

    for issue in user["issues"]["nodes"]:
        if issue["repository"]["isPrivate"]:
            continue
        activity.append({
            "type": "issue",
            "repo": issue["repository"]["nameWithOwner"],
            "title": issue["title"],
            "number": issue["number"],
            "state": issue["state"].lower(),
            "url": issue["url"],
            "date": issue["createdAt"],
            "comments": issue["comments"]["totalCount"],
            "body": (issue["bodyText"] or "")[:180],
        })

    for repo in user["repositories"]["nodes"]:
        if repo["isPrivate"]:
            continue
        activity.append({
            "type": "repo",
            "repo": repo["nameWithOwner"],
            "url": repo["url"],
            "date": repo["createdAt"],
            "language": (repo["primaryLanguage"] or {}).get("name"),
            "is_fork": repo["isFork"],
        })

    activity.sort(key=lambda x: x["date"], reverse=True)

    result = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "total": cal["totalContributions"],
        "weeks": weeks,
        "activity": activity[:20],
    }

    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "data",
        "github-stats.json",
    )
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        json.dump(result, f)

    print(f"Wrote {out} -- {result['total']} contributions, {len(result['activity'])} activities")


if __name__ == "__main__":
    main()
