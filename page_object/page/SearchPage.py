from selenium.webdriver.common.by import By
from page_object.page.BasePage import BasePage
import time


class SearchPage(BasePage):

    _edit_locator=(By.CLASS_NAME,"android.widget.EditText")
    _searched_lab=(By.XPATH,"//*[contains(@resource-id,'name') and @text='招商银行']")

    def search(self, name):
        self.find(self._edit_locator).send_keys(name)
        self.find(self._searched_lab).click()
        time.sleep(2)
        return self  #为了进行链式调用，一直用.调用

    def addToSelected(self,text):
        follow_button = (By.XPATH, "//*[contains(@resource-id,'stockCode') and contains(@text,'%s')]"
                         % text + "/../../..//*[contains(@resource-id,'follow_btn')]")
        self.find(follow_button).click()
        return self

    def removeFromSelected(self,text):
        follow_button = (By.XPATH, "//*[contains(@resource-id,'stockCode') and contains(@text,'%s')]"
                         % text + "/../../..//*[contains(@resource-id,'followed_btn')]")
        self.find(follow_button).click()
        return self

    def isInSelected(self,text):
        folled_button=(By.XPATH,"//*[contains(@resource-id,'stockCode') and contains(@text,'%s')]"
                                 %text+"/../../..//*[contains(@resource-id,'follow')]")
        id=self.find(folled_button).get_attribute("resourceId")
        print(id)
        return "followed_btn" in id

    def cancel(self):
        self.findByText("取消").click()

    def searchByUser(self,key):
        pass

    def isFollowed(self):
        pass

