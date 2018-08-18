from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()
url = 'https://www.douyu.com'
driver.get(url)
driver.find_element_by_css_selector('.pop-zoom-hide').click()
sleep(2)
driver.find_element_by_xpath(".//*[@id='header']/div/ul/li[2]/a").click()
sleep(2)
driver.find_element_by_xpath(".//*[@id='J-pager']/a[3]").click()
sleep(2)
driver.quit()