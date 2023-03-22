from HTMLTestRunner import HTMLTestRunner
from venv.testcase.register_cases import RegisterTestcase
import unittest


class UseHtml:
    def testmethod(self):
        suite = unittest.TestSuite()
        lists = ["test_register_email_error", "test_captcha_code_error"]
        for list_i in lists:
            suite.addTest(RegisterTestcase(list_i))
        with open("../../venv/report/report.html", "wb") as f:
            HTMLTestRunner(
                stream=f,
                title="单元测试",
                description="测试一期",
                verbosity=2
            ).run(suite)


uh = UseHtml()
uh.testmethod()
