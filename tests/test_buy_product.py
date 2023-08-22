import time
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.user_information_page import UserInformationPage
from pages.overview_page import OverviewPage
from pages.finish_page import FinishPage
from utilities.conftest import set_up


@pytest.mark.run(order=3)
def test_buy_product_1(set_up):
    # Подключение к Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.page_load_strategy = 'eager'
    path_chrome = Service(executable_path='D:/Necessary/QA/drivers/chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=path_chrome)
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
def git(set_up):
    # Подключение к Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.page_load_strategy = 'eager'
    path_chrome = Service(executable_path='D:/Necessary/QA/drivers/chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=path_chrome)
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
def test_buy_product_3(set_up):
    # Подключение к Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.page_load_strategy = 'eager'
    path_chrome = Service(executable_path='D:/Necessary/QA/drivers/chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=path_chrome)
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


@pytest.mark.run(order=4)
@allure.description("Test Full Purchase")
def test_full_purchase(set_up):
    # Подключение к Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.page_load_strategy = 'eager'
    path_chrome = Service(executable_path='D:/Necessary/QA/drivers/chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=path_chrome)
    print('Start Test Full Purchase')

    lp = LoginPage(driver)
    lp.authorization()

    mp = MainPage(driver)
    mp.select_product_2()

    cp = CartPage(driver)
    cp.product_confirm()

    uip = UserInformationPage(driver)
    uip.input_user_information()

    ov = OverviewPage(driver)
    ov.payment()

    fp = FinishPage(driver)
    fp.finish()

    print('Finish Test Full Purchase')
    time.sleep(1)
    driver.quit()
