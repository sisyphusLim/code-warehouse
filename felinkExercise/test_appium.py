#coding=utf-8
#from appium import webdriver
from connetFP.connetFP import connetFP
from login.login import login_user
#from swipe.swipe import Swipe
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
import time


class TestDemo:

    def setup(self):
       self.driver = self.connetFP() 

    def test_login(self):
        self.mine_tab = self.driver.find_element_by_id("com.felink.foregroundpaper:id/fp_tv_v8_mine")
        if self.mine_tab.is_selected() == False:

            print("??'??'??")
            self.mine_tab.click()
        
        self.login_user(self.driver, 13599096447, "123456a")


    def teardown(self):
        self.driver(quit)

