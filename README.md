# 🎭 Project 1: Login Test Suite

Automated login tests using Python + Playwright + pytest.

## Tech Stack
- Python
- Playwright
- pytest

## Test Scenarios
| Test | Scenario | Expected Result |
|------|----------|-----------------|
| test_successful_login | Valid credentials | Redirected to success page |
| test_wrong_password | Invalid password | Error message shown |
| test_wrong_username | Invalid username | Error message shown |

## How To Run
```bash
pip install -r requirements.txt
playwright install
pytest tests/ -v --headed
```
```

---

## 🗺️ Where We Are
```
✅ Project 1: Login Test Suite        ← YOU ARE HERE (DONE!)
⬜ Project 2: Form Automation
⬜ Project 3: Data-Driven Tests
⬜ Project 4: Full Suite + Reports
⬜ Project 5: CI/CD Pipeline