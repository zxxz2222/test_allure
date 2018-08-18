from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# //*[@id="kw"]
driver = webdriver.Firefox()
# 通过浏览器对象打开指定网页
driver.get("file:///C:/Users/Administrator.000/Desktop/day02/%E6%B3%A8%E5%86%8CA.html")
# 通过元素id属性定位获取元素对象
element1 = driver.find_element_by_id("userA")
# 通过元素id属性定位获取元素对象
element2 = driver.find_element_by_id("passwordA")
# 清空元素内容
element1.clear()
# 通过键盘事件向元素输入数据
element1.send_keys("admin")
element2.clear()
# 通过键盘事件向元素输入数据
element2.send_keys("123456")
# 等待3秒
sleep(3)
# 关闭浏览器窗口
driver.close()
# 退出浏览器
driver.quit()
driver = webdriver.Firefox()
url = "https://www.baidu.com"
driver.get(url)
serchr = driver.find_element_by_id("kw")
serchr.send_keys("淘宝")
button = driver.find_element_by_id("su")
button.click()
sleep(3)
driver.quit()

