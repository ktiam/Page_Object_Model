from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET_LINK), "Product is presented, but should not be"
    
    def text_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_BASKET_IS_EMPTY), "Text basket is empty is not presented"
            
  
    

        
    
   
 