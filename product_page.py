from base_page import BasePage
from locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        return self.is_visible(*ProductPageLocators.BUY_BUTTON).click()
    
    def should_be_equal_prices_of_cart_and_product_added_to_cart(self):
        product_price = self.is_visible(*ProductPageLocators.PRODUCT_PRICE).text
        cart_price = self.is_visible(*ProductPageLocators.CART_PRICE).text
        assert product_price == cart_price,\
            f"Prices between product and cart are not equal. Product price is {product_price} \
            and cart price is {cart_price}"