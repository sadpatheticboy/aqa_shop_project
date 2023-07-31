import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.user_information_page import UserInformationPage
from pages.overview_page import OverviewPage
from pages.finish_page import FinishPage


@pytest.mark.run(order=3)
def test_buy_product_1():
    # Подключение к Chrome
    driver = webdriver.ChromeOptions()
    driver.add_experimental_option('detach', True)
    path_chrome = Service('D:/Necessary/QA/drivers')
    driver = webdriver.Chrome(options=driver, service=path_chrome)
    print('Start Test 1')

    lp = LoginPage(driver)
    lp.authorization()

    mp = MainPage(driver)
    mp.select_product_1()

    cp = CartPage(driver)
    cp.product_confirm()

    print('Finish Test 1')
    time.sleep(1)
    driver.quit()


@pytest.mark.run(order=1)
def test_buy_product_2():
    # Подключение к Chrome
    driver = webdriver.ChromeOptions()
    driver.add_experimental_option('detach', True)
    path_chrome = Service('D:/Necessary/QA/drivers')
    driver = webdriver.Chrome(options=driver, service=path_chrome)
    print('Start Test 2')

    lp = LoginPage(driver)
    lp.authorization()

    mp = MainPage(driver)
    mp.select_product_2()

    cp = CartPage(driver)
    cp.product_confirm()

    print('Finish Test 2')
    time.sleep(1)
    driver.quit()


@pytest.mark.run(order=2)
def test_buy_product_3():
    # Подключение к Chrome
    driver = webdriver.ChromeOptions()
    driver.add_experimental_option('detach', True)
    path_chrome = Service('D:/Necessary/QA/drivers')
    driver = webdriver.Chrome(options=driver, service=path_chrome)
    print('Start Test 3')

    lp = LoginPage(driver)
    lp.authorization()

    mp = MainPage(driver)
    mp.select_product_3()

    cp = CartPage(driver)
    cp.product_confirm()

    print('Finish Test 3')
    time.sleep(1)
    driver.quit()

# def test_buy_product():
#     # Подключение к Chrome
#     driver = webdriver.ChromeOptions()
#     driver.add_experimental_option('detach', True)
#     path_chrome = Service('D:/Necessary/QA/drivers')
#     driver = webdriver.Chrome(options=driver, service=path_chrome)
#     print('Start Test')
#
#     lp = LoginPage(driver)
#     lp.authorization()
#
#     mp = MainPage(driver)
#     mp.select_product()
#
#     cp = CartPage(driver)
#     cp.product_confirm()
#
#     uip = UserInformationPage(driver)
#     uip.input_user_information()
#
#     ov = OverviewPage(driver)
#     ov.payment()
#
#     fp = FinishPage(driver)
#     fp.finish()
