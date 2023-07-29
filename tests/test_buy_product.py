from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_buy_product():
    # Подключение к Chrome
    driver = webdriver.ChromeOptions()
    driver.add_experimental_option('detach', True)
    path_chrome = Service('D:/Necessary/QA/drivers')
    driver = webdriver.Chrome(options=driver, service=path_chrome)
    print('Start Test')

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)  # mp = Main Page
    mp.select_product()

    # enter_cart = WebDriverWait(driver, 10).until(
    #     expected_conditions.element_to_be_clickable((By.XPATH, "//div[@id='shopping_cart_container']")))
    # enter_cart.click()  # Entry Cart
    # print('Click Cart')
