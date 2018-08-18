from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep


driver = webdriver.Firefox()
url = "file:///C:/Users/Administrator.000/Desktop/day02/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html"
driver.get(url)
sel = driver.find_element_by_id("select")
select = Select(sel)
select.select_by_index(1)
sleep(2)
select.select_by_index(3)
sleep(2)
select.select_by_index(2)
sleep(3)
driver.quit()