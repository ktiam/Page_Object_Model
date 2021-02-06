from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER_LINK = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    PRODUCT_LINK = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    NAME_BOOK_LINK = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    NAME_BOOK_IN_BASKET_LINK = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_BOOK_LINK = (By.CSS_SELECTOR, ".col-sm-6.product_main > p.price_color")
    PRICE_BOOK_IN_BASKET_LINK = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
     
    
 