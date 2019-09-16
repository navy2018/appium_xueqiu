from selenium.webdriver.common.by import By
from page_object.page.BasePage import BasePage


class LoginPage(BasePage):
    _back_locator=(By.ID,"iv_action_back")
    _phone_login=(By.ID,"iv_login_phone")
    _wx_login=(By.ID,"iv_login_wx")
    _weibo_login=(By.ID,"iv_login_weibo")
    _qq_login=(By.ID,"iv_login_qq")
    _other_login=(By.ID,"login_more")
    _register_phone_number=(By.ID,"register_phone_number")
    _register_code=(By.ID,"register_code")
    _button_next=(By.ID,"button_next")
    _tv_login_with_account=(By.ID,"tv_login_with_account")
    _login_account=(By.ID,"login_account")
    _login_password=(By.ID,"login_password")
    _error_msg=(By.ID,"md_content")

    def loginByWX(self):
        return self

    def loginByMSG(self,phone,code):
        return self

    def loginByPassword(self, account, password):

        self.loadStep("../data/LoginPage.yaml","loginByPassword",var1=account,var2=password)
        return self


    def loginSuccessByPassword(self,account,password):
        from page_object.page.MainPage import MainPage  #为什么会这样？
        return MainPage()

    def back(self):
        self.find(self._back_locator).click()
        from page_object.page.ProfilePage import ProfilePage  #为什么会这样？
        return ProfilePage()

    def getErrorMsg(self):
        msg= self.find(self._error_msg).text
        self.findByText("确定").click()

        return msg