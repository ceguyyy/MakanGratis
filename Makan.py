from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
import pandas as pd

def generate_weekdays(start_date, end_date):
    """Generate weekday dates in MM/DD/YYYY format."""
    dates = pd.date_range(start=start_date, end=end_date)  # 'B' excludes weekends
    return dates.strftime('%m/%d/%Y').tolist()

# User inputs
start_date = "2025/02/25"  
end_date = "2025/02/28"   
employee_id = "internship0001"     
full_name = "Christian Gunawan"     

# Generate list of weekdays
weekdays = generate_weekdays(start_date, end_date)

# Start Selenium WebDriver
driver = webdriver.Chrome()

# Open Google Form
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdpbhMNE-S8TLPohAu7nKMxJTybSkpFHJO5bgMOk9AKA-08dA/viewform"

for date in weekdays:
    try:
        driver.get(form_url)
        time.sleep(3)  # Allow time for form to load

        # Locate input fields
        #id_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        id_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        name_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        
        date_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
        # Clear any previous input
        id_field.clear()
        name_field.clear()
        date_field.clear()

        # Enter data
        id_field.send_keys(employee_id)
        name_field.send_keys(full_name)
        formatted_date_push = datetime.strptime(date, "%m/%d/%Y").strftime("%d/%m/%Y")
        print(f"formatted date {date}")
        date_field.send_keys(formatted_date_push)
        time.sleep(1)  # Small delay to ensure input is processed

        # Submit the form
        submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
        submit_button.click()
        
        print(f"Submitted form for {date}")

        time.sleep(2)  # Allow time for submission to process before next iteration

    except Exception as e:
        print(f"Error submitting form for {date}: {e}")

# Close the browser
driver.quit()
print("Form submission completed!")
