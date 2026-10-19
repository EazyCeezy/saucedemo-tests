# SauceDemo Test Suite

Automated UI tests for saucedemo.com, a practice e-commerce site,
built with Python, Playwright, and pytest.

## What it tests
- Valid login lands on the products page
- Invalid login shows an error and blocks access

## How to run
    python3 -m venv venv
    source venv/bin/activate
    pip install pytest pytest-playwright
    playwright install chromium
    pytest -v

## Environment
Built and run on an Ubuntu Server VM (UTM on an M4 Mac mini).

## Next
- Cart and checkout tests
- Page Object pattern
- GitHub Actions to run tests on every push
