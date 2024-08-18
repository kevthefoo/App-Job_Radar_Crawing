import time
import config

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

URL = config.LINKEDIN

def linkdedin(driver):
    driver.get(URL)
    time.sleep(5)

    while True:
        # Scroll down the page smoothly
        side_bar_results = driver.find_element(By.CLASS_NAME, "jobs-search-results-list")
        driver.execute_script("""arguments[0].scrollTo({top: arguments[0].scrollHeight,behavior: 'smooth'});""", side_bar_results)
        time.sleep(3)

        # Fetch all jobs entry in the side bar
        side_bar_entry = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
        side_bar_results = driver.find_element(By.CLASS_NAME, "jobs-search-results-list")
        job_title_element = side_bar_results.find_elements(By.CLASS_NAME, "job-card-list__title--link")

        if len(job_title_element) == len(side_bar_entry):
            break
        else:
            # Scroll up the page smoothly
            driver.execute_script("""arguments[0].scrollTo({top: 0,behavior: 'smooth'});""", side_bar_results)
            time.sleep(3)
            print("System: Found", len(job_title_element), "Jobs")
            print("System: Found", len(side_bar_entry), "Jobs")

    for job_entry in side_bar_entry:
        # Get the job ID
        job_id = job_entry.get_attribute("data-occludable-job-id")

        # Get the job title
        job_title_element = job_entry.find_element(By.CLASS_NAME, "job-card-list__title--link")
        job_title = job_title_element.text.split("\n")[0].strip()
        
        # Get the job URL
        job_url = job_title_element.get_attribute("href")

        # Get the company name
        company_name = job_entry.find_element(By.CLASS_NAME, "job-card-container__primary-description").text.strip()

        # Get the job location
        job_loaction = job_entry.find_element(By.CLASS_NAME, "artdeco-entity-lockup__caption").text.strip()

        print("No.", side_bar_entry.index(job_entry)+1)
        print("Job ID:", job_id, "\nJob Title:", job_title, "\nJob Location:", job_loaction, "\nCompany Name:", company_name, "\nJob URL:", job_url, "\n\n----------------------------------------")