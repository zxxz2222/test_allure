from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
assert "百度" in driver.title
elem = driver.find_element_by_name("wd")
elem.send_keys("Eastmount")
elem.send_keys(Keys.RETURN)
driver.save_screenshot('baidu.png')
driver.close()
driver.quit()