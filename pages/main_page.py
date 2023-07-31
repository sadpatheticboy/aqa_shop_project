from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    add_to_cart_button = "//button[@id='add-to-cart-sauce-labs-backpack']"
    cart_button = "//div[@id='shopping_cart_container']"
    menu_button = "//button[@id='react-burger-menu-btn']"
    link_about = "//a[@id='about_sidebar_link']"

    # Getters
    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_menu_button(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.menu_button)))

    def get_link_about(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.link_about)))

    # Actions
    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print('Click Add To Cart Button')

    def click_cart_button(self):
        self.get_cart_button().click()
        print('Click Cart Button')

    def click_menu_button(self):
        self.get_menu_button().click()
        print('Click Menu Button')

    def click_link_about(self):
        self.get_link_about().click()
        print('Click Link About')

    # Methods
    def select_product(self):
        self.get_current_url()
        self.click_add_to_cart_button()
        self.click_cart_button()

    def go_to_menu_about(self):
        self.get_current_url()
        self.click_menu_button()
        self.click_link_about()
        self.assert_url_check('https://saucelabs.com/')
