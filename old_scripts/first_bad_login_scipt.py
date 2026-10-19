from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "wrong_password")
    page.click("#login-button")
    error = page.text_content('[data-test="error"]')
    assert "do not match" in error
    assert "inventory" not in page.url
    print("Bad password test passed")
    browser.close()

