from selenium import webdriver
from time import sleep
# 1. 如何获取元素大小？
# 2. 如果获取元素的文本？
# 3. 如何获取元素属性的值？
# 4. 如果让程序判断元素是否为可见状态？

driver = webdriver.Firefox()
url = "http://www.baidu.com"
driver.get(url)
driver.find_element_by_id("kw").send_keys("淘宝")
button = driver.find_element_by_id("su")
print(button.size,button.text,button.get_attribute("value"),button.is_displayed())
button.click()
sleep(3)
driver.back()
sleep(3)
driver.forward()
sleep(3)
driver.refresh()
sleep(3)
driver.close()