from base.base_driver import BaseDriver


class SearchFlights(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def search_flight(self):
        pass
