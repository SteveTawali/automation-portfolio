# 🎭 Project 4: Page Object Model + HTML Reports

Professional POM design pattern with auto-generated HTML reports.

## 🎯 What This Project Demonstrates
- Page Object Model design pattern
- Separation of locators and test logic
- Auto-generated HTML test reports
- Professional project structure

## 💡 Key Learnings
- POM makes tests cleaner and maintainable
- One change in page object fixes all tests
- pytest.ini automates report generation
- self stores page and locators for reuse

## 📁 Structure
```
project_4_pom/
├── pages/
│   └── login_page.py    ← locators + actions
├── tests/
│   └── test_login_pom.py  ← test scenarios
├── reports/
│   └── report.html      ← auto-generated!
└── pytest.ini
```

## 🌐 Test Site
https://practicetestautomation.com/practice-test-login/

## ▶️ How To Run
```bash
pip install -r requirements.txt
playwright install
pytest tests/ -v --headed
```

## 📊 Test Results
| Test | Status |
|------|--------|
| test_successful_login | ✅ PASSED |
| test_wrong_password | ✅ PASSED |
| test_wrong_username | ✅ PASSED |