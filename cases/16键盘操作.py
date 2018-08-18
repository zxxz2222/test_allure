# 需求：
#     1). 输入用户名：admin1     暂停2秒，删除1
#     2). 全选用户名：admin      暂停2秒
#     3). 复制用户名：admin      暂停2秒
#     4). 粘贴到密码框           暂停2秒
#     5). 关闭浏览器
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
url = "file:///C:/Users/Administrator.000/Desktop/day02/%E6%B3%A8%E5%86%8CA.html"
driver.get(url)
username = driver.find_element_by_id("userA")
password = driver.find_element_by_id("passwordA")
username.send_keys("admin1")
sleep(2)
username.send_keys(Keys.BACK_SPACE)
sleep(2)
username.send_keys(Keys.CONTROL, 'a')
sleep(2)
username.send_keys(Keys.CONTROL, 'c')
sleep(2)
password.send_keys(Keys.CONTROL, 'v')


sleep(2)
driver.quit()