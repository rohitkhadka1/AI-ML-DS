from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Set up the WebDriver (Make sure you have the correct driver installed)
driver = webdriver.Chrome()
driver.get("https://www.google.com")
# Find the search box and input the query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Tutorial")
search_box.send_keys(Keys.RETURN)
# Wait for results to load
time.sleep(2)
# Close the browser
#driver.quit()