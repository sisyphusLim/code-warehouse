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
#测试一下
#search_theme("3577565", driver)

def make_theme(theme_id,driver=driver):
    
    search_theme(theme_id)
    driver.find_element_by_id("tv_make").click()
    
    #这里如果未登录，需要插入一个登录会员账号的流程。
    '''
    if driver.find_element_by_id("submit_login") is not None:
        print(driver.find_elements_by_id("submit_login"))
        login_user(driver, 13599096447, "123456a")
    '''

    driver.find_element_by_id("img_select_material").click()

    #假使需要指定图片目录
    #driver.find_element_by_id("mSetArrowImg").click()
    #driver.find_element_by_android_uiautomator('resourceId("name").text("我的壁纸")').click()

    #下面查找时使用了find_elements_by_xxxx，会报错'list' object has no attribute 'click' 因为找到的元素是一个列表
    driver.find_element_by_android_uiautomator('new UiSelector().resourceId("mRoot").index(14)').click()
    
    driver.find_element_by_id("tv_rightBtn").click()
    driver.find_element_by_id("crop_finish_btn").click()
    #可能出现图片无法识别的问题，需要引入纠错流程
    driver.find_element_by_id("btn_next").click()
    driver.find_element_by_id("tv_make").click()

    #等待合成完成，保存并返回，预留30s
    WebDriverWait(driver, 30).until(lambda x: x.find_element_by_id(("tv_save")).is_displayed())
    driver.find_element_by_id("tv_save").click()
    driver.find_element_by_id("img_close").click()
    print("模板{}合成完成".format(theme_id))



make_theme("3577565",driver)  
    





