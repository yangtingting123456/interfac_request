import os
import xlrd
from ReadExcel import readexcelbase
#读取excel，将作为对象存储
current_path=os.path.dirname(__file__)        #获取当前工作路径的工作路径
excel_path=os.path.join(current_path,'..//data//userinfo.xlsx')   #获取用户信息excel的路径
workbook=xlrd.open_workbook(excel_path)       #打开一个工作簿
sheet=workbook.sheet_by_index(0)              #打开第一个工作表
sheet01=sheet.cell_value(1,0)                 #读取某个工作表某一个表的内容
row_count=sheet.nrows                         #获取sheet01总共有多少行
cell_count=sheet.ncols
userinfo=[]
for i in range(1,row_count):
    user_name = sheet.cell_value(i, 0)
    user_realname = sheet.cell_value(i, 1)
    sex = sheet.cell_value(i, 2)
    age = sheet.cell_value(i, 3)
    occupation = sheet.cell_value(i, 4)
    salary = sheet.cell_value(i, 5)
    case_info=readexcelbase.read_excel(user_name,user_realname,sex,age,occupation,salary)
    userinfo.append(case_info)
print(userinfo[0].user_realname)

from selenium import webdriver
import os
current_path=os.path.dirname(__file__)
print(current_path)
wbdriver_path=os.path.join(current_path,'../webdriver/chromedriver.exe')
print(wbdriver_path)
driver=webdriver.Firefox(executable_path=wbdriver_path)
driver.get('https://www.baidu.com')