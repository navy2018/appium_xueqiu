import pytest
from page_object.page.MainPage import MainPage
from page_object.page.app import App


class TestSelected(object):

    mainPage:MainPage
    @classmethod
    def setup_class(cls):
        cls.mainPage=App.main()   #进入首页

    def setup_method(self):
        self.mainPage=TestSelected.mainPage
        self.searchPage=self.mainPage.gotoSearch()



    def test_selected_stock(self):
        self.searchPage.search('alibaba')
        assert self.searchPage.isInSelected("BABA")==True
        assert self.searchPage.isInSelected("1688")==False

    #数据驱动
    @pytest.mark.parametrize("key,code",[("招商银行","SH600036"),
                                         ("平安银行","SZ000001"),
                                         ("pingan","SH601318")
                                         ])
    def test_is_selected_stock_hs(self,key,code):
        searchPage=self.searchPage.search(key)
        assert searchPage.isInSelected(code)==False

    def teardown_method(self):
        self.searchPage.cancel()


    def test_add_stock_hs(self):
        key="招商银行"
        code="SH600036"
        searchPage=self.searchPage.search(key)
        if searchPage.isInSelected(code)==True:
            searchPage.removeFromSelected(code)

        searchPage.addToSelected(code)
        assert searchPage.isInSelected(code)==True


    def test_is_follow_user(self):
        pass