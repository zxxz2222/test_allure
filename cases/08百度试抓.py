from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
url = "https://www.baidu.com"
driver.get(url)
sea = driver.find_element_by_id("kw")
sea.send_keys("淘宝网")
driver.find_element_by_id("su").click()
driver.find_element_by_xpath(".//*[@id='1']/h3/a[1]").click()
sleep(5)
driver.quit()