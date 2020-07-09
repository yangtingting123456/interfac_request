import os
import xlrd
#获取excel的路径
current_path=os.path.dirname(__file__)
print(current_path)
excel_path=os.path.join(current_path,'../data/studentinfo.xlsx')
print(excel_path)
#打开工作簿
workbook = xlrd.open_workbook(excel_path)
#打开第一个表
sheet01=workbook.sheet_by_index(0)
nrow=sheet01.nrows
nclow=sheet01.ncols
print(nrow)
print(nclow)
#读取第一张表的内容
print(sheet01.cell_value(3,1))
