import pytest
from selenium import webdriver
import os
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver
@pytest.fixture()
def test_setup():
    global driver
    # chromeDriverPath = os.path.abspath("/static/driver/chromedriver.exe")
    driver = webdriver.Chrome('C://Users//kenneth.m//Desktop//DRI Backup Files//Git Hub Repo//python_automation//static//driver//chromedriver.exe')
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.quit()

@allure.description("go to google website")
@allure.severity(severity_level="CRITICAL")
def test_open_google(test_setup):
    print('Open google website....')
    driver.get("https://www.google.com/")
    typing_in_google_search("jenkins")
    allure.attach(driver.get_screenshot_as_png(), name="google website", attachment_type=allure.attachment_type.PNG)
    print('Google Success!')
    
@allure.description("go to facebook website")
@allure.severity(severity_level="NORMAL")
def test_open_facebook(test_setup):
    print('Open facebook website....')
    driver.get("https://www.facebook.com/")
    print('Facebook Success!')

@allure.step("Search {0} in google website ")
def typing_in_google_search(keyword):
    WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "q"))).send_keys(keyword)


# def test_quit_driver():
#     driver.quit()