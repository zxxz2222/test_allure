from selenium import webdriver
from time import sleep


driver = webdriver.Firefox()
url = "file:///C:/Users/Administrator.000/Desktop/day02/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html"
driver.get(url)
driver.maximize_window()
driver.find_element_by_id('alert').click()
sleep(2)
alert = driver.switch_to.alert
alert.accept()
driver.find_element_by_id("user").send_keys("admin")


sleep(3)
driver.quit()