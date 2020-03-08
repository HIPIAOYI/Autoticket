import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

print(driver.title)

btn = driver.find_element_by_id("su")
search_text = driver.find_element_by_id("kw")
search_text.clear();
search_text.send_keys("tencent")

attribute =search_text.get_attribute("type")
print(attribute)

attribute =btn.get_attribute("value")
print(attribute)

time.sleep(5)
btn.click();

#time.sleep(5)
#driver.quit()