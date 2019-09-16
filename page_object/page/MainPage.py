from selenium.webdriver.common.by import By
from page_object.page.BasePage import BasePage
from page_object.page.ProfilePage import ProfilePage
from page_object.page.SelectedPage import SelectedPage
from page_object.page.SearchPage import SearchPage


class MainPage(BasePage):
    #_profile_button=(By.ID,"user_profile_icon")
    _search_button=(By.ID,"tv_search")


    def gotoSelected(self):

        zixuan = (By.XPATH, "//*[@text='自选']")
        self.find(zixuan)  # self.driver.find_element(By.XPATH,"//*[@text='自选']")
        self.find(zixuan).click()
        return SelectedPage()

    def gotoSearch(self):

        self.find(self._search_button).click()
        return SearchPage()


    def gotoProfile(self):
        #self.find(MainPage._profile_button).click()
        self.loadStep("../data/MainPage.yaml","gotoProfile")  #使用yaml进行改造
        return ProfilePage()