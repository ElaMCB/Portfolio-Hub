# 🤝 Contributing to ElaMCB Projects

Thank you for your interest in contributing! This guide will help you get started.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Project-Specific Guidelines](#project-specific-guidelines)
- [Pull Request Process](#pull-request-process)
- [Issue Reporting](#issue-reporting)

## 📜 Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for all contributors.

## 🚀 How to Contribute

### Reporting Bugs
1. Check if the issue already exists
2. Use the bug report template
3. Provide detailed reproduction steps
4. Include environment information

### Suggesting Features
1. Check existing feature requests
2. Use the feature request template
3. Describe the use case and benefits
4. Consider implementation approach

### Code Contributions
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Write/update tests
5. Submit a pull request

## 🛠️ Development Setup

### Prerequisites
- Git
- Node.js (for TypeScript projects)
- Python 3.8+ (for Python projects)
- VS Code (recommended)

### Initial Setup
```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/PROJECT_NAME.git
cd PROJECT_NAME

# Install dependencies
npm install  # or pip install -r requirements.txt

# Run tests
npm test  # or pytest
```

## 📝 Project-Specific Guidelines

### TypeScript Projects (LILIA, mcp-testing-servers)
- Follow TypeScript best practices
- Use ESLint configuration
- Write unit tests with Jest
- Document complex functions

### Python Projects (AI-Ethica, Neuro, HouseBots)
- Follow PEP 8 style guide
- Use type hints
- Write tests with pytest
- Document with docstrings

### Documentation
- Use clear, concise language
- Include code examples
- Update README when adding features
- Keep architecture diagrams current

## 🔄 Pull Request Process

### Before Submitting
1. ✅ All tests pass
2. ✅ Code follows style guidelines
3. ✅ Documentation updated
4. ✅ No merge conflicts
5. ✅ Commit messages are clear

### PR Checklist
- [ ] Description explains the change
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
- [ ] Follows project conventions

### Review Process
1. Automated checks run (CI/CD)
2. Maintainers review code
3. Address feedback
4. Approval and merge

## 🐛 Issue Reporting

### Bug Report Template
```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. See error

**Expected behavior**
What you expected to happen.

**Environment**
- OS: [e.g., Windows 10]
- Version: [e.g., 1.2.3]
- Node/Python version: [e.g., 18.0.0]

**Additional context**
Any other relevant information.
```

### Feature Request Template
```markdown
**Is your feature request related to a problem?**
A clear description of the problem.

**Describe the solution you'd like**
What you want to happen.

**Describe alternatives you've considered**
Other solutions or features you've thought about.

**Additional context**
Any other relevant information.
```

## 🏷️ Commit Message Guidelines

Follow conventional commits:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes
- `refactor:` Code refactoring
- `test:` Test additions/changes
- `chore:` Maintenance tasks

Example:
```
feat: Add support for Playwright test generation
```

## 📚 Resources

- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Contributor Covenant](https://www.contributor-covenant.org/)

## ❓ Questions?

- Open a discussion in the repository
- Check existing issues and discussions
- Reach out via GitHub profile

## 🙏 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Credited in release notes
- Acknowledged in project documentation

---

Thank you for contributing! Your efforts help make these projects better for everyone. 🎉

