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

driver = webdriver
class TestNavigate(unittest.TestCase):
    
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome('C://Users//kenneth.m//Desktop//DRI Backup Files//Git Hub Repo//python_automation//static//driver//chromedriver.exe', options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()

    # @pytest.fixture(autouse=True)
    # def test_setup(self):
    #     self.driver = driver
    #     chromeDriverPath = os.path.abspath("/static/driver/chromedriver.exe")
    #     print("Chrome Driver Path: " + chromeDriverPath)
    #     options = webdriver.ChromeOptions()
    #     options.add_argument("--headless")
    #     self.driver = webdriver.Chrome('C://Users//kenneth.m//Desktop//DRI Backup Files//Git Hub Repo//python_automation//static//driver//chromedriver.exe', options=options)
    #     self.driver.implicitly_wait(10)
    #     self.driver.maximize_window()
    #     yield
    #     driver.quit()

    @allure.description("go to youtube website")
    # @allure.step("Open youtube website") 
    @allure.severity(severity_level="NORMAL")
    def test_open_youtube(self):
        print('Open youtube website....')
        driver.get("https://www.youtube.com/")
        # typing_in_google_search("jenkins")
        # allureResultPath = os.path.abspath("C://Users//kenneth.m//Desktop//DRI Backup Files//Git Hub Repo//python_automation//allure-results")
        # with open(allureResultPath, 'rb') as image:
        #     file = image.read()
        #     byte_array = bytearray(file)
        #     allure.attach(byte_array, name="youtube_website", attachment_type=AttachmentType.PNG)
        allure.attach(driver.get_screenshot_as_png(), name="youtube_website", attachment_type=AttachmentType.PNG)
        print('youtube Success!')
        
    @allure.description("go to gmail")
    @allure.severity(severity_level="NORMAL")
    def test_open_gmail(self):
        print('Open gmail website....')
        driver.get("https://www.gmail.com/")
        print('Gmail Success!')

    # @allure.step("Search {0} in google website ")
    # def typing_in_google_search(keyword):
    #     WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.NAME, "q"))).send_keys(keyword)

if __name__ == '__main__':
    unittest.main()
