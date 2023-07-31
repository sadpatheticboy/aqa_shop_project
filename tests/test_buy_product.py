from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.user_information_page import UserInformationPage
from pages.overview_page import OverviewPage
from pages.finish_page import FinishPage


def test_buy_product():
    # Подключение к Chrome
    driver = webdriver.ChromeOptions()
    driver.add_experimental_option('detach', True)
    path_chrome = Service('D:/Necessary/QA/drivers')
    driver = webdriver.Chrome(options=driver, service=path_chrome)
    print('Start Test')

    lp = LoginPage(driver)
    lp.authorization()

    mp = MainPage(driver)  # mp = Main Page
    mp.select_product()

    cp = CartPage(driver)
    cp.product_confirm()

    uip = UserInformationPage(driver)
    uip.input_user_information()

    ov = OverviewPage(driver)
    ov.payment()

    fp = FinishPage(driver)
    fp.finish()
