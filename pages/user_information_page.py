import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class UserInformationPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    first_name = "//input[@id='first-name']"
    last_name = "//input[@id='last-name']"
    postal_code = "//input[@id='postal-code']"
    continue_button = "//input[@id='continue']"

    # Getters
    def get_first_name(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.postal_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.continue_button)))

    # Actions
    def input_first_name(self, first_name_input):
        self.get_first_name().send_keys(first_name_input)
        print('Input First Name')

    def input_last_name(self, last_name_input):
        self.get_last_name().send_keys(last_name_input)
        print('Input Last Name')

    def input_postal_code(self, postal_code_input):
        self.get_postal_code().send_keys(postal_code_input)
        print('Input Postal Code')

    def click_continue_button(self):
        self.get_continue_button().click()
        print('Click Continue Button')

    # Methods
    def input_user_information(self):
        with allure.step("Input User Information"):
            Logger.add_start_step(method="input_user_information")
            self.get_current_url()
            self.input_first_name('Ivan')
            self.input_last_name('Ivanov')
            self.input_postal_code(117345)
            self.click_continue_button()
            Logger.add_end_step(url=self.driver.current_url, method="input_user_information")
