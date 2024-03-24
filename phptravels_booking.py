# Selenium Python Task:
# 1. Go to URL: https://www.phptravels.net/
# 2. Select a radio button (one way / multiway)
# 3. Select a flying from option
# 4. Select a destination to option
# 5. Select a departed date
# 6. Select travelers
# 7. Search a flight
# 8. Verify that the flight search is successful
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Firefox()
driver.get('https://www.phptravels.net/')
driver.maximize_window()
time.sleep(15)
driver.find_element("xpath", "(//a[@href='javascriptvoid(0)'])[3]").click()
driver.find_element("xpath", "(//a[@href='https://www.phptravels.net/login'])").click()
driver.find_element("name", "email").send_keys("user@phptravels.com")
driver.find_element('id', 'password').send_keys('demouser')
time.sleep(10)
driver.find_element('id', 'submitBTN').click()
time.sleep(15)
driver.find_element("xpath","(//a[normalize-space()='Flights'])").click()
time.sleep(10)
driver.find_element("xpath","(//label[normalize-space()='One Way'])").click()
driver.find_element("xpath","((//strong[@class='mt-2'][normalize-space()='Select City'])[1])").click()
driver.find_element("xpath","(//button[normalize-space()='MNL'])").click()
driver.find_element("xpath","((//span[@id='select2--container'])[2])").click()
driver.find_element("xpath","(//small[normalize-space()='John F Kennedy International Airport'])").click()
driver.find_element("xpath","(//input[@id='departure'])").click()
driver.find_element("xpath","((//td[contains(text(),'13')])[1])").click()
driver.find_element("xpath","(//a[@class='dropdown-toggle dropdown-btn travellers waves-effect'])").click()
driver.find_element("xpath","((//div[@class='qty-box d-flex align-items-center justify-content-between'])[1])").click()
driver.find_element("xpath","(//select[@id='flight_type'])").click()
driver.find_element("xpath","(//option[@value='business'])").click()
driver.find_element("xpath","(//button[@id='flights-search'])").click()
time.sleep(10)
radio_list = driver.find_elements(By.NAME, "type")

for rbtn in radio_list:
    rbtn_attr = rbtn.get_attribute("value")
    print(rbtn_attr)
    if rbtn_attr ==type:
        if rbtn.is_selected():
             print("The radio button is already selected")
        else:
            rbtn.click()
            print("The radio button is selected")
        break
#driver.find_element("xpath","(//form)[4]").click()
#time.sleep(10)