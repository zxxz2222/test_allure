from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
url = 'file:///C:/Users/Administrator.000/Desktop/day02/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html'
driver.get(url)
driver.switch_to.frame('myframe1')
driver.find_element_by_id('userA').send_keys('admin')
driver.find_element_by_id('passwordA').send_keys('123456')
driver.find_element_by_id('telA').send_keys('13048859741')
driver.find_element_by_id('emailA').send_keys('admin@QQ.COM')
driver.get_screenshot_as_file('./bug.png')


sleep(3)
driver.quit()