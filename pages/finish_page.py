from base.base_class import Base
from utilities.logger import Logger


class FinishPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Methods
    def finish(self):
        Logger.add_start_step(method="finish")
        self.get_current_url()
        self.assert_url_check("https://www.saucedemo.com/checkout-complete.html")
        self.take_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method="finish")
