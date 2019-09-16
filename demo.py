# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "hogwarts"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["autoGrantPermissions"] = "true"   #自动授权


driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)  #隐式等待

el1=driver.find_element_by_id("com.xueqiu.android:id/home_search")
el1.click()

el3=driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el3.send_keys("alibaba")


"""
el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ImageView")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/iv_login_phone")
el2.click()

"""
driver.quit()