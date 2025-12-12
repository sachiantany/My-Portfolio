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
    
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    
    # Define file paths
    html_file = script_dir / "cv-template.html"
    pdf_file = script_dir / "cv" / "cv.pdf"
    
    # Create cv directory if it doesn't exist
    pdf_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Check if HTML template exists
    if not html_file.exists():
        print(f"❌ Error: HTML template not found at {html_file}")
        return False
    
    try:
        print("🔄 Converting HTML to PDF...")
        
        # Convert HTML to PDF
        HTML(filename=str(html_file)).write_pdf(
            str(pdf_file),
            stylesheets=None,  # CSS is already in the HTML
        )
        
        print(f"✅ PDF generated successfully: {pdf_file}")
        print(f"📄 File size: {pdf_file.stat().st_size / 1024:.2f} KB")
        return True
        
    except Exception as e:
        print(f"❌ Error generating PDF: {str(e)}")
        return False

if __name__ == "__main__":
    generate_pdf()
