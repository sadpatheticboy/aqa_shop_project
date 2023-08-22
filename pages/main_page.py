import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    add_to_cart_button_1 = "#add-to-cart-sauce-labs-backpack"
    add_to_cart_button_2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    add_to_cart_button_3 = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    cart_button = "//div[@id='shopping_cart_container']"
    menu_button = "//button[@id='react-burger-menu-btn']"
    link_about = "//a[@id='about_sidebar_link']"

    # Getters
    def get_add_to_cart_button_1(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.add_to_cart_button_1)))

    def get_add_to_cart_button_2(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.add_to_cart_button_2)))

    def get_add_to_cart_button_3(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.add_to_cart_button_3)))

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
    def click_add_to_cart_button_1(self):
        self.get_add_to_cart_button_1().click()
        print('Click Add To Cart Button 1')

    def click_add_to_cart_button_2(self):
        self.get_add_to_cart_button_2().click()
        print('Click Add To Cart Button 2')

    def click_add_to_cart_button_3(self):
        self.get_add_to_cart_button_3().click()
        print('Click Add To Cart Button 3')

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
    def select_product_1(self):
        with allure.step("Select Product 1"):
            Logger.add_start_step(method="select_product_1")
            self.get_current_url()
            self.click_add_to_cart_button_1()
            self.click_cart_button()
            Logger.add_end_step(url=self.driver.current_url, method="select_product_1")

    def select_product_2(self):
        with allure.step("Select Product 2"):
            Logger.add_start_step(method="select_product_2")
            self.get_current_url()
            self.click_add_to_cart_button_2()
            self.click_cart_button()
            Logger.add_end_step(url=self.driver.current_url, method="select_product_2")

    def select_product_3(self):
        with allure.step("Select Product 3"):
            Logger.add_start_step(method="select_product_3")
            self.get_current_url()
            self.click_add_to_cart_button_3()
            self.click_cart_button()
            Logger.add_end_step(url=self.driver.current_url, method="select_product_3")

    def go_to_menu_about(self):
        with allure.step("Go To Menu About"):
            Logger.add_start_step(method="go_to_menu_about")
            self.get_current_url()
            self.click_menu_button()
            self.click_link_about()
            self.assert_url_check('https://saucelabs.com/')
            Logger.add_end_step(url=self.driver.current_url, method="go_to_menu_about")
