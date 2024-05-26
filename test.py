from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time

username = 'u2109064'
password = '211022'

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
    print("Redirected to course feedback page...\n")
    
    
    dropdown = Select(driver.find_element(By.NAME, "Subject"))
    options = dropdown.options
    
    for option in options:
        try: 
            option_text = option.text
            option_value = option.get_attribute("value")
            print(option_text)
            
            

        except NoSuchElementException:
            print("Feedback submission completed!.")
            break
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break
        

    
    
    
finally:
    time.sleep(2)
    driver.quit()
