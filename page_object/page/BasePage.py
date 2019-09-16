from page_object.driver.Client import AndroidClient
from appium.webdriver.webelement import WebElement
from selenium.webdriver.common.by import By
import yaml
import re

class BasePage(object):

    element_black=[
        (By.XPATH,"ddd")
    ]

    def __init__(self):
        self.driver=self.getDriver()

    @classmethod
    def getDriver(cls):
        cls.driver=AndroidClient.driver
        return cls.driver  #没想通

    @classmethod
    def getClient(cls):
        return AndroidClient  # 没想通

    def find(self,kv)->WebElement:
        #todo:处理弹框
        return self.find(*kv)

    """
    def find(self,by,value):
        element:WebElement
        #加上重试机制
        for i in range(3):
            try:
                element=self.driver.find_element(by,value)
                return element
            except:

                #找到页面的最顶层元素进行点击

                #黑名单
                self.driver.page_source
                for e in BasePage.element_black:
                    elements=self.driver.find_elements(*e)
                    if(elements.__sizeof__()>0):
                        elements[0].click()
                    
                    #if(self.driver.page_source.matches(e)):
                        #self.driver.find_element(*e).click()
                   
    """

    def findByText(self,text)->WebElement:
        return self.find((By.XPATH,"//*[@text='%s']" %text))

    def loadStep(self,po_path,key,**kwargs):
        file=open(po_path,'r')
        po_data=yaml.load(file)
        po_method=po_data[key]
        po_elements=dict()
        if po_data.keys().__contains__("elements"):
            po_elements=po_data['elements']
        #po_element=yaml.load(open('xxx.yaml'))['element']
        for step in po_method:
            step:dict
            element_platform=dict()
            if step.keys().__contains__("element"):
                element_platform=po_elements[step['element']][AndroidClient.platform]
            else:
                element_platform={"by":step['by'],"locator":step['locator']}
            element=self.driver.find(by=element_platform['by'],value=element_platform['locator'])
            action=str(step['action']).lower()  #这里把action的值转化成了小写
            #todo:定位失败，多数是弹框，try catch后进入 一个弹框处理
            if action =="click":  #写上小写，yaml文件中也要写上小写
                element.click()
            elif action=="sendkeys":  #这里要写小写，ymal文件中也要写上小写
                text=str(step['text'])
                for k,v in kwargs.items():
                    text=text.replace("$%s" %k, v)
                    print("update text:%s "% (text))
                element.send_keys(text)
            else:
                print("UNKONW COMMAND %s" % step)