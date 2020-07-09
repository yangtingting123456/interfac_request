# 1. Python webdriver环境搭建  步骤+截图，自己收集、整理好相关资料
# 步骤1，按照python；
# 步骤2：按照pycharm
# 步骤3;下载浏览器器对应的驱动
# 步骤4：下载selenium包，有两种方式，方式1，通过pip  install selenium 安装；  方式2，通过pycharm中的file->setting
# ->project:newproject->project Interpreter->点击+搜索selenium，点击instll进行安装；
# 步骤5，导入selenium包，开始编写自动化脚本；

# 2. 完成元素识别老师上课讲的练习
# 1，元素识别练习1
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


# 3. 把第二章 元素识别整理成xmind上交



# 4. 编写禅道登录脚本，分别是使用id、name等普通方案、xpath、css方法编写脚本
from selenium import webdriver
import os

#编写tapd提交bug登录的脚本
#1.通过id定位元素
current_path=os.path.dirname(__file__)
print(current_path)
wbdriver_path=os.path.join(current_path,'../webdriver/chromedriver.exe')
print(wbdriver_path)
driver=webdriver.Chrome(executable_path=wbdriver_path)   #加载驱动
driver.get('https://www.tapd.cn/cloud_logins/login')      #打开登录地址
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element_by_id('username').send_keys('tingting.yang@juneyaokc.com')   #输入用户名
driver.find_element_by_id('password_input').send_keys('ytt123456..')   #输入密码
driver.find_element_by_id('tcloud_login_button').click()        #点击登录按钮
driver.quit()     #关闭浏览器

from selenium import webdriver
import os

#编写tapd提交bug登录的脚本
#1.通过name定位元素
current_path=os.path.dirname(__file__)
print(current_path)
wbdriver_path=os.path.join(current_path,'../webdriver/chromedriver.exe')
print(wbdriver_path)
driver=webdriver.Chrome(executable_path=wbdriver_path)   #加载驱动
driver.get('https://www.tapd.cn/cloud_logins/login')      #打开登录地址
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element_by_name('data[Login][email]').send_keys('tingting.yang@juneyaokc.com')   #输入用户名
driver.find_element_by_name('data[Login][password]').send_keys('ytt123456..')   #输入密码
driver.find_element_by_id('tcloud_login_button').click()        #点击登录按钮
driver.quit()     #关闭浏览器

from selenium import webdriver
import os

#编写tapd提交bug登录的脚本
#3.通过xpass定位元素
current_path=os.path.dirname(__file__)
print(current_path)
wbdriver_path=os.path.join(current_path,'../webdriver/chromedriver.exe')
print(wbdriver_path)
driver=webdriver.Chrome(executable_path=wbdriver_path)   #加载驱动
driver.get('https://www.tapd.cn/cloud_logins/login')      #打开登录地址
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element_by_xpath('/html/body/div/form/div[2]/div/input').send_keys('tingting.yang@juneyaokc.com')   #输入用户名
driver.find_element_by_xpath('/html/body/div/form/div[3]/div/input').send_keys('ytt123456..')   #输入密码
driver.find_element_by_xpath('/html/body/div/form/div[4]/input').click()        #点击登录按钮
driver.quit()     #关闭浏览器

#编写tapd提交bug登录的脚本
#4.通过css定位元素
current_path=os.path.dirname(__file__)
print(current_path)
wbdriver_path=os.path.join(current_path,'../webdriver/chromedriver.exe')
print(wbdriver_path)
driver=webdriver.Chrome(executable_path=wbdriver_path)   #加载驱动
driver.get('https://www.tapd.cn/cloud_logins/login')      #打开登录地址
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element_by_css_selector('input#username').send_keys('tingting.yang@juneyaokc.com')   #输入用户名
driver.find_element_by_css_selector('input#password_input').send_keys('ytt123456..')   #输入密码
driver.find_element_by_css_selector('input#tcloud_login_button').click()        #点击登录按钮
driver.quit()     #关闭浏览器



