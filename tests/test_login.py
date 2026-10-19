def test_valid_login(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    assert "inventory" in page.url

def test_invalid_login(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "wrong_password")
    page.click("#login-button")
    error = page.text_content('[data-test="error"]')
    assert "do not match" in error
    assert "inventory" not in page.url
