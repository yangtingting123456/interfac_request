import os
import xlrd
#读取excel中的内容，将内容放到列表中打印出来
current_path=os.path.dirname(__file__)        #获取当前工作路径的工作路径
excel_path=os.path.join(current_path,'..//data//userinfo.xlsx')   #获取用户信息excel的路径
workbook=xlrd.open_workbook(excel_path)       #打开一个工作簿
sheet=workbook.sheet_by_index(0)              #打开第一个工作表
sheet01=sheet.cell_value(1,0)                 #读取某个工作表某一个表的内容
row_count=sheet.nrows                         #获取sheet01总共有多少行
cell_count=sheet.ncols
userinfo=[]   #定义一个列表
for i in range(1,row_count):
    for j in range(0,cell_count):
        sheet_value=sheet.cell_value(i,j)
        userinfo.append(sheet_value)
print(userinfo)

