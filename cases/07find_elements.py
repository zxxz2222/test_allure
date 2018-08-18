from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
url = "file:///C:/Users/Administrator.000/Desktop/day02/%E6%B3%A8%E5%86%8CA.html"
driver.get(url)
lists = driver.find_elements_by_tag_name("input")
lists[0].send_keys("admin")
lists[1].send_keys("123456")
sleep(3)
driver.quit()
