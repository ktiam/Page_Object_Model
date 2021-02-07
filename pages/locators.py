from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER_LINK = (By.CSS_SELECTOR, "#register_form")
    EMAIL_LINK = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1_LINK = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2_LINK = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_LINK = (By.CSS_SELECTOR, "#register_form > button")
        
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
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class BasketPageLocators():
    PRODUCT_IN_BASKET_LINK = (By.CSS_SELECTOR, ".col-sm-4.col-sm-offset-8")
    TEXT_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    
    
   
 