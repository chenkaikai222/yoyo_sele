# coding:utf-8
from selenium import webdriver
import unittest
from page.loginpage import LoginPage,login_url
class TestLogin(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.logindriver = LoginPage(self.driver)
        self.driver.get(login_url)

    def test_login(self):
        # 1输入账号
        self.logindriver.input_username("1111")
        # 2输入密码
        self.logindriver.input_psw("111")
        # 3点登录按钮
        self.logindriver.click_login_button()
        # 4获取登录结果
        result = self.logindriver.is_login_sucess()
        # 5断言
        self.assertTrue(result)


