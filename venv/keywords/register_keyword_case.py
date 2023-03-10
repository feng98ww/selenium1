from read_excel import ReadExcel
from register_keyword import RegeisterKeyword
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(executable_path=r'c:\Program Files\Google\Chrome\Application\chromedriver.exe')


class RegisterKeywordCase(object):
    def __init__(self, brower):
        self.rk = RegeisterKeyword(brower)
        self.excel_path = 'data/test.xls'

    # 执行关键字测试方法
    def run_keyword_method(self, keyword_method, operator_element='', send_value=''):
        print('keyword_method --->', keyword_method)
        print("operaator_element -->", send_value)
        print("send_value --->", send_value)
        execute_method = getattr(self.rk, keyword_method)
        print(execute_method)
        if operator_element == '' and send_value != '':
            result = execute_method(send_value)
        elif operator_element != '' and send_value == '':
            result = execute_method(operator_element)
        elif operator_element == '' and send_value == '':
            result = execute_method(operator_element, send_value)
        else:
            result = execute_method(operator_element, send_value)
        return result

    # 执行关键词测试用例
    def run_keyword_excel_cases(self):
        handle_excel = ReadExcel(self.excel_path)
        # 获取excel 关键词测试用例条数
        cases_numbers = handle_excel.get_lines()
        print("注册页获取到的关键词的测试用例条数为： %s" % cases_numbers)
        # 循环遍历测试用例
        if cases_numbers:
            # 第0行是标题作为用例不执行
            for i in range(1, cases_numbers):
                # 获取测试用例名称
                testcase_name = handle_excel.get_cell(i, 0)
                # 获取用例是否执行
                is_run = handle_excel.get_cell(i, 1)
                if is_run == 'yes':
                    keyword_method = handle_excel.get_cell(i, 2)
                    operator_element = handle_excel.get_cell(i, 3)
                    send_value = handle_excel.get_cell(i, 4)
                    except_result = handle_excel.get_cell(i, 5)
                    actual_result = handle_excel.get_cell(i, 6)

                    # 反射
                    self.run_keyword_method(keyword_method, operator_element, send_value)
                    # if except_result is not '':
                    #     except_value = self.run_keyword_method(keyword_method)
                else:
                    print('第 %s 条用例不执行，用例名称是： [%s], 无预期结果' % (i, testcase_name))
        else:
            print("请检查是否有写测试用例")


if __name__ == "__main__":
    brower = webdriver.Chrome(service=s)
    rkc = RegisterKeywordCase(brower)
    rkc.run_keyword_method('open_brower', '', 'chrome')
    rkc.run_keyword_method('get_url', '', 'http://www.5itest.cn/register')
    rkc.run_keyword_excel_cases()
