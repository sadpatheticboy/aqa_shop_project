from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from pages.main_page import MainPage
from utilities.conftest import set_group


def test_link_about(set_group):
    # Подключение к Chrome
    driver = webdriver.ChromeOptions()
    driver.add_experimental_option('detach', True)
    path_chrome = Service('D:/Necessary/QA/drivers')
    driver = webdriver.Chrome(options=driver, service=path_chrome)
    print('Start Test')

    lp = LoginPage(driver)
    lp.authorization()

    mp = MainPage(driver)
    mp.go_to_menu_about()
