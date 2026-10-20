def test_add_to_cart(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.click("#add-to-cart-sauce-labs-backpack")
    assert page.text_content(".shopping_cart_badge") == "1"
    page.click(".shopping_cart_link")
    assert "cart" in page.url
    assert "Sauce Labs Backpack" in page.text_content(".cart_item")

