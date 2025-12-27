#!/bin/bash
# Run All Demos Script
# Executes demo scripts for all available projects

echo "🎬 Running All Project Demos"
echo "============================"
echo ""

# Check if projects are cloned
projects=(
    "mcp-testing-servers"
    "LILIA"
    "Neuro"
    "AI-Ethica"
    "Ela-s-HouseBots"
    "virtual-recruiter-reply-bot_ARIA"
)

for project in "${projects[@]}"; do
    if [ -d "../$project" ]; then
        echo "▶️  Running demo for $project..."
        cd "../$project"
        
        # Try to run demo (project-specific)
        if [ -f "demo.sh" ]; then
            bash demo.sh
        elif [ -f "npm" ] && [ -f "package.json" ]; then
            npm run demo 2>/dev/null || echo "  ⚠️  No demo script found"
        elif [ -f "demo.py" ]; then
            python demo.py 2>/dev/null || echo "  ⚠️  No demo script found"
        else
            echo "  ⚠️  No demo script found for $project"
        fi
        
        cd - > /dev/null
        echo ""
    else
        echo "⏭️  Skipping $project (not cloned)"
    fi
done

echo "✅ Demo execution complete!"
echo ""
echo "💡 Tip: Clone individual projects to run their demos:"
echo "   git clone https://github.com/ElaMCB/PROJECT_NAME.git"

