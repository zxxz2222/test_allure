from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Firefox()
url = url = "file:///C:/Users/Administrator.000/Desktop/day02/%E6%B3%A8%E5%86%8CA.html"
driver.get(url)
# action = ActionChains(driver)
# button = driver.find_element_by_css_selector("button")
# action.move_to_element(button)
# action.perform()

ActionChains(driver).move_to_element(driver.find_element_by_css_selector("button")).perform()
sleep(3)
driver.quit()