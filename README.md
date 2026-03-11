# 🎭 Playwright QA Framework

A production-ready end-to-end test automation framework built with **Playwright** and **Python**, following Page Object Model (POM) design pattern with full CI/CD integration via GitHub Actions.

## ✨ Features

- ✅ Page Object Model (POM) architecture
- ✅ Data-driven testing with parameterization
- ✅ Cross-browser execution (Chromium, Firefox, WebKit)
- ✅ GitHub Actions CI/CD pipeline with automated test runs
- ✅ HTML test reports with screenshots on failure
- ✅ Environment configuration management
- ✅ Parallel test execution support

## 🗂️ Project Structure

```
playwright-qa-framework/
├── tests/
│   ├── test_login.py
│   └── test_search.py
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   └── search_page.py
├── .github/
│   └── workflows/
│       └── playwright-tests.yml
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- pip

### Installation

```bash
git clone https://github.com/roshinisam/playwright-qa-framework.git
cd playwright-qa-framework
pip install -r requirements.txt
playwright install
```

### Running Tests

```bash
# Run all tests
pytest

# Run with HTML report
pytest --html=reports/report.html --self-contained-html

# Run specific browser
pytest --browser firefox

# Run in parallel
pytest -n 4

# Run specific test file
pytest tests/test_login.py -v
```

## 📊 CI/CD Pipeline

Tests run automatically on every push and pull request via GitHub Actions:
- Runs on: `push` to `main`, all pull requests
- Browsers: Chromium (default)
- Reports: HTML report uploaded as artifact on failure

## 🧠 Design Principles

- **Shift-left**: Tests written alongside feature development
- **Maintainability**: POM pattern isolates UI changes to one place
- **Reliability**: Explicit waits over fixed sleeps
- **Visibility**: Screenshots and traces captured on failure
