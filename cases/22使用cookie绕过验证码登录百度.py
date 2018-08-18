from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
url = 'https://www.baidu.com'
BAIDUID = 'A3984BB72C68C4B1BA80AE769A9D74C7:SL=0:NR=50:FG=1'
BDUSS = 'I3UzNmTmUtYmtoRmpKVGN5bGNpMnV4NmRmTVc5ZjMzcGJCaWpIaS1nOUt2VmxiQVFBQUFBJCQAAAAAAAAAAAEAAADchIA~0MezvXPEpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEowMltKMDJbM3'
dict1 = {'name':'BAIDUID','value':BAIDUID}
dict2 = {'name':'BDUSS','value':BDUSS}
driver.get(url)
driver.add_cookie(dict1)
driver.add_cookie(dict2)
driver.refresh()

print(driver.get_cookies())
sleep(2)
driver.quit()