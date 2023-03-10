from venv.handle.register_handle import RegisterHandle
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
s = Service(executable_path=r'c:\Program Files\Google\Chrome\Application\chromedriver.exe')


class RegisterBusiness(object):
    def __init__(self, brower):
        self.rh = RegisterHandle(brower)

    # 正常注册
    def common_register(self, register_email, nickname, password, captcha):
        self.rh.send_register_email(register_email)
        self.rh.send_register_nickname(nickname)
        self.rh.send_register_password(password)
        self.rh.send_register_captcha(captcha)

    # 判断是否注册成功
    def success_or_fail(self):
        if self.rh.get_register_btn_text() is None:
            return True
        else:
            return False

    # 邮箱错误
    def register_email_error(self, register_email, nickname, password, captcha):
        self.common_register(register_email, nickname, password, captcha)
        if self.rh.get_user_text('register_email_error', "请输入有效的电子邮件地址") is None:
            print("注册邮箱输入错误")
            return True
        else:
            return False

    # 用户昵称错误
    def register_nickname_error(self, register_email, nickname, password, captcha):
        self.common_register(register_email, nickname, password, captcha)
        if self.rh.get_user_text('register_nickname_error', "字符长度必须大于等于4，一个中文字算2个字符") is None:
            print("用户昵称错误")
            return True
        else:
            return False

    # 用户密码错误
    def register_password_error(self, register_email, nickname, password, captcha):
        self.common_register(register_email, nickname, password, captcha)
        if self.rh.get_user_text('register_password_error', "最少需要输入 5 个字符") is None:
            print("用户密码错误")
            return True
        else:
            return False

    # 验证码错误
    def captcha_code_error(self, register_email, nickname, password, captcha):
        self.common_register(register_email, nickname, password, captcha)
        if self.rh.get_user_text('captcha_code_error', "验证码错误") is None:
            print("验证码错误")
            return True
        else:
            return False


if __name__ == "__main__":
    register_url = 'http://www.5itest.cn/register'
    driver = webdriver.Chrome(service=s)
    driver.get(register_url)
    rb = RegisterBusiness(driver)
    rb.captcha_code_error('1243589@163.com', 'pass123', 'test@123', 'sds')

    sleep(3)
    driver.close()
