# 需求：对iweb_shop项目进行前台登录设计脚本
# 要求：
# 1.	使用unittest框架
# 2.	使用Fixture(setup、tearDown)
# 3.	浏览器最大化、隐式等待30秒
# 4.	使用断言判断登录用户是否为admin，不是则截屏保存图片
# 5.	图片命名格式为脚本执行时间
# 6.	暂停2秒退出、暂停2秒关闭浏览器
# 7.	元素定位方式不限
import unittest
from selenium import webdriver
from time import strftime, sleep


class IWebShop(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        url = 'http://localhost:8080/iwebshop/index.php?controller=site&action=index'
        self.driver.get(url)
        self.driver.implicitly_wait(30)

    def test_login(self):
        self.driver.find_element_by_link_text('登录').click()
        self.driver.find_element_by_name('login_info').send_keys('星辰')
        self.driver.find_element_by_name('password').send_keys('20031866')
        self.driver.find_element_by_class_name('submit_login').click()
        content = self.driver.find_element_by_class_name('loginfo').text
        img_file = strftime('%Y_%m_%d %H_%M_%S')
        print(content)
        print(img_file)
        try:
            unittest.TestCase.assertIn(self,'admin',content)
        except AssertionError:
            self.driver.get_screenshot_as_file('./%s.png' % img_file)


    def tearDown(self):
        sleep(2)
        self.driver.close()
        sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
