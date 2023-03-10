import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from venv.basic.find_element import FindElement

s = Service(executable_path=r'c:\Program Files\Google\Chrome\Application\chromedriver.exe')


class RegeisterKeyword(object):
    def __init__(self, brower):
        self.fe = FindElement(brower)

    # 打开浏览器
    def open_brower(self,brower):
        if brower == 'chrome':
            self.driver = webdriver.Chrome(service=s)
        elif brower == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()


    # 输入测试地址
    def get_url(self, url):
        self.driver.get(url)

    # 定位元素
    def get_element(self, key):
        return self.fe.get_element(key)

    # 输入元素
    def send_element_key(self, key, value):
        get_element = self.get_element(key)
        get_element.send_key(value)

    # 点击元素
    def click_element(self, key):
        self.fe.get_element(key).click()

    # 页面等待
    @staticmethod
    def wait_loading():
        time.sleep(2)

    # 关闭浏览器
    def close_brower(self):
        self.driver.close()


if __name__ == "__main__":
    register_url = 'http://www.5itest.cn/register'
    driver = webdriver.Chrome(service=s)
    driver.get(register_url)
    rk = RegeisterKeyword(driver)
    print(rk.get_element('register_email'))
    driver.close()
