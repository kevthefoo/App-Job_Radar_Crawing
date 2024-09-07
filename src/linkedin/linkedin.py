import time, json, config

from src.message import sendMessage
from src.classify import locationClassify

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

URL = config.LINKEDIN

def job_id_exists(job_id, file_path='./data/linkedin.json'):
    with open(file_path, 'r') as f:
        data = json.load(f)
    if job_id in data:
        print("System: Job ID already exists")
        return True
    else:
        print("System: New Job ID found")
        return False

def linkdedin(driver):
    driver.get(URL)
    time.sleep(5)

    while True:
        # Scroll down the page smoothly
        side_bar_results = driver.find_element(By.CLASS_NAME, "jobs-search-results-list")
        driver.execute_script("""arguments[0].scrollTo({top: arguments[0].scrollHeight,behavior: 'smooth'});""", side_bar_results)

        # Target the pagination bar and find the next page button
        pagination_bar = side_bar_results.find_element(By.CLASS_NAME, "artdeco-pagination__pages")
        current_page = pagination_bar.find_element(By.CLASS_NAME, "selected")
        try:
            next_page = current_page.find_element(By.XPATH, "following-sibling::li")
        except:
            print("System: No more pages to load...")
            break

        driver.execute_script("""arguments[0].scrollTo({top: arguments[0].scrollHeight,behavior: 'smooth'});""", side_bar_results)
        time.sleep(3)

        # Fetch all jobs entry in the side bar
        side_bar_entry = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
        side_bar_results = driver.find_element(By.CLASS_NAME, "jobs-search-results-list")
        job_title_element = side_bar_results.find_elements(By.CLASS_NAME, "job-card-list__title--link")


        print(len(job_title_element))
        print(len(side_bar_entry))
        if len(job_title_element) != len(side_bar_entry):
            # Scroll up the page smoothly
            driver.execute_script("""arguments[0].scrollTo({top: 0,behavior: 'smooth'});""", side_bar_results)
            time.sleep(3)
            print("System: Found", len(job_title_element), "Jobs")
            print("System: Found", len(side_bar_entry), "Jobs")
        else:
            count = 0
            for job_entry in side_bar_entry:
                # Get the job ID
                job_id = job_entry.get_attribute("data-occludable-job-id")
                print(job_id)
                if job_id_exists(job_id):
                    continue
                
                # Get the job source
                job_source = "LinkedIn"

                # Get the job title
                job_title_element = job_entry.find_element(By.CLASS_NAME, "job-card-list__title--link")
                job_title = job_title_element.text.split("\n")[0].strip()
                
                # Get the job URL
                job_url = job_title_element.get_attribute("href")

                # Get the company name
                company_name = job_entry.find_element(By.CLASS_NAME, "job-card-container__primary-description").text.strip()

                # Get the job location
                job_location = job_entry.find_element(By.CLASS_NAME, "artdeco-entity-lockup__caption").text.strip()

                new_data = {
                    "job_id": job_id,
                    "job_title": job_title,
                    "company_name": company_name,
                    "job_location": job_location,
                    "job_url": job_url,
                    "label":{
                        "state":"",
                        "city":"",
                        "title":"",
                        "language":"",
                        "framework":"",
                    },
                    "timestamp": int(time.time())
                }

                new_data =  locationClassify(new_data)

                # Read existing data
                try:
                    with open('./data/linkedin.json', 'r') as f:
                        data = json.load(f)
                except FileNotFoundError:
                    print("System: File not found. Creating a new file.")
                    return

                # Add new data to the existing dictionary
                data[job_id] = new_data

                # Write updated data back to the file
                with open('./data/linkedin.json', 'w') as f:
                    json.dump(data, f, indent=4)

                print(f"System: {count+1} New Jobs Found\n")
                content = f'Job Title:\n{job_title}\n\nLocation:\n{job_location}\n\nCompany:\n{company_name}\n\nJob URL:\n{job_url}\n\nSource: \n{job_source}'
                sendMessage(content)
                time.sleep(3)
                count += 1
            

            next_page.click()
            for second in range(30):
                print(f"System: Waiting for {30-second} seconds to load the next page")
                time.sleep(1)