from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
url = "file:///C:/Users/Administrator.000/Desktop/day02/%E6%B3%A8%E5%86%8CA.html"
driver.get(url)
search = driver.find_element_by_name("userA")
search.send_keys("admin")
button = driver.find_element_by_name("passwordA")
button.send_keys("123456")
sleep(3)
driver.quit()
