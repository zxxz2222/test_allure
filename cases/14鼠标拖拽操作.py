from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
url = 'file:///C:/Users/Administrator.000/Desktop/day02/drop.html'
driver.get(url)
action = ActionChains(driver)
source = driver.find_element_by_id("div1")
target = driver.find_element_by_id("div2")
ele = action.drag_and_drop(source, target)
ele.perform()
sleep(3)
# driver.quit()
