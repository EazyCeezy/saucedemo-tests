from pages.login_page import LoginPage


def test_valid_login(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    assert "inventory" in page.url


def test_invalid_login(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "wrong_password")
    assert "do not match" in login.get_error()
    assert "inventory" not in page.url
