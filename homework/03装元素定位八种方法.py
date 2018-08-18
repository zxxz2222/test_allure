class Positioning(object):
    # element接收定位元素字符串（例如//*[@id='header']/div/ul/li[2]/a），
    # driver操作的浏览器对象
    def __init__(self, element, driver):
        self.element = element
        self.driver = driver

    # 封装定位元素方法，type使用什么方法进行定位，例如使用id定位元素则传入id
    def positioning_element(self, type):
        if type == 'xpath':
            ele = self.driver.find_element_by_by_xpath(self.element)
            return ele
        elif type == 'id':
            ele = self.driver.find_element_by_id(self.element)
            return ele
        elif type == 'link_text':
            ele = self.driver.find_element_by_link_text(self.element)
            return ele
        elif type == 'partial_link_text':
            ele = self.driver.find_element_by_partial_link_text(self.element)
            return ele
        elif type == 'name':
            ele = self.driver.find_element_by_name(self.element)
            return ele
        elif type == 'tag_name':
            ele = self.driver.find_element_by_tag_name(self.element)
            return ele
        elif type == 'class_name':
            ele = self.driver.find_element_by_class_name(self.element)
            return type
        elif type == 'css_selector':
            ele = self.driver.find_element_by_css_selector(self.element)
            return ele
        else:
            print("无法找到元素")
