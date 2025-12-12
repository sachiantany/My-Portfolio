# Quick Start Guide - VS Code / Cloud Code Users

## 🎯 Overview

Your CV is now maintained as an **editable HTML file** that automatically converts to PDF. This means:
- ✅ Edit CV content like editing a text file
- ✅ No need for Word, Pages, or design software
- ✅ Consistent formatting every time
- ✅ Easy version control with Git

## 📝 How to Update Your CV

### Step 1: Open the HTML Template

Open `cv-template.html` in VS Code or Cloud Code.

### Step 2: Find the Section You Want to Edit

The HTML is organized into clear sections:

```html
<!-- About Me Section -->
<div class="section">
    <h2 class="section-title">About Me</h2>
    <p class="about-text">
        YOUR ABOUT TEXT HERE
    </p>
</div>
```

### Step 3: Edit the Content

**Example: Adding a New Job**

Find the "Professional Experience" section and add:

```html
<div class="experience-item">
    <div class="experience-header">
        <span class="date">2025 – Present</span>
        <span class="position">Lead Flutter Engineer | TechCorp Inc</span>
    </div>
    
    <div class="subsection">
        <div class="subsection-title">Key Achievements</div>
        <ul>
            <li>Led team of 5 developers in building scalable mobile apps</li>
            <li>Reduced app load time by 40% through optimization</li>
            <li>Implemented CI/CD pipeline reducing deployment time</li>
        </ul>
    </div>
</div>
```

**Example: Updating Contact Information**

Find the header section and update:

```html
<div class="contact-info">
    +94 717804901 | <a href="mailto:YOUR-EMAIL@gmail.com">YOUR-EMAIL@gmail.com</a> | Colombo, Sri Lanka<br>
    <a href="https://linkedin.com/in/yourprofile">LinkedIn</a> | <a href="https://yourportfolio.com">Portfolio</a>
</div>
```

### Step 4: Generate the PDF

**Option A: Terminal**
```bash
python generate_cv.py
```

**Option B: VS Code Task**

Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac), type "Tasks: Run Task", then create/run "Generate CV"

**Option C: Use the helper script**
```bash
./update-cv.sh
```

## 🎨 Styling Tips

### Change Colors

Find the `:root` or color values in the `<style>` section:

```css
/* Change primary color from blue to green */
color: #1a5490;  /* Old: Blue */
color: #2d7a2d;  /* New: Green */
```

### Change Fonts

```css
body {
    font-family: 'Arial', sans-serif;  /* Clean and professional */
    /* OR */
    font-family: 'Georgia', serif;  /* Traditional and elegant */
    /* OR */
    font-family: 'Courier New', monospace;  /* Technical/coding style */
}
```

### Adjust Spacing

```css
.section {
    margin-bottom: 25px;  /* Increase for more space */
}
```

## 🖼️ Adding Your Photo

Replace the placeholder image with your actual photo:

### Method 1: Local File
```html
<img src="images/profile.jpg" alt="Profile" class="profile-image">
```

### Method 2: Base64 (Recommended for portability)

1. Convert your image to base64:
   ```bash
   base64 your-photo.jpg > photo-base64.txt
   ```

2. Replace the `<img>` tag:
   ```html
   <img src="data:image/jpeg;base64,YOUR_BASE64_STRING_HERE" alt="Profile" class="profile-image">
   ```

### Method 3: Online URL
```html
<img src="https://your-website.com/profile.jpg" alt="Profile" class="profile-image">
```

## 🚀 Workflow in VS Code

### Setup (One-time)

1. **Install Python Extension** (if not already installed)
   - Search "Python" in Extensions
   - Install by Microsoft

2. **Create VS Code Task** for easy PDF generation

Create `.vscode/tasks.json`:

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Generate CV PDF",
            "type": "shell",
            "command": "python",
            "args": ["generate_cv.py"],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "shared"
            },
            "problemMatcher": []
        }
    ]
}
```

Now you can press `Ctrl+Shift+B` to generate PDF instantly!

### Daily Workflow

1. Open `cv-template.html`
2. Make your edits (add job, update skills, etc.)
3. Press `Ctrl+Shift+B` (or run `python generate_cv.py`)
4. Check `cv/cv.pdf` - it's updated!
5. Commit changes:
   ```bash
   git add cv-template.html cv/cv.pdf
   git commit -m "Updated CV with new project"
   git push
   ```

## 🔍 Preview Before Generating

Open `cv-template.html` directly in your browser:
- Right-click → "Open with Live Server" (if you have the extension)
- Or just double-click the file

This lets you see changes before generating the PDF.

## 📋 Common Edits

### Add a New Skill
```html
<div class="tech-item">
    <span class="tech-label">New Category:</span> Skill1, Skill2, Skill3
</div>
```

### Add a Project
```html
<div class="project-item">
    <span class="project-name">Amazing App</span> – Mobile app that does X, Y, Z (01/2025–03/2025)
</div>
```

### Update Certification
```html
<div class="cert-item">AWS Certified Solutions Architect – Valid till 12/2026</div>
```

### Add a Publication
```html
<div class="publication-item">
    "Your Paper Title Here" – Journal/Conference Name, Year
</div>
```

## 🐛 Troubleshooting

### PDF looks different from HTML?

- Use "Print Preview" in browser (Ctrl+P) to see how it will look
- WeasyPrint uses print styles, similar to printing from browser

### Styles not applying?

- Make sure styles are inside `<style>` tags in the HTML
- Check for typos in CSS class names
- Validate HTML at https://validator.w3.org/

### Image not showing in PDF?

- Use base64 encoding for images
- Or use absolute paths (https:// URLs)

## 💡 Pro Tips

1. **Keep it organized**: Group related content in clear `<div>` sections
2. **Test frequently**: Generate PDF after major changes to catch issues early
3. **Use comments**: Add HTML comments to mark sections
   ```html
   <!-- EXPERIENCE SECTION - Update your jobs here -->
   ```
4. **Version control**: Commit after each significant update
5. **Backup**: Keep a copy of your working template

## 🔗 Integration with Portfolio Website

In your portfolio HTML:

```html
<!-- Download button -->
<a href="cv/cv.pdf" download class="btn-download">
    📄 Download CV
</a>

<!-- View in new tab -->
<a href="cv/cv.pdf" target="_blank" class="btn-view">
    👁️ View CV
</a>

<!-- Inline iframe (optional) -->
<iframe src="cv/cv.pdf" width="100%" height="800px"></iframe>
```

## 🎓 Learn More

- HTML Basics: https://developer.mozilla.org/en-US/docs/Learn/HTML
- CSS Styling: https://developer.mozilla.org/en-US/docs/Learn/CSS
- WeasyPrint: https://weasyprint.org/

---

**Questions?** Feel free to customize this template to match your style!
