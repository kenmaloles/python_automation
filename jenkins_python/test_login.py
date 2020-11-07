import pytest
from selenium import webdriver
import os
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from allure_commons.types import AttachmentType                                                      

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome('C://Users//kenneth.m//Desktop//DRI Backup Files//Git Hub Repo//python_automation//static//driver//chromedriver.exe', options=options)
@allure.severity(severity_level="NORMAL")
class TestLogin(unittest.TestCase):
    global driver
    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    # driver = webdriver.Chrome('C://Users//kenneth.m//Desktop//DRI Backup Files//Git Hub Repo//python_automation//static//driver//chromedriver.exe', options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()

    # @pytest.fixture(autouse=True)
    # @allure.description("Setup Chrome Driver...")
    # @allure.severity(severity_level="NORMAL")
    # def test_setup(self):
        # self.driver = webdriver.Chrome()
        # chromeDriverPath = os.path.abspath("/static/driver/chromedriver.exe")
        # print("Chrome Driver Path: " + chromeDriverPath)
        # options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        # self.driver = webdriver.Chrome('C://Users//kenneth.m//Desktop//DRI Backup Files//Git Hub Repo//python_automation//static//driver//chromedriver.exe', options=options)
        # self.driver.implicitly_wait(10)
        # self.driver.maximize_window()
        # self.driver.quit()

    @allure.description("go to google website")
    @allure.severity(severity_level="CRITICAL")
    def test_open_google(self):
        print('Open google website....')
        driver.get("https://www.google.com/")
        self.typing_in_google_search("jenkins")
        allure.attach(driver.get_screenshot_as_png(), name="google_website", attachment_type=AttachmentType.PNG)
        print('Google Success!')
        
    @allure.description("go to yahoo website")
    @allure.severity(severity_level="NORMAL")
    def test_open_yahoo(self):
        print('Open yahoo website....')
        driver.get("https://www.yahoo.com/")
        print('yahoo Success!')

    @allure.step("Search {0} in google website ")
    def typing_in_google_search(self, keyword):
        WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "q"))).send_keys(keyword)

# def test_quit_driver():
#     driver.quit()

if __name__ == '__main__':
    unittest.main()