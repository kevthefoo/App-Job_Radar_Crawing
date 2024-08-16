import time, subprocess, requests, os, json
from web_list import web_list
import config

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

chrome_path = config.chrome_browser_path
user_profile_path = config.user_profile_path

# Launch Chrome in debug mode
subprocess.Popen([chrome_path, '--remote-debugging-port=9222', f'--user-data-dir={user_profile_path}'])

# --------------------------------------Initialize Selenium--------------------------------------

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# --------------------------------------Go To The Target URL--------------------------------------

while True:
    for web in web_list:
        inspect_url = web["url"]
        driver.get(inspect_url)

        



        time.sleep(5000)