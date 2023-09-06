from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self,driver):
        self.driver = driver

    def scroll_page(self):
        pass

    def wait_for_presense_of_elements(self,locator_type,locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_elements = wait.until(EC.presence_of_element_located((locator_type,locator)))
        return list_of_elements

    def wait_until_element_is_clickable(self,locator_type,locator):
        wait = WebDriverWait(self.driver,10)
        element = wait.until(EC.element_to_be_clickable((locator_type,locator)))
        return element