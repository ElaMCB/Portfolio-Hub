# 🚀 Quick Start Guide

Get started with the ElaMCB Portfolio Hub in minutes!

## 📋 Prerequisites

- Git
- Python 3.8+ (for automation scripts)
- Node.js (optional, for some projects)

## ⚡ Quick Setup

### 1. Clone the Repository
```bash
git clone https://github.com/ElaMCB/ElaMCB-Portfolio-Hub.git
cd ElaMCB-Portfolio-Hub
```

### 2. Install Dependencies
```bash
# Install Python dependencies for automation
pip install -r requirements.txt
```

### 3. Update Project Metrics (Optional)
```bash
# Run the metrics update script
python scripts/update_metrics.py
```

This will fetch the latest repository data from GitHub and update the project status tables.

### 4. Explore Projects
```bash
# On Linux/Mac
bash scripts/explore-projects.sh

# On Windows (PowerShell)
# Use the GitHub web interface or clone projects individually
```

## 📚 Next Steps

1. **Read the Documentation**
   - [README.md](README.md) - Main overview
   - [PROJECTS.md](PROJECTS.md) - Detailed project descriptions
   - [TECHNOLOGIES.md](TECHNOLOGIES.md) - Technology stack
   - [ARCHITECTURE.md](ARCHITECTURE.md) - System designs

2. **Explore Individual Projects**
   - Visit project repositories linked in [PROJECTS.md](PROJECTS.md)
   - Check out [DEMOS.md](DEMOS.md) for live examples

3. **Contribute**
   - Read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines
   - Open issues or submit pull requests

## 🔧 Automation

### GitHub Actions
The repository includes automated workflows:
- **Weekly Updates**: Project metrics are updated every Sunday
- **Manual Trigger**: You can manually trigger updates via GitHub Actions

### Local Scripts
- `scripts/update_metrics.py` - Update project metrics from GitHub API
- `scripts/explore-projects.sh` - Interactive project explorer
- `scripts/run-all-demos.sh` - Run all project demos

## 🌐 GitHub Pages Setup

To enable GitHub Pages for a visual portfolio:

1. Go to repository Settings
2. Navigate to Pages
3. Select source branch (usually `main`)
4. Select folder (usually `/docs` or root)
5. Save

Your portfolio will be available at:
`https://elamcb.github.io/ElaMCB-Portfolio-Hub/`

## 📞 Need Help?

- Open an [issue](https://github.com/ElaMCB/ElaMCB-Portfolio-Hub/issues)
- Check existing [discussions](https://github.com/ElaMCB/ElaMCB-Portfolio-Hub/discussions)
- Visit the [portfolio website](https://elamcb.github.io)

---

**Happy Exploring! 🎉**

