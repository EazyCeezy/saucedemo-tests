from pages.login_page import LoginPage


def test_add_to_cart(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    page.click("#add-to-cart-sauce-labs-backpack")
    assert page.text_content(".shopping_cart_badge") == "1"
    page.click(".shopping_cart_link")
    assert "cart" in page.url
    assert "Sauce Labs Backpack" in page.text_content(".cart_item")
