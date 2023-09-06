import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


from pages.yatra_launch_page import LaunchPage
from utilities.utils import Utils

@pytest.mark.usefixtures("setup")
class TestSearchFlights:
    def test_search_flight_method(self):
        lp = LaunchPage(self.driver)

        # lp.depart_from("Banglore")
        lp.enterDepartFrom("Bangalore")
       # city_list = lp.wait_for_presense_of_elements(By.XPATH, "//div[@class='ac_results origin_ac']//ul//div//div//div//li")
        lp.going_to("pune")

        # lp.selectdate("03/09/2023")

        ut = Utils()
        list = ['1','2',"3",'4','4']
        # ut.assert_text(list,list.__contains__('3') )

        # time.sleep(3)

        # self.wait.until(EC.element_to_be_clickable((By.ID,"BE_flight_origin_date"))).click()
        # # origin_date = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        # # time.sleep(3)
        # # origin_date.click()
        # origin_date.screenshot(".//date1.png")
        # origin_date_list = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@id='monthWrapper']//tbody//tr//td[@class !='inActiveTD']")))
        #
        # # origin_date_list = self.driver.find_elements(By.XPATH,
        # #                                         "//div[@id='monthWrapper']//tbody//tr//td[@class !='inActiveTD']")
        #
        # for date in origin_date_list:
        #     if date.get_attribute("data-date") == "03/09/2023":
        #         date.click()
        #         break
        # time.sleep(4)
        # self.driver.get_screenshot_as_file(".//test.png")




