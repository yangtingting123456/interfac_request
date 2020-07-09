from selenium import webdriver
import os,time
import datetime as dt

#编写tapd提交bug登录的脚本
#1.通过id定位元素
current_path=os.path.dirname(__file__)
print(current_path)
wbdriver_path=os.path.join(current_path,'../webdriver/chromedriver.exe')
print(wbdriver_path)
driver=webdriver.Chrome(executable_path=wbdriver_path)   #加载驱动
driver.get('https://www.baidu.com/')      #打开登录地址
driver.maximize_window()   #窗口最大化
driver.implicitly_wait(30)   #隐性等待30分钟
driver.find_element_by_id('kw').send_keys('高考加油')   #输入搜索词
driver.find_element_by_id('su').click()   #点击搜索按钮
time.sleep(3)
#返回上一页
driver.back()
time.sleep(3)
#刷新
driver.refresh()
time.sleep(3)
#往前一页
driver.forward()
time.sleep(3)
current_data=dt.datetime.now().strftime('%Y-%m-%d-%H_%M_%S')
print(current_data)
os.chdir('../error-img')
driver.get_screenshot_as_file(current_data+'.png')  #截图
current_url01=driver.current_url
print(current_url01)
p_source=driver.page_source
print(p_source)
web_title=driver.title
print(web_title)
driver.quit()     #关闭浏览器
