#!/usr/bin/env python3
"""
CV HTML to PDF Converter
Converts the cv-template.html to cv.pdf

Requirements:
    pip install weasyprint --break-system-packages

Usage:
    python generate_cv.py
"""

from weasyprint import HTML, CSS
from pathlib import Path
import os

def generate_pdf():
    """Convert HTML CV template to PDF"""

    script_dir = Path(__file__).parent

    html_file = script_dir / "cv-template.html"
    pdf_file = script_dir / "cv" / "MDSM_Antany_CV_v2.pdf"
    root_pdf  = script_dir.parent / "cv" / "MDSM_Antany_CV_v2.pdf"  # served by the portfolio

    pdf_file.parent.mkdir(parents=True, exist_ok=True)
    root_pdf.parent.mkdir(parents=True, exist_ok=True)

    if not html_file.exists():
        print(f"❌ Error: HTML template not found at {html_file}")
        return False

    try:
        print("🔄 Converting HTML to PDF...")

        HTML(filename=str(html_file)).write_pdf(
            str(pdf_file),
            stylesheets=None,
        )

        import shutil
        shutil.copy2(str(pdf_file), str(root_pdf))

        print(f"✅ PDF generated: {pdf_file}")
        print(f"✅ Copied to portfolio: {root_pdf}")
        print(f"📄 File size: {pdf_file.stat().st_size / 1024:.2f} KB")
        return True

    except Exception as e:
        print(f"❌ Error generating PDF: {str(e)}")
        return False

if __name__ == "__main__":
    generate_pdf()
