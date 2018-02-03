# coding:utf-8

from page.loginpage import LoginPage,login_url
from page.homepage import HomePage,home_url
import unittest
from selenium import webdriver

class HomeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.logindriver = LoginPage(cls.driver)
        cls.homedriver = HomePage(cls.driver)

        # 先登录
        cls.driver.get(login_url)
        cls.logindriver.login()


    def test_click_bky(self):
        self.driver.get(home_url)
        self.homedriver.click_bky()   # 点首页的bky按钮
        # 判断结果
        result = self.homedriver.is_exists_img()
        print(result)
        # 断言
        self.assertTrue(result)



