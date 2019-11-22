# coding: utf-8

#from appium import webdriver
from connetFP.connetFP import connetFP
from swipe.swipe import Swipe
import time

driver = connetFP()
# 通过权限


size = driver.get_window_size()
width = size['width']
height = size['height']
print("获取当前屏幕大小成功:宽 {}, 高 {}".format(width, height))



# 登录

## 访问我的

mineTab = driver.find_element_by_id("com.felink.foregroundpaper:id/fp_tv_v8_mine")
if mineTab.is_selected() == False:
    print("点击'我的'标签")
    mineTab.click()

a = driver.find_element_by_name("请登录")
a.click()