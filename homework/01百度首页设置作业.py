from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep

# 获取浏览器对象
driver = webdriver.Chrome()
# 访问网站地址
url = 'https://www.baidu.com'
# 浏览器打开网站
driver.get(url)
# 浏览器最大化
driver.maximize_window()
# 获取鼠标事件对象
action = ActionChains(driver)
# 定位设置元素
css = driver.find_element_by_xpath(".//*[@id='u1']/a[8]")
# 调用鼠标移动（悬停）事件
action.move_to_element(css)
# 执行鼠标操作
action.perform()
sleep(3)
# 定位搜索设置元素
link = driver.find_element_by_class_name("setpref")
# 点击搜索设置
link.click()
sleep(3)
# 定位select元素
sel = driver.find_element_by_xpath(".//*[@id='nr']")
# 获取select对象
select = Select(sel)
# 选择select下option元素中value='50'的元素
select.select_by_value('50')
sleep(2)
# 定位保存设置元素并点击两次
# for i in range(1, 3):
driver.find_element_by_link_text("保存设置").click()
sleep(2)
# 获取弹出框对象
alert = driver.switch_to.alert
# 点击同意
alert.accept()
sleep(2)
# 关闭浏览器对象
driver.quit()
