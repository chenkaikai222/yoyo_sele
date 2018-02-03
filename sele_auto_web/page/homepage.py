# coding:utf-8
from common.base import BasePage

home_url = "http://www.cnblogs.com/yoyoketang/"
class HomePage(BasePage):

    bky_loc = ("id", "blog_nav_sitehome")
    nav_loc = ("id", "blog_nav_myhome")
    xsb_loc = ("id", "blog_nav_newpost")

    def click_bky(self):
        self.click(self.bky_loc)

    def click_nav(self):
        self.click(self.nav_loc)

    def click_xbs(self):
        self.click(self.xsb_loc)

    def is_exists_img(self):
        img_loc = ("xpath", ".//*[@id='logo']/h1/a/img")
        return self.is_exists(img_loc)


if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Firefox()
    homedriver = HomePage(driver)
    driver.get(home_url)
    homedriver.click_bky()