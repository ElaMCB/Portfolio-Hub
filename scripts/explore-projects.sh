#!/bin/bash
# Explore Projects Script
# Lists all projects and provides quick navigation

echo "🚀 ElaMCB Portfolio Hub - Project Explorer"
echo "=========================================="
echo ""

# Define project categories
declare -A projects=(
    ["Testing & QA"]="mcp-testing-servers"
    ["AI Development Tools"]="LILIA Neuro AI-Ethica"
    ["Practical AI"]="Ela-s-HouseBots virtual-recruiter-reply-bot_ARIA"
)

echo "📂 Project Categories:"
echo ""

for category in "${!projects[@]}"; do
    echo "  📁 $category"
    for project in ${projects[$category]}; do
        echo "    - $project"
    done
    echo ""
done

echo "🔗 Quick Links:"
echo "  - View all projects: https://github.com/ElaMCB?tab=repositories"
echo "  - Portfolio website: https://elamcb.github.io"
echo "  - Research blog: https://elamcb.github.io/research"
echo ""

read -p "Enter project name to clone (or 'q' to quit): " project_name

if [ "$project_name" != "q" ] && [ -n "$project_name" ]; then
    echo "Cloning https://github.com/ElaMCB/$project_name.git..."
    git clone "https://github.com/ElaMCB/$project_name.git"
    echo "✅ Project cloned successfully!"
fi

