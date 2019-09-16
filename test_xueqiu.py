# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
import time

class TestXueqiuAndroid(object):


    @classmethod
    def setup_class(cls):
        print("class setup")


    def setup_method(self):
        print("method setup")
        self.driver=self.restart_app()  #下面的driver来自动这里



    def test_login(self):
        el1=self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        el1.click()

        el3=self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el3.send_keys("alibaba")


    def test_jijin(self):
        """
        el1=self.driver.find_element_by_xpath("//*[contains(@resource-id,'buttons_container')]//*[@text='基金']")
        el1.click()
        """
        el2=self.driver.find_element_by_xpath("//*[contains(@resource-id,'indicator')]//*[@text='基金']")
        el2.click()



    #三种滑动屏幕的方法

    def test_swipe(self):
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'buttons_container')]//*[@text='基金']")
        for i in range(5):
            self.driver.swipe(800,800,200,200)
            time.sleep(2)

    def test_action(self):
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'buttons_container')]//*[@text='基金']")
        action=TouchAction(self.driver)
        for i in range(5):
            action.press(x=800,y=800).move_to(x=200,y=200).release().perform()
            time.sleep(2)

    def test_action_p(self):
        rect=self.driver.get_window_rect()
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'buttons_container')]//*[@text='基金']")
        action=TouchAction(self.driver)
        for i in range(5):
            action.press(x=rect['width']*0.8,y=rect['height']*0.8).move_to(x=rect['width']*0.2,y=rect['height']*0.2).release().perform()
            time.sleep(2)
            self.driver.get_screenshot_as_file(str(i)+".png")



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

    #不加这段teardown的代码也没关系，如果不quit(),启动appium会自动quit之前的session,一次自动化执行
    def teardown_method(self):
        self.driver.quit()




