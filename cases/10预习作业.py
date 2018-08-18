# 需求：
#     1. 通过脚本执行输入：
#        用户名：admin；密码：123456；电话号码：18611111111；电子邮件：123@qq.com
#     2. 间隔3秒后，修改电话号码为：18600000000
#     3. 间隔3秒，点击注册用户A
#     4. 间隔3秒，关闭浏览器
#     5. 元素定位方法不限
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()
url = "file:///C:/Users/Administrator.000/Desktop/day02/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html"
driver.get(url)
user = driver.find_element_by_xpath(".//*[@id='user']")
password = driver.find_element_by_css_selector("#password")
phone = driver.find_element_by_xpath(".//*[@id='tel']")
email = driver.find_element_by_css_selector("#email")
# button = driver.find_element_by_xpath(".//*[@id='zc']/fieldset/button")
button = driver.find_element_by_xpath("//button[text()='注册用户']")
user.send_keys("admin")
password.send_keys("123456")
phone.send_keys("18611111111")
email.send_keys("123@qq.com")
sleep(3)
phone.clear()
phone.send_keys("18600000000")
sleep(3)
button.click()
sleep(3)
driver.quit()