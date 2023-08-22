import allure

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.description("Test Link About")
def test_link_about():
    # Подключение к Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.page_load_strategy = 'eager'
    path_chrome = Service(executable_path='D:/Necessary/QA/drivers/chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=path_chrome)
    print('Start Test')

    lp = LoginPage(driver)
    lp.authorization()

    mp = MainPage(driver)
    mp.go_to_menu_about()
