#!/bin/bash

# CV Update Script
# This script helps you update your CV and optionally commit changes

echo "🚀 CV Update Tool"
echo "=================="
echo ""

# Check if cv-template.html exists
if [ ! -f "cv-template.html" ]; then
    echo "❌ Error: cv-template.html not found!"
    echo "   Please run this script from your portfolio root directory."
    exit 1
fi

# Function to generate PDF
generate_pdf() {
    echo "🔄 Generating PDF from HTML template..."
    python generate_cv.py
    
    if [ $? -eq 0 ]; then
        echo "✅ PDF generated successfully!"
        return 0
    else
        echo "❌ Failed to generate PDF"
        return 1
    fi
}

# Function to preview in browser
preview() {
    echo "🌐 Opening CV template in browser..."
    
    if command -v xdg-open &> /dev/null; then
        xdg-open cv-template.html
    elif command -v open &> /dev/null; then
        open cv-template.html
    else
        echo "ℹ️  Please open cv-template.html manually in your browser"
    fi
}

# Function to git commit
git_commit() {
    if [ -d ".git" ]; then
        echo ""
        read -p "📝 Enter commit message (or press Enter for default): " commit_msg
        
        if [ -z "$commit_msg" ]; then
            commit_msg="Update CV - $(date +'%Y-%m-%d')"
        fi
        
        git add cv-template.html cv/cv.pdf ../cv/cv.pdf
        git commit -m "$commit_msg"
        
        echo "✅ Changes committed!"
        echo ""
        read -p "🚀 Push to remote? (y/n): " push_choice
        
        if [ "$push_choice" = "y" ] || [ "$push_choice" = "Y" ]; then
            git push
            echo "✅ Changes pushed to remote!"
        fi
    else
        echo "ℹ️  Not a git repository. Skipping commit."
    fi
}

# Main menu
while true; do
    echo ""
    echo "What would you like to do?"
    echo "1. Generate PDF from HTML"
    echo "2. Preview HTML in browser"
    echo "3. Generate PDF and commit changes"
    echo "4. Exit"
    echo ""
    read -p "Enter your choice (1-4): " choice
    
    case $choice in
        1)
            generate_pdf
            ;;
        2)
            preview
            ;;
        3)
            if generate_pdf; then
                git_commit
            fi
            ;;
        4)
            echo "👋 Goodbye!"
            exit 0
            ;;
        *)
            echo "❌ Invalid choice. Please enter 1-4."
            ;;
    esac
done
