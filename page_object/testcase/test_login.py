import pytest

from page_object.page.app import App


class TestLogin(object):

    @classmethod
    def setup_class(cls):
        cls.profilePage=App.main().gotoProfile()

    def setup_method(self):
        self.loginPage=self.profilePage.gotoLogin()


    @pytest.mark.parametrize("user,pw,msg",[
        ("1561998", "123qazws","手机号码"),
        ("15619981501", "0000000","密码错误")
    ])
    def test_login_password(self,user,pw,msg):
        self.loginPage.loginByPassword(user,pw)
        assert msg in self.loginPage.getErrorMsg()

    def teardown_method(self):
        self.loginPage.back()