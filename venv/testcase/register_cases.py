import time
from venv.log import Logger
from venv.business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
from selenium.webdriver.chrome.service import Service
import ddt

logger = Logger(logger='RegisterTestcase').getlog()

s = Service(executable_path=r'c:\Program Files\Google\Chrome\Application\chromedriver.exe')


@ddt.ddt
class RegisterTestcase(unittest.TestCase):
    driver = webdriver.Chrome(service=s)

    @classmethod
    def setUpClass(cls) -> None:
        cls.register_url = 'http://www.5itest.cn/register'

        cls.driver.get(cls.register_url)

        cls.driver.maximize_window()
        cls.rb = RegisterBusiness(cls.driver)
        cls.driver.set_page_load_timeout(5)
        logger.info("打开浏览器，窗口最大化")

        cls.start = time.time()

    @classmethod
    def tearDownClass(cls) -> None:

        cls.driver.close()

    # @ddt.data(
    #     # 顺序分别是：注册邮箱、用户昵称、注册密码、验证码、错误信息定位元素、错误提示信息
    #     ['123', 'test01', 'test01abc', 'type'],
    #     ['@163.com', 'test01', 'test10abc', 'tyu9'],
    #     # ['@163', 'test01', 'test01abc', 'tyu9']
    # )
    # @ddt.unpack
    # def test_ddt_email_error(self, register_email, nickname, password, captcha):
    #     register_email_error = self.rb.register_email_error(register_email, nickname, password, captcha)
    #
    #
    #     print("register_email_error:", register_email_error)
    #
    #
    #     self.assertFalse(register_email_error, '你输入的邮箱错误，但此条测试用例执行成功')
    # 邮箱错误测试的测试用例

    # 注册邮箱错误，但用例执行成功
    def test_register_email_error(self):
        register_email_error = self.rb.register_email_error('23', 'test01', 'test01abc', 'abc4')
        if register_email_error is True:
            print("账号注册失败，该用例执行成功")
        else:
            print("账号注册成功，该用例执行失败")
        logger.info("注册邮箱错误，但用例执行成功")

    # # 验证码错误，但用例执行成功‘
    # def test_captcha_code_error(self):
    #     captcha_code_error = self.rb.captcha_code_error('test02@163.com', 'test02', 'test02abc', 'height')
    #     if captcha_code_error is True:
    #         print("账号注册失败，该用例执行成功")
    #     else:
    #         print("账号注册成功，该用例执行失败")
    #     logger.info("验证码错误，但用例执行成功")


#
testlog = RegisterTestcase()
testlog.setUpClass()
# testlog.test_ddt_email_error()
testlog.test_register_email_error()
# testlog.test_captcha_code_error()

if __name__ == "__main__":
    unittest.main()
