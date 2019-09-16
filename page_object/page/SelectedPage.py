from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy  #是对By的补充，只能使用在app中
from page_object.page.BasePage import BasePage


class SelectedPage(BasePage):

    def addDefault(self):
        return self

    def gotoHS(self):
        self.findByText("沪深").click()
        return self

    def getPriceByName(self,name):
        priceLocator=(By.XPATH,"//*[contains(@resource-id,'portfolio_stockName') and @text='%s']" %name+
                               "/../../../..//*[contains(@resource-id,'item_layout')]")
        price=self.find(priceLocator).text
        return float(price)