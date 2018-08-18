from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
url = "file:///C:/Users/Administrator.000/Desktop/day02/%E6%B3%A8%E5%86%8CA.html"
driver.get(url)
input = driver.find_element_by_xpath("//input[@id='userA']")
password = driver.find_element_by_xpath("//input[@id='passwordA']")

password.send_keys("123456")
input.send_keys("admin")
sleep(3)
driver.quit()