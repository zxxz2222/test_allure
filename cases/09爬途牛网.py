from selenium import webdriver

options = webdriver.FirefoxOptions()
browser = webdriver.Firefox()
browser.get(
    'http://flight.tuniu.com/domestic/list/CKG_BJS_ST_1_0_0/?start=2018-07-05')

elements = browser.find_elements_by_xpath(
    '//div[@class="J-flightlist"]')  # 每个航班最外层的div
for element in elements:
    airline_element = element.find_element_by_xpath(
        './/div[@class="fl-logo"]//div[@class="aircom"]')  # 航空公司信息
    flight_element = element.find_element_by_xpath(
        './/div[@class="fl-logo"]//div[@class="flihtnumber left"]')  # 航班信息
    depart_time_element = element.find_element_by_xpath(
        './/div[@class="fl-depart"]//p[@class="hours"]')  # 出发时间
    arrive_time_element = element.find_element_by_xpath(
        './/div[@class="fl-arrive"]//span[@class="hours"]/span')  # 到达时间
    space_time_element = element.find_element_by_xpath(
        './/div[@class="fl-center"]//p[@class="durationTime"]')  # 花费时间
    depart_airport_element = element.find_element_by_xpath(
        './/div[@class="fl-depart"]//p[@class="airport"]')  # 出发机场
    arrive_airport_element = element.find_element_by_xpath(
        './/div[@class="fl-arrive"]//p[@class="airport"]')  # 到达机场
    price_element = element.find_element_by_xpath(
        './/div[@class="price"]//span[@class="num"]')  # 机票价格
    air = {
        'airline': airline_element.text,
        'flight': flight_element.text,
        'depart_time': depart_time_element.text,
        'arrive_time': arrive_time_element.text,
        'space_time': space_time_element.text,
        'depart_airport': depart_airport_element.text,
        'arrive_airport': arrive_airport_element.text,
        'price': price_element.text
    }
    print(air)  # 输出到控制台

# browser.quit()  # 关闭浏览器
