# Explore Projects Script (PowerShell)
# Lists all projects and provides quick navigation

Write-Host "🚀 ElaMCB Portfolio Hub - Project Explorer" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

# Define project categories
$projects = @{
    "Testing & QA" = @("mcp-testing-servers")
    "AI Development Tools" = @("LILIA", "Neuro", "AI-Ethica")
    "Practical AI" = @("Ela-s-HouseBots", "virtual-recruiter-reply-bot_ARIA")
}

Write-Host "📂 Project Categories:" -ForegroundColor Yellow
Write-Host ""

foreach ($category in $projects.Keys) {
    Write-Host "  📁 $category" -ForegroundColor Green
    foreach ($project in $projects[$category]) {
        Write-Host "    - $project"
    }
    Write-Host ""
}

Write-Host "🔗 Quick Links:" -ForegroundColor Yellow
Write-Host "  - View all projects: https://github.com/ElaMCB?tab=repositories"
Write-Host "  - Portfolio website: https://elamcb.github.io"
Write-Host "  - Research blog: https://elamcb.github.io/research"
Write-Host ""

$projectName = Read-Host "Enter project name to clone (or 'q' to quit)"

if ($projectName -ne "q" -and $projectName -ne "") {
    Write-Host "Cloning https://github.com/ElaMCB/$projectName.git..." -ForegroundColor Cyan
    git clone "https://github.com/ElaMCB/$projectName.git"
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Project cloned successfully!" -ForegroundColor Green
    } else {
        Write-Host "❌ Failed to clone project. Please check the project name." -ForegroundColor Red
    }
}

