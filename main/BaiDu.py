import untils.pyselenium as py
from selenium.webdriver.support.ui import WebDriverWait
from PIL import Image, ImageEnhance
import pytesseract
import cv2 as cv


class BaiDu(py.pyselenium):
    _screenImg = r'../img/screenImg.png'

    def login(self):
        self.clickElement('xpath', '//*[@id="hd"]/div/div[1]/p/a[2]')
        self.clickElement('name', 'username')
        self.sendKeys('name', 'username', 'sola_one')
        self.clickElement('name', 'password')
        self.sendKeys('name', 'password', 'q88555493')
        self.recognizeCode()

    def recognizeCode(self):
        driver = self._driver
        WebDriverWait(driver, 20, 0.5).until(lambda x: x.find_element_by_xpath( '//*[@id="vseccode_cSA"]/img'))
        driver.get_screenshot_as_file(self._screenImg)
        location = driver.find_element_by_xpath('//*[@id="vseccode_cSA"]/img').location
        size = driver.find_element_by_xpath('//*[@id="vseccode_cSA"]/img').size
        # 取图片的位置和宽高（暂用）
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        img = Image.open(self._screenImg).crop((left, top, right, bottom))
        img = img.convert('L')
        img = ImageEnhance.Contrast(img)
        img = img.enhance(2.0)
        img.save(self._screenImg)

        img = Image.open(self._screenImg)
        code = pytesseract.image_to_string(img)
        print(code)
        self.sendKeys('xpath', '//*[@id="seccodeverify_cSA"]', code)

    def getUrl(self, url):
        return super().getUrl(url)

    def recognize_text(self):
        gray=cv.cvtColor(self._screenImg,cv.COLOR_BGR2GRAY)


if __name__ == "__main__":
    nn = BaiDu()
    nn.maxWindow()
    nn.getUrl("http://bbs.3dmgame.com/")
    nn.login()
