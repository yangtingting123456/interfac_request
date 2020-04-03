from selenium import webdriver
import time
import unittest
#加载浏览器的驱动
driver=webdriver.Chrome()
#打开网站首页
driver.get('http://www.sogou.com')
#定位到搜索输入框并清空
driver.find_element_by_id('query').clear()
#输入搜索内容
driver.find_element_by_id('query').send_keys('开始了自动化的光荣测试之路')
#点击搜索按钮
driver.find_element_by_id('stb').click()
#强制等待3秒
time.sleep(30)
#关闭浏览器
driver.quit()

