from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.user_information_page import UserInformationPage


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

    # enter_cart = WebDriverWait(driver, 10).until(
    #     expected_conditions.element_to_be_clickable((By.XPATH, "//div[@id='shopping_cart_container']")))
    # enter_cart.click()  # Entry Cart
    # print('Click Cart')
