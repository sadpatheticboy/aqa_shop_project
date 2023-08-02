import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class LoginPage(Base):
    # Base URL
    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    username = "//input[@id='user-name']"
    password = "//input[@id='password']"
    login_button = "//input[@id='login-button']"
    main_word = "//span[@class='title']"

    # Getters
    def get_username(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.username)))

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions
    def input_username(self, username_input):
        self.get_username().send_keys(username_input)
        print('Input Username')

    def input_password(self, password_input):
        self.get_password().send_keys(password_input)
        print('Input Password')

    def click_login_button(self):
        self.get_login_button().click()
        print('Click Login Button')

    # Methods
    def authorization(self):
        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.input_username('standard_user')
            self.input_password('secret_sauce')
            self.click_login_button()
            self.assert_word_check(self.get_main_word(), 'Products')
            Logger.add_end_step(url=self.driver.current_url, method="authorization")
