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

    # Getters
    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.cart_button)))

    # Actions
    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print('Click Add To Cart Button')

    def click_cart_button(self):
        self.get_cart_button().click()
        print('Click Cart Button')

    # Methods
    def select_product(self):
        self.get_current_url()
        self.click_add_to_cart_button()
        self.click_cart_button()
