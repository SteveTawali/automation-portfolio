# 🎭 Project 5: CI/CD Pipeline

Automated test runs on every GitHub push using GitHub Actions.

## 🎯 What This Project Demonstrates
- CI/CD pipeline with GitHub Actions
- Automated test runs in the cloud
- Test reports uploaded as artifacts
- Professional workflow configuration

## 💡 Key Learnings
- CI/CD runs tests automatically on every push
- No more "works on my machine" excuses
- Test artifacts help debug cloud failures
- Headless mode required for cloud environments

## 📁 Workflow
```
Push code to GitHub
      ↓
GitHub Actions triggers automatically
      ↓
Installs Python + Playwright in cloud
      ↓
Runs all tests headless
      ↓
Uploads HTML report as artifact
```

## ▶️ How To Run Locally
```bash
pip install -r requirements.txt
playwright install
pytest tests/ -v --headed
```

## ☁️ How To Run In CI
```bash
# Happens automatically on every push!
git push
```