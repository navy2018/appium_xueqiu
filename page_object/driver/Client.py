from appium import webdriver
from appium.webdriver.webdriver import WebDriver
import yaml

class AndroidClient(object):

    driver:WebDriver
    platform="android"
    @classmethod
    def installApp(cls)->WebDriver:
        # caps = {}
        # # caps['app']='app存放的位置'    #安装app
        # caps["platformName"] = "android"
        # caps["deviceName"] = "hogwarts"
        # caps["appPackage"] = "com.xueqiu.android"
        # caps["appActivity"] = ".view.WelcomeActivityAlias"
        # caps["autoGrantPermissions"] = "true"  # 自动授权
        # # caps["noReset"] = True

        # cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # cls.driver.implicitly_wait(20)  # 隐式等待
        # return cls.driver
        return cls.initDriver("install_app")


    @classmethod
    def restartApp(cls)->WebDriver:
        # caps = {}
        # caps["platformName"] = "android"
        # caps["deviceName"] = "hogwarts"
        # caps["appPackage"] = "com.xueqiu.android"
        # caps["appActivity"] = ".view.WelcomeActivityAlias"
        # # caps["autoGrantPermissions"] = "true"  # 启动的时候将，noReset设置成True就不需要这一句代码自动授权
        # caps["noReset"] = True
        # caps["unicodeKeyboard"]=True
        # caps["resetKeyboard"]=True
        #
        # cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # cls.driver.implicitly_wait(20)  # 隐式等待
        # return cls.driver
        return cls.initDriver("restart_app")

    @classmethod
    def initDriver(cls,key):
        driver_data=yaml.load(open("../data/driver.yaml"))
        server=driver_data[key]['server']
        implicitly_wait=driver_data[key]['implicitly_wait']
        platform=str(driver_data['platform'])
        cls.platform=platform
        caps = driver_data[key]['caps'][platform]
        cls.driver=webdriver.Remote(server,caps)
        cls.driver.implicitly_wait(implicitly_wait)
        return cls.driver
