from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time


def select_feedback_options(driver):
    while(1):
        driver.find_element(By.XPATH, "//input[@value='5']").click()
        time.sleep(2)
        nextButton = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='submit']")))
        nextButton.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='submit']")))

        try:
            dropdown = Select(driver.find_element(By.NAME, "Subject"))
            time.sleep(2)
            return
        except NoSuchElementException:
            time.sleep(2)
            continue

username = input("Enter your uid: ")
password = input("Enter your password: ")

try:
    print("Logging in to you rsms account...")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # driver.maximize_window()
    driver.get("https://www.rajagiritech.ac.in/stud/ktu/student/")
    driver.find_element(By.NAME, "Userid").send_keys(username)
    driver.find_element(By.NAME, "Password").send_keys(password)
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    try:
        driver.find_element(By.LINK_TEXT, "Course Feedback").click()
    except NoSuchElementException:
        print("Incorrect credentials")
        raise SystemExit
    print("Successfully logged in...\n")
    
    driver.find_element(By.NAME, "Userid").send_keys(username)
    driver.find_element(By.NAME, "Pass").send_keys(password)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='submit']")))
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='submit']")))
     
    dropdown = Select(driver.find_element(By.NAME, "Subject"))
    options = [option.get_attribute("value") for option in dropdown.options]
    
    for optionn in options:
        try: 
            dropdown = Select(driver.find_element(By.NAME, "Subject"))
            dropdown.select_by_value(optionn)
            
            time.sleep(2)
            driver.find_element(By.XPATH, "//input[@type='submit']").click()
        
            try:
                driver.find_element(By.XPATH, "//input[@type='submit']")
            except NoSuchElementException:
                print(f"Questions not added by Teacher for {optionn}")
                driver.back()
                time.sleep(2)
                continue
            
        
            select_feedback_options(driver)
            print(f"Feedback for {optionn} completed")

        except NoSuchElementException as e:
            print(f"No sych element found: {e}")
            break
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break
    
finally:
    time.sleep(0.5)
    print("\nFeedback process completed.")
    driver.quit()
