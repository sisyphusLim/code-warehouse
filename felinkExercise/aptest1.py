# coding: utf-8

#from appium import webdriver
from connetFP.connetFP import connetFP
from swipe.swipe import Swipe
import time

driver = connetFP()
time.sleep(5)
# 通过权限




## 个人信息保护指引
try:
    infoText = driver.find_element_by_id("com.felink.foregroundpaper:id/btn_confirm")
    infoText.click()
except:
    print("没找到该元素")

## 权限
try:
    perWindow = driver.find_element_by_id("com.felink.foregroundpaper:id/tv_open")
    print("找到了")
    perWindow.click()
except:
    print("没找到该元素")   

# 获取权限

try:
    andPer = driver.find_element_by_id("android:id/action_bar_title")
    print("找到了")
    time.sleep(2)
    window = Swipe(driver)
    #window.get_window_size()
    window.swipeUp(500,2)
except:
    print("上滑失败")


'''el1 = driver.find_element_by_id("com.felink.foregroundpaper:id/btn_confirm")
el1.click()
el2 = driver.find_element_by_id("com.felink.foregroundpaper:id/tv_open")
el2.click()
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[3]/android.widget.TextView")
el3.click()
el4 = driver.find_element_by_id("android:id/button1")
el4.click()
el5 = driver.find_element_by_id("com.felink.foregroundpaper:id/tv_open")
el5.click()
el6 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[14]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView")
el6.click()
el7 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[14]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView")
el7.click()
el8 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[14]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Switch")
el8.click()
el9 = driver.find_element_by_id("com.felink.foregroundpaper:id/tv_open")
el9.click()
el10 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
el10.click()
el11 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
el11.click()
el12 = driver.find_element_by_id("com.felink.foregroundpaper:id/iv_videoplayer_video_surface")
el12.click()
driver.back()'''

#driver.quit()