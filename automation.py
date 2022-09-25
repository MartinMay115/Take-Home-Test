import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("./chromedriver")

driver.get("https://www.google.de")
time.sleep(4)

keywords = ["ratenzahlung", "flexibel online shoppen"]
results = {}

# Accept cookie popup
cookies_button = driver.find_element(By.CLASS_NAME, "sy4vM")
cookies_button.click()

for keyword in keywords:
    driver.get("https://www.google.de")

    # Search for keyboard
    search = driver.find_element(By.NAME, "q")
    search.send_keys(keyword)
    search.send_keys(Keys.RETURN)

    # Click first search result
    search = driver.find_element(By.CLASS_NAME, "DKV0Md")
    result_title = search.text
    search.click()

    # get displayed url
    result_url = driver.current_url
    results[result_url] = result_title

print(results)




