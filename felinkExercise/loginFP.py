# coding: utf-8

#from appium import webdriver
from connetFP.connetFP import connetFP
from login.login import login_user
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
import time

driver = connetFP()
# 通过权限


size = driver.get_window_size()
width = size['width']
height = size['height']
print("获取当前屏幕大小成功:宽 {}, 高 {}".format(width, height))



# 登录

## 访问我的

mine_tab = driver.find_element_by_id("com.felink.foregroundpaper:id/fp_tv_v8_mine")
if mine_tab.is_selected() == False:
    print("点击'我的'标签")
    mine_tab.click()

#time.sleep(2)

## 确认登录状态
login_button = driver.find_element_by_xpath("//*[@text='请登录']").click()
time.sleep(2)

## 测试登账登录-失败
login_user(driver, 13599096447, "muyi1198")
 
try:
    xpath = '//*[contains(@text,"账号或密码错误")]'
    WebDriverWait(driver,10,0.01).until(EC.presence_of_element_located((MobileBy.XPATH,xpath)))
except Exception as e:
    print('没找到！！',e)
else:
    print('找到对应的toast！！',xpath)

login_user(driver, 13599096666, "muyi1987")
## 登录测试账号-成功
login_user(driver, 13599096447, "muyi1987")

'''def find_toast(message, timeout, poll_frequency):
    #获取toast信息文本并验证
    message1 = "//*[@text=\'{}\']".format(message)
    element = WebDriverWait(timeout, poll_frequency).until(
        EC.presence_of_element_located((By.XPATH, message1)))
    return element.text'''