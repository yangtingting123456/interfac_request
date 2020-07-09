#类封装
import os
import xlrd
from  pritices_daily import case_infos
from  pritices_daily.config_utils import conf_test
from pritices_daily.log_util import log_info
class ReadExcel:
    def __init__(self,excel_path):
        self.excel_path=excel_path

    def read_excel_data_convert_info_01(self):
        # 1,读取数据存到列表中：[[用例编号，用例名称，所在模块...],[....],[......]]
        workbook = xlrd.open_workbook(self.excel_path)  # 打开工作簿
        try:
            log_info.info('打开工作簿')
            sheet = workbook.sheet_by_index(0)  # 打开第一个表
            log_info.info('打开第一个工作表')
            all_case_info1 = []
            for i in range(1, sheet.nrows):
                case_info = []
                for j in range(0, sheet.ncols):
                    case_info.append(sheet.cell_value(i, j))
                all_case_info1.append(case_info)
        except Exception as e:
            log_info.error('系统错误')
        return all_case_info1

    # 2,做成类形成
    def read_excel_data_convert_info_02(self):
        workbook = xlrd.open_workbook(self.excel_path)  # 打开工作簿
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

if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    expath = conf_test.read_ini
    excel_path = os.path.join(current_path, conf_test.read_ini)
    rd01=ReadExcel(excel_path)
    print(rd01.read_excel_data_convert_info_01())
    print(rd01.read_excel_data_convert_info_02())