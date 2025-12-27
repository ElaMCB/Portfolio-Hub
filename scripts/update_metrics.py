#!/usr/bin/env python3
"""
Update project metrics in README.md and PROJECTS.md
Fetches repository data from GitHub API and updates documentation.
"""

import requests
import json
import re
from datetime import datetime
from pathlib import Path

# GitHub API configuration
GITHUB_USERNAME = "ElaMCB"
GITHUB_API_BASE = "https://api.github.com"

def fetch_repo_data(username=GITHUB_USERNAME):
    """Fetch repository data from GitHub API"""
    url = f"{GITHUB_API_BASE}/users/{username}/repos"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "ElaMCB-Portfolio-Hub"
    }
    
    try:
        response = requests.get(url, headers=headers, params={"per_page": 100, "sort": "updated"})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching repository data: {e}")
        return []

def get_repo_metrics(repo):
    """Extract metrics from a repository object"""
    return {
        "name": repo.get("name", ""),
        "stars": repo.get("stargazers_count", 0),
        "updated_at": repo.get("updated_at", ""),
        "language": repo.get("language", "N/A"),
        "description": repo.get("description", ""),
        "url": repo.get("html_url", ""),
        "archived": repo.get("archived", False),
        "fork": repo.get("fork", False)
    }

def format_date(date_string):
    """Format ISO date string to readable format"""
    if not date_string:
        return "N/A"
    try:
        date = datetime.fromisoformat(date_string.replace("Z", "+00:00"))
        return date.strftime("%b %Y")
    except:
        return date_string[:7] if len(date_string) >= 7 else date_string

def get_status(updated_at, archived):
    """Determine project status based on update date and archive status"""
    if archived:
        return "🟡 Archived"
    
    if not updated_at:
        return "🟡 Unknown"
    
    try:
        updated = datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        days_since_update = (datetime.now(updated.tzinfo) - updated).days
        
        if days_since_update < 30:
            return "🟢 Active"
        elif days_since_update < 90:
            return "🟡 Maintained"
        else:
            return "🟡 Maintained"
    except:
        return "🟡 Maintained"

def update_readme_table(repos, readme_path="README.md"):
    """Update the project status table in README.md"""
    if not Path(readme_path).exists():
        print(f"README.md not found at {readme_path}")
        return
    
    # Filter and sort repositories
    relevant_repos = [
        get_repo_metrics(r) for r in repos 
        if not r.get("fork", False) and not r.get("archived", False)
    ]
    relevant_repos.sort(key=lambda x: x["stars"], reverse=True)
    top_repos = relevant_repos[:10]  # Top 10 by stars
    
    # Read current README
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Generate new table rows
    table_rows = []
    for repo in top_repos:
        status = get_status(repo["updated_at"], False)
        updated = format_date(repo["updated_at"])
        language = repo["language"] or "N/A"
        stars = repo["stars"]
        
        table_rows.append(
            f"| {repo['name']} | {status} | {updated} | {language} | {stars} |"
        )
    
    # Replace table content (between ## 📈 Project Status and next section)
    pattern = r"(## 📈 Project Status\n\n\| Project \| Status \| Last Updated \| Language \| Stars \|\n\|[^\|]*\|[^\|]*\|[^\|]*\|[^\|]*\|[^\|]*\|\n)((?:\|[^\|]*\|[^\|]*\|[^\|]*\|[^\|]*\|[^\|]*\|\n)*)"
    
    new_table = "| Project | Status | Last Updated | Language | Stars |\n"
    new_table += "|---------|--------|--------------|----------|-------|\n"
    new_table += "\n".join(table_rows) + "\n"
    
    replacement = r"\1" + new_table
    
    new_content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
    
    # Write updated README
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"Updated {readme_path} with latest project metrics")

def main():
    """Main execution function"""
    print("Fetching repository data from GitHub...")
    repos = fetch_repo_data()
    
    if not repos:
        print("No repositories found or error occurred.")
        return
    
    print(f"Found {len(repos)} repositories")
    
    # Update README
    update_readme_table(repos)
    
    # Save raw data for reference
    output_file = Path("scripts/repo_data.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(repos, f, indent=2)
    
    print(f"Repository data saved to {output_file}")
    print("Metrics update complete!")

if __name__ == "__main__":
    main()

