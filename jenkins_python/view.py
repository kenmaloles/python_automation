from django.shortcuts import render
from django.template.loader import render_to_string
import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
from datetime import datetime
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.firefox.options import Log
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index(request):
    return render(request, 'home.html')

@app.route('/testResult', methods = ['POST', 'GET'])
def testResult(request):
    print('Running headless...')
    options = webdriver.ChromeOptions()
    log = Log()
    log.level = "SEVERE"
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    options.add_argument("--incognito")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument("--start-fullscreen")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("disable-infobars") 
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--allow-insecure-localhost")
    options.add_argument("--log-level=3")
    options.add_argument("--headless")
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument(log.level)
    driver = webdriver.Chrome(executable_path=os.path.abspath("static/driver/chromedriver.exe"), chrome_options=options)
    print('Open google.com website....')
    driver.get("https://www.google.com/")
    print('Success!')

    return render(request, 'home.html')

if __name__ == "__main__":
    app.run()