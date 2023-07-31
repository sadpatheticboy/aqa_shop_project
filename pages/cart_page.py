from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class CartPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    checkout_button = "//button[@id='checkout']"

    # Getters
    def get_checkout_button(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.checkout_button)))

    # Actions
    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('Click Checkout Button')

    # Methods
    def product_confirm(self):
        self.get_current_url()
        self.click_checkout_button()
