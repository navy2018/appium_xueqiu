from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
import time

class TestXueqiuLogin(object):
    driver:WebDriver

    @classmethod
    def setup_class(cls):
        print("class setup")
        cls.driver=cls.install_app()
        #进入登陆页面
        logbutn = cls.driver.find_element_by_id("user_profile_icon")
        logbutn.click()


    def setup_method(self):
        print("method setup")
        self.driver=TestXueqiuLogin.driver  #下面的driver来自动这里
        #进入手机登陆页面
        phonelog = self.driver.find_element_by_id("iv_login_phone")
        phonelog.click()



    def test_login_phone(self):

        username=self.driver.find_element_by_id("register_phone_number")
        username.send_keys("15618871501")
        regcode=self.driver.find_element_by_id("register_code")
        regcode.send_keys("3456")
        loginbtn=self.driver.find_element_by_id("button_next")  #两个页面一样的
        loginbtn.click()
        errorsure = self.driver.find_element_by_id("md_buttonDefaultPositive")
        if errorsure.is_displayed():
            errorsure.click()
            print("发生报错")



    def test_login_acc(self):
        emaiphonelog = self.driver.find_element_by_xpath("//*[@text='邮箱手机号密码登录']")
        emaiphonelog.click()
        acc = self.driver.find_element_by_id("login_account")
        acc.send_keys("luweiwon@163.com")
        password = self.driver.find_element_by_id("login_password")
        password.send_keys("654321")
        loginbtn = self.driver.find_element_by_id("button_next")  # 两个页面一样的
        loginbtn.click()
        errorsure = self.driver.find_element_by_id("md_buttonDefaultPositive")
        if errorsure.is_displayed():
            errorsure.click()
            print("发生报错")



    @classmethod
    def install_app(cls)-> WebDriver:
        caps = {}
        #caps['app']='app存放的位置'    #安装app
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"  # 自动授权
        #caps["noReset"] = True

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(20)  # 隐式等待
        return driver


    @classmethod
    def restart_app(cls) -> WebDriver:
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        #caps["autoGrantPermissions"] = "true"  # 启动的时候将，noReset设置成True就不需要这一句代码自动授权
        caps["noReset"] = True

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(20)  # 隐式等待
        return driver



    #不加这段teardown的代码也没关系，如果不quit(),启动appium会自动quit之前的session
    def teardown_method(self):
        self.driver.back()