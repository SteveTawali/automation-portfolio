# 🎭 Project 2: Form Automation

Automated form filling tests using Python + Playwright + pytest.

## 🎯 What This Project Tests
- Text inputs
- Radio buttons
- Checkboxes
- Date picker (custom calendar widget)
- Autocomplete field
- File upload
- Form submission

## 💡 Key Learnings
- Handling custom date picker widgets
- Using `:not()` CSS selector to avoid duplicate elements
- Autocomplete fields require type + Enter not just fill()
- Always inspect elements manually before writing locators

## 🌐 Test Site
https://demoqa.com/automation-practice-form

## ▶️ How To Run
```bash
pip install -r requirements.txt
playwright install
pytest tests/ -v --headed
```

## 📊 Test Results
| Test | Status |
|------|--------|
| test_fill_student_registration_form | ✅ PASSED |