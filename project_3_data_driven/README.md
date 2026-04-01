# 🎭 Project 3: Data-Driven Tests

Data-driven login tests using pytest parametrize.

## 🎯 What This Project Tests
- Valid login credentials
- Invalid password
- Invalid username
- Empty credentials

## 💡 Key Learnings
- pytest parametrize runs ONE test with MULTIPLE data sets
- Never hardcode data inside test functions
- Parameters must be variables not strings
- Generic assertions work better for failure scenarios

## 🌐 Test Site
https://practicetestautomation.com/practice-test-login/

## ▶️ How To Run
```bash
pip install -r requirements.txt
playwright install
pytest tests/ -v --headed
```

## 📊 Test Results
| Test | Data | Status |
|------|------|--------|
| test_login | student/Password123 | ✅ PASSED |
| test_login | student/WrongPass | ✅ PASSED |
| test_login | wronguser/Password123 | ✅ PASSED |
| test_login | empty/empty | ✅ PASSED |