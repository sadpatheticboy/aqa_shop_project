from base.base_class import Base


class FinishPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Methods
    def finish(self):
        self.get_current_url()
        self.take_screenshot()
