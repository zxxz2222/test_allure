from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
url = "file:///C:/Users/Administrator.000/Desktop/day02/%E6%B3%A8%E5%86%8CA.html"
driver.get(url)
tel = driver.find_element_by_class_name("telA")
tel.send_keys("186111111111")
sleep(3)
driver.quit()
