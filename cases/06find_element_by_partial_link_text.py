from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()
url = "file:///C:/Users/Administrator.000/Desktop/day02/%E6%B3%A8%E5%86%8CA.html"
driver.get(url)
driver.find_element_by_partial_link_text("新浪").click()

sleep(3)
driver.quit()
