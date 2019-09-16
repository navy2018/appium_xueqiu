from selenium.webdriver.common.by import By
from page_object.page.BasePage import BasePage
from page_object.page.LoginPage import LoginPage


class ProfilePage(BasePage):


    #_phone_login = (By.ID, "iv_login_phone")

    def gotoLogin(self):
        #self.find(self._phone_login).click()
        self.loadStep("../data/ProfilePage.yaml","gotoLogin")
        return LoginPage()