from selenium import webdriver
from time import sleep
import random

#
# #driver = webdriver.Firefox()
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)  # 隐性等待，最长等30秒
# driver.get("http://47.106.144.234:9000")
# sleep(2)
#
#
#
# # 登录
# driver.find_element_by_xpath('//*[@id="app"]/div/div/div/form/div[1]/div/div/input').send_keys('18575074750')
# driver.find_element_by_xpath('//*[@id="app"]/div/div/div/form/div[2]/div/div/input').send_keys('12345678')
# driver.find_element_by_xpath('//*[@id="app"]/div/div/div/form/button').click()

modName = '自动化测试模板'+''.join(random.sample('abcdefghijk1234567890',5))


#driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)  # 隐性等待，最长等30秒
driver.get("https://yunoa.newtopgd.com/")
#driver.get("https://oa.newtopgd.com/")
sleep(2)


# 登录
driver.find_element_by_xpath('//*[@id="app"]/div/div/div/form/div[1]/div/div/input').clear()
#driver.find_element_by_xpath('//*[@id="app"]/div/div/div/form/div[1]/div/div/input').send_keys('广东新拓计算机科技有限公司')
driver.find_element_by_xpath('//*[@id="app"]/div/div/div/form/div[1]/div/div/input').send_keys('新拓')
driver.find_element_by_xpath('//*[@id="app"]/div/div/div/form/div[2]/div/div/input').send_keys('18575074750')
#driver.find_element_by_xpath('//*[@id="app"]/div/div/div/form/div[3]/div/div/input').send_keys('toab417517')
driver.find_element_by_xpath('//*[@id="app"]/div/div/div/form/div[3]/div/div/input').send_keys('12345678')
driver.find_element_by_xpath('//*[@id="app"]/div/div/div/form/button').click()


def login():
    global driver
    return driver

