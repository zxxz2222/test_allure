from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
url = 'https://www.taobao.com'
driver.get(url)
driver.maximize_window()
js = 'window.scrollTo(0,10000)'
driver.execute_script(js)

sleep(3)
driver.quit()