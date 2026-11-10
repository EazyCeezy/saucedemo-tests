from pages.login_page import LoginPage


def test_checkout(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")
    page.click("#checkout")
    page.fill("#first-name", "Test")
    page.fill("#last-name", "User")
    page.fill("#postal-code", "90001")
    page.click("#continue")
    page.click("#finish")
    assert "Thank you" in page.text_content(".complete-header")
