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
driver.implicitly_wait(10)


diy_tab = driver.find_element_by_id("main_tab_diy_layout")
if diy_tab.is_selected() == False:
    print("回到首页")
    diy_tab.click()

def search_theme(theme_id,driver=driver):
    # 点击输入框，输入模板编号进行搜索
    try:
        #模糊搜索“搜索”
        driver.find_element_by_android_uiautomator('new UiSelector().textContains("搜索")').click()
        driver.find_element_by_id('search_navigation_edit_text').send_keys("{}".format(theme_id))
        driver.find_element_by_id('search_navigation_search').click()
        driver.find_element_by_xpath("//*[@text='编号:{}']".format(theme_id)).click()
    except:
        print("出错了")

search_theme("3577565", driver)

def make_theme(theme_id,driver=driver):
    
    search_theme(theme_id)
    if 





