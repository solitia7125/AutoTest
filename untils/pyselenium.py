from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


class pyselenium(object):
    def __init__(self, brower="Chrome"):
        if brower == "Chrome":
            driver = webdriver.Chrome()
        elif brower == "Firefox":
            driver = webdriver.Firefox()
        elif brower == "Edge":
            driver = webdriver.edge()
        else:
            print("不支持的游览器")
        self._driver = driver

    def getUrl(self, url):
        self._driver.get(url)

    def maxWindow(self):
        self._driver.maximize_window()

    def findElement(self, by, value):
        if by == "name":
            return self._driver.find_element_by_name(value)
        elif by == "id":
            return self._driver.find_element_by_id(value)
        elif by == "xpath":
            return self._driver.find_element_by_xpath(value)
        elif by == "classname":
            return self._driver.find_element_by_class_name(value)
        elif by == "link":
            return self._driver.find_element_by_link_text(value)
        elif by == "css":
            return self._driver.find_element_by_css_selector(value)
        else:
            return None

    def clickElement(self, by, value):
        try:
            WebDriverWait(self._driver, 20, 0.5).until(lambda x: self.findElement(by, value)).click()
        except Exception as e:
            print('Error:', e)

    def sendKeys(self, by, value, msg):
        try:
            WebDriverWait(self._driver, 20, 0.5).until(lambda x: self.findElement(by, value)).send_keys(msg)
        except Exception as e:
            print('Error:', e)

    def hover(self, by, value):
        try:
            element = self.findElement(by, value)
            ActionChains(self._driver).move_to_element(element).perform()
        except Exception as e:
            print('Error', e)

    def getTitle(self):
        return self._driver.title

    def quit(self):
        self._driver.quit()
