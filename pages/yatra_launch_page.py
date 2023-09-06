import logging

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from base.base_driver import BaseDriver
from utilities.utils import Utils

class LaunchPage(BaseDriver):
    log = Utils.custom_logger(logging.WARNING)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait
    DEPART_FROM_FIELD = "BE_flight_origin_city"
    def getDepartFrom(self):
        return self.wait_until_element_is_clickable(By.ID, self.DEPART_FROM_FIELD)

    def enterDepartFrom(self,loc):
        self.getDepartFrom().click()
        self.getDepartFrom().send_keys(loc)
        self.getDepartFrom().send_keys(Keys.ENTER)
        # city_list = self.wait_for_presense_of_elements(By.XPATH,"//div[@class='ac_results origin_ac']//ul//div//div//div//li")
        city_list = self.driver.find_elements(By.XPATH, "//div[@class='ac_results origin_ac']//ul//div//div//div//li")
        # print(len(city_list))
        self.log.warning("length of city list is 5:")
        for city in city_list:
            if "Bangalore (BLR)" in city.text:
                print(city.text)
                city.click()
                break
    # def depart_from(self,departloc):
    #     # bd =BaseDriver()
    #     origin = self.wait_until_element_is_clickable(By.ID, self.DEPART_FROM_FIELD)
    #     # origin = self.wait.until(EC.element_to_be_clickable((By.ID, "BE_flight_origin_city")))
    #     # origin = self.driver.find_element(By.ID,"BE_flight_origin_city")
    #     origin.click()
    #     origin.send_keys(departloc)
    #     # city_list = self.wait_for_presense_of_elements(By.XPATH,"//div[@class='ac_results origin_ac']//ul//div//div//div//li")
    #     city_list = self.driver.find_elements(By.XPATH, "//div[@class='ac_results origin_ac']//ul//div//div//div//li")
    #     print(len(city_list))
    #     for city in city_list:
    #         if "Bangalore (BLR)" in city.text:
    #             print(city.text)
    #             city.click()
    #             break

    def going_to(self, goingtoloc):
        arrival = self.wait_until_element_is_clickable(By.ID, "BE_flight_arrival_city")
        # arrival = self.wait.until(EC.element_to_be_clickable((By.ID, "BE_flight_arrival_city")))
    # arrival = self.driver.find_element(By.ID,"BE_flight_arrival_city")
        arrival.click()
        arrival.send_keys(goingtoloc)
        arrival.send_keys(Keys.ENTER)


    def selectdate(self,departuredate):
        ele = self.wait_until_element_is_clickable(By.ID, "BE_flight_origin_date")
        ele.click()
        # self.wait.until(EC.element_to_be_clickable((By.ID, "BE_flight_origin_date"))).click()
        origin_date_list = self.wait_for_presense_of_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//tr//td[@class !='inActiveTD']")
        # origin_date_list = self.wait.until(
        #     EC.presence_of_element_located((By.XPATH, "//div[@id='monthWrapper']//tbody//tr//td[@class !='inActiveTD']")))
        # origin_date_list = self.driver.find_elements(By.XPATH,
  #                                         "//div[@id='monthWrapper']//tbody//tr//td[@class !='inActiveTD']")
        for date in origin_date_list:
            if date.get_attribute("data-date") == departuredate:
                date.click()
                break
        time.sleep(4)
        self.driver.get_screenshot_as_file(".//test.png")
