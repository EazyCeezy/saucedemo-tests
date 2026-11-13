# SauceDemo Test Suite

![Tests](https://github.com/EazyCeezy/saucedemo-tests/actions/workflows/tests.yml/badge.svg)

Automated UI tests for saucedemo.com, a practice e-commerce site,
built with Python, Playwright, and pytest.

## What it tests
- Valid login lands on the products page
- Invalid login shows an error and blocks access
- Adding an item to the cart
- Completing checkout

## Features
- Page Object pattern (selectors live in one place)
- Continuous integration: GitHub Actions runs the suite on every push
- Headless Chromium, so it runs on a server with no screen

## Project structure
    pages/login_page.py      Page Object for the login page
    tests/                   test_login, test_cart, test_checkout
    .github/workflows/       CI workflow
    pytest.ini               lets tests import from pages/
    requirements.txt         dependencies

## How to run
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    playwright install chromium
    pytest -v

## Environment
Developed on an Ubuntu Server VM (UTM on an M4 Mac mini),
with CI running on GitHub's Ubuntu runners.

## Next
- Cart Page Object
- Run the suite inside a Docker container
