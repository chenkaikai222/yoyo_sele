# coding:utf-8
from common.base import BasePage

login_url = "https://passport.cnblogs.com/user/signin"

class LoginPage(BasePage):

    usename_loc = ("id", "input1")
    psw_loc = ("id", "input2")
    button_loc = ("id", "signin")
    remember_loc = ("id", "remember_me")

    def input_username(self, user):
        self.send_keys(self.usename_loc, user)

    def input_psw(self,psw):
        self.send_keys(self.psw_loc, psw)

    def click_login_button(self):
        self.click(self.button_loc)

    def click_remember_me(self):
        self.click(self.remember_loc)

    def login(self, user="admin",psw="111111"):
        '''登录流程'''
        self.input_username(user)
        self.input_psw(psw)
        self.click_login_button()

    def is_login_sucess(self):
        # 判断是不是登录成功
        sucess_loc = ("", "")
        result = self.is_text_in_element(sucess_loc,"上海-悠悠")
        return result


if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Firefox()
    login_driver = LoginPage(driver)
    driver.get(login_url)
    login_driver.login()
