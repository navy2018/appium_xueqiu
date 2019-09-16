import pytest
from page_object.page.MainPage import MainPage
from page_object.page.app import App


class TestSelected(object):

    mainPage:MainPage
    @classmethod
    def setup_class(cls):
        cls.mainPage=App.main()   #进入首页


    def test_price(self):
        assert self.mainPage.gotoSelected().gotoHS().getPriceByName("恒瑞医药")==78.88