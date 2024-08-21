import time, subprocess, requests, os, json, config
from web_list import web_list

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from src.linkedin.linkedin import linkdedin

# --------------------------------------Initialize Chrome--------------------------------------
chrome_path = config.chrome_browser_path
user_profile_path = config.user_profile_path

# Launch Chrome in debug mode
subprocess.Popen([chrome_path, '--remote-debugging-port=9222', f'--user-data-dir={user_profile_path}'])

# --------------------------------------Initialize Selenium--------------------------------------

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# --------------------------------------Main--------------------------------------

def main():
    linkdedin(driver)

    print("System: Done")


if __name__ == "__main__":
    main()