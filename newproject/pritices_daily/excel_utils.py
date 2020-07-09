#操作excel的工具包，将excel中的数据存储到列表中
import os
import xlrd
from pritices_daily import student_base_info

#--1.将excel中的数据存储到列表中
#----第一种方式，一个个获取---
#----第二种方式，通过循环获取---
#----第三种方式，通过循环获取---
def read_excel_get_stu_info(excel_path):
    workbook = xlrd.open_workbook(excel_path)  # 打开工作簿
    sheet01 = workbook.sheet_by_index(0)  # 打开第一个表
    nrow = sheet01.nrows
    student_infos=[]
    for i in range(1, nrow):
        studnt01 = student_base_info.StudentBaseInfo(sheet01.cell_value(i, 0),
                                                     sheet01.cell_value(i, 1),
                                                     sheet01.cell_value(i, 2),
                                                     sheet01.cell_value(i, 3),
                                                     sheet01.cell_value(i, 4))
        student_infos.append(studnt01)
        return  student_infos[0].stuName
    # 获取excel的路径

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '../data/studentinfo.xlsx')
print(read_excel_get_stu_info(excel_path))




