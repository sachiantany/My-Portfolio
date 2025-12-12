# CV Management System

This system allows you to maintain your CV in an editable HTML format and automatically generate a PDF version.

## 📁 File Structure

```
your-portfolio/
├── cv/
│   └── cv.pdf              # Generated PDF (don't edit this directly)
├── cv-template.html        # EDIT THIS FILE to update your CV
├── generate_cv.py          # Script to convert HTML → PDF
└── README.md               # This file
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Install WeasyPrint (HTML to PDF converter)
pip install weasyprint --break-system-packages
```

### 2. Edit Your CV

Simply open `cv-template.html` in any text editor (VS Code, Cloud Code, etc.) and update the content:

- **Contact Info**: Update in the header section
- **About Me**: Update the paragraph in the "About Me" section
- **Tech Stack**: Modify the tech items list
- **Experience**: Add/remove/edit experience items
- **Projects**: Update project highlights
- **Education**: Update degree information
- **Certifications**: Update certification details
- **References**: Update reference information

### 3. Generate PDF

After editing the HTML, run:

```bash
python generate_cv.py
```

This will create/update `cv/cv.pdf` with your changes.

## 💡 Tips for Editing

### Adding a New Job Experience

```html
<div class="experience-item">
    <div class="experience-header">
        <span class="date">2025 – Present</span>
        <span class="position">Senior Flutter Developer | New Company</span>
    </div>
    
    <div class="subsection">
        <div class="subsection-title">Key Responsibilities</div>
        <ul>
            <li>Built awesome mobile apps</li>
            <li>Led development team</li>
        </ul>
    </div>
</div>
```

### Adding a New Project

```html
<div class="project-item">
    <span class="project-name">Project Name</span> – Description (MM/YYYY–MM/YYYY)
</div>
```

### Adding a New Certification

```html
<div class="cert-item">Certification Name – Valid till MM/YYYY</div>
```

### Updating Your Profile Image

Replace the SVG placeholder in the `<img src="...">` tag with your actual image:

```html
<img src="path/to/your/photo.jpg" alt="Profile" class="profile-image">
```

Or use a base64 encoded image:

```html
<img src="data:image/jpeg;base64,YOUR_BASE64_STRING" alt="Profile" class="profile-image">
```

## 🎨 Styling

All styles are contained within the `<style>` tag in the HTML file. You can customize:

- **Colors**: Change `#1a5490` (blue) to your brand color
- **Fonts**: Modify the `font-family` in the `body` style
- **Spacing**: Adjust margins and padding values
- **Font sizes**: Modify various `.section-title`, `.name`, etc.

## 🔄 Automated Workflow (Optional)

### Using npm scripts

Create a `package.json` in your project root:

```json
{
  "name": "cv-management",
  "version": "1.0.0",
  "scripts": {
    "build:cv": "python generate_cv.py",
    "watch:cv": "nodemon --watch cv-template.html --exec python generate_cv.py"
  }
}
```

Then:
- Run `npm run build:cv` to generate PDF
- Run `npm run watch:cv` to auto-generate on HTML changes (requires nodemon)

### Using a shell script

Create `update-cv.sh`:

```bash
#!/bin/bash
python generate_cv.py
git add cv/cv.pdf cv-template.html
git commit -m "Update CV"
git push
```

Make it executable: `chmod +x update-cv.sh`

## 📦 Deployment

### For GitHub Pages / Static Hosting

1. Edit `cv-template.html`
2. Run `python generate_cv.py`
3. Commit both files:
   ```bash
   git add cv-template.html cv/cv.pdf
   git commit -m "Update CV"
   git push
   ```

### Link to CV on Your Portfolio

```html
<!-- Direct download -->
<a href="cv/cv.pdf" download>Download CV</a>

<!-- Open in new tab -->
<a href="cv/cv.pdf" target="_blank">View CV</a>
```

## 🐛 Troubleshooting

### PDF not generating?

1. Check WeasyPrint is installed: `pip list | grep weasyprint`
2. Check for errors in the HTML (missing closing tags, etc.)
3. Try running with verbose output: `python -v generate_cv.py`

### Styling looks different in PDF?

- WeasyPrint supports most CSS, but not all JavaScript/dynamic features
- Use print preview in browser to test: Press Ctrl+P (Cmd+P on Mac)
- Stick to standard CSS properties for best compatibility

### Profile image not showing?

- Use absolute paths or base64 encoding
- For local development, relative paths work
- For deployment, use base64 or hosted images

## 📝 Best Practices

1. **Always edit the HTML, never the PDF directly**
2. **Test in browser first** (open HTML file) before generating PDF
3. **Keep a backup** of your cv-template.html
4. **Use version control** (git) to track changes
5. **Generate PDF before deploying** to ensure it's up to date

## 🔧 Advanced: Custom PDF Settings

Edit `generate_cv.py` to customize PDF generation:

```python
HTML(filename=str(html_file)).write_pdf(
    str(pdf_file),
    stylesheets=None,
    presentational_hints=True,  # Use HTML styling
    optimize_size=('fonts', 'images'),  # Reduce file size
)
```

## 📚 Resources

- [WeasyPrint Documentation](https://doc.courtbouillon.org/weasyprint/)
- [HTML/CSS Guide](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [Print CSS Tips](https://www.smashingmagazine.com/2018/05/print-stylesheets-in-2018/)

---

**Need help?** Open an issue or contact: sachi.antany@gmail.com
