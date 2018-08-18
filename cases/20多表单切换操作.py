from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
url = 'file:///C:/Users/Administrator.000/Desktop/day02/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html'
driver.get(url)
driver.find_element_by_id('user').send_keys('admin')
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_id('tel').send_keys('13048859741')
driver.find_element_by_id('email').send_keys('123@qq.com')

driver.switch_to_frame('idframe1')

driver.find_element_by_id('userA').send_keys('adminA')
driver.find_element_by_id('passwordA').send_keys('123456A')
driver.find_element_by_id('telA').send_keys('13048859741A')
driver.find_element_by_id('emailA').send_keys('123A@qq.com')

driver.switch_to_default_content()

driver.switch_to_frame('myframe2')

driver.find_element_by_id('userB').send_keys('adminB')
driver.find_element_by_id('passwordB').send_keys('123456B')
driver.find_element_by_id('telB').send_keys('13048859741B')
driver.find_element_by_id('emailB').send_keys('123B@qq.com')

sleep(3)
driver.quit()