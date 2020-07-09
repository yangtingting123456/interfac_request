#读取excel为各种类型：列表，类
import os
import xlrd
from  pritices_daily import case_infos
def read_excel_data_convert_info_01(excel_path):
    # 1,读取数据存到列表中：[[用例编号，用例名称，所在模块...],[....],[......]]
    workbook = xlrd.open_workbook(excel_path)  # 打开工作簿
    sheet = workbook.sheet_by_index(0)  # 打开第一个表
    all_case_info1 = []
    for i in range(1, sheet.nrows):
        case_info = []
        for j in range(0, sheet.ncols):
            case_info.append(sheet.cell_value(i, j))
        all_case_info1.append(case_info)
    return all_case_info1

#2,做成类形成
def read_excel_data_convert_info_02(excel_path):
    workbook = xlrd.open_workbook(excel_path)  # 打开工作簿
    sheet = workbook.sheet_by_index(0)  # 打开第一个表
    all_case_info2 = []
    for i in range(1, sheet.nrows):
        case_id = sheet.cell_value(i, 0)
        case_name = sheet.cell_value(i, 1)
        case_module = sheet.cell_value(i, 2)
        case_pri = sheet.cell_value(i, 3)
        case_step = sheet.cell_value(i, 4)
        case_result = sheet.cell_value(i, 5)
        CaseInfo = case_infos.CaseInfo(case_id, case_name, case_module, case_pri, case_step, case_result)
        all_case_info2.append(CaseInfo)
    return all_case_info2[0].case_name

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '../data/testcases.xlsx')
print(read_excel_data_convert_info_01(excel_path))
print(read_excel_data_convert_info_02(excel_path))