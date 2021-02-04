from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        product_link = self.browser.find_element(*ProductPageLocators.PRODUCT_LINK)
        product_link.click()
    
    def name_book_in_basket(self):
        book_name = self.browser.find_element(*ProductPageLocators.NAME_BOOK_LINK)
        name_book_in_basket = self.browser.find_element(*ProductPageLocators.NAME_BOOK_IN_BASKET_LINK)
        assert book_name.text == name_book_in_basket.text, "Wrong name product added to basket"
        
    def price_book_in_basket(self):
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK_LINK)
        price_book_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_BOOK_IN_BASKET_LINK)
        assert price_book.text == price_book_in_basket.text, "Wrong price product added to basket"    