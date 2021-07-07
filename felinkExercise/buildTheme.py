# coding: utf-8

#from appium import webdriver
from connetFP.connetFP import connet_XT
from login.login import login_user
#from swipe.swipe import Swipe
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
import time


driver = connet_XT()

time.sleep(3)
diy_tab = driver.find_element_by_id("main_tab_diy_layout")
if diy_tab.is_selected() == False:
    print("点击'定制'tab页")
    diy_tab.click()

#time.sleep(3)
driver.find_element_by_xpath("//*[@text='定制']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@text='特效模板']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@text='编号:3577565']").click()



