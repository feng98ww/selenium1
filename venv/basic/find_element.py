from venv.read.read_ini import ReadIni
from selenium.webdriver.common.by import By


class FindElement(object):
    def __init__(self, driver):
        self.driver = driver

    #     def get_element(self, by=By.ID, value=None) -> WebElement:
    #
    #
    #
    #         """
    #         Find an element given a By strategy and locator.
    #
    #         :Usage:
    #             ::
    #
    #                 element = driver.find_element(By.ID, 'foo')
    #
    #         :rtype: WebElement
    #         """
    #         if by == By.ID:
    #             by = By.CSS_SELECTOR
    #             value = '[id="%s"]' % value
    #         elif by == By.TAG_NAME:
    #             by = By.CSS_SELECTOR
    #         elif by == By.CLASS_NAME:
    #             by = By.CSS_SELECTOR
    #             value = ".%s" % value
    #         elif by == By.NAME:
    #             by = By.CSS_SELECTOR
    #             value = '[name="%s"]' % value
    #
    #         return self.execute(Command.FIND_ELEMENT, {
    #             'using': by,
    #             'value': value})['value']
    # #
    def get_element(self, key):

        ri = ReadIni()
        data = ri.get_value(key=key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:

            if by == By.ID:
                return self.driver.find_element(By.ID, value)
            elif by == By.NAME:
                return self.driver.find_element(By.NAME, value)
            elif by == By.CLASS_NAME:
                return self.driver.find_element(By.CLASS_NAME, value)
            else:
                return self.driver.find_element(By.XPATH, value)



        except:
            file_path = '../image/no_element.png'
            self.driver.save_screenshot(file_path)


if __name__ == "__main__":
    fe = FindElement()
    fe.get_element('register_nickname')
