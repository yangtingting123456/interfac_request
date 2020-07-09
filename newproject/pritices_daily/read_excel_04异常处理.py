#异常处理
#1.让try的方位更广
#读取excel为各种类型：列表，类
import os
import xlrd
from  pritices_daily import case_infos
from  pritices_daily import config_utils
def read_excel_data_convert_info_01(excel_path):
    # 1,读取数据存到列表中：[[用例编号，用例名称，所在模块...],[....],[......]]
    try:
        workbook = xlrd.open_workbook(excel_path)  # 打开工作簿
        sheet = workbook.sheet_by_index(0)  # 打开第一个表
        all_case_info1 = []
        for i in range(1, sheet.nrows):
            case_info = []
            for j in range(0, sheet.ncols):
                case_info.append(sheet.cell_value(i, j))
            all_case_info1.append(case_info)
    except Exception as e:
        print('系统错误')
    return all_case_info1



# current_path = os.path.dirname(__file__)
# excel_path = os.path.join(current_path, '../111data/testcases.xlsx')
# print(read_excel_data_convert_info_01(excel_path))

#2.看业务要求怎么定
import os
import xlrd
from  pritices_daily import case_infos
def read_excel_data_convert_info_01(excel_path):
    # 1,读取数据存到列表中：[[用例编号，用例名称，所在模块...],[....],[......]]
    try:
        workbook = xlrd.open_workbook(excel_path)
    except FileNotFoundError as e:   #文件路径错误再给一个默认的路径
         current_path = os.path.dirname(__file__)
         excel_path = os.path.join(current_path, '../data/testcases.xlsx')
         workbook = xlrd.open_workbook(excel_path)  # 打开工作簿
    sheet = workbook.sheet_by_index(0)  # 打开第一个表
    all_case_info1 = []
    for i in range(1, sheet.nrows):
        case_info = []
        for j in range(0, sheet.ncols):
            case_info.append(sheet.cell_value(i, j))
            all_case_info1.append(case_info)
    return all_case_info1

current_path = os.path.dirname(__file__)
conf_test = config_utils.ConfigUtils()
expath= conf_test.read_ini
print(expath)
excel_path = os.path.join(current_path, expath)
print(read_excel_data_convert_info_01(excel_path))

