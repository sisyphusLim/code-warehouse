#coding: utf-8

'''
处于登录界面时,进行登录操作
'''

from appium import webdriver

# 账号名登录
def login_user(driver, username, password):
    driver.find_element_by_id("com.felink.foregroundpaper:id/user_agreement_checkbox").click()
    driver.find_element_by_id("com.felink.foregroundpaper:id/input_user_name").send_keys(username)
    driver.find_element_by_id("com.felink.foregroundpaper:id/input_password").send_keys(password)
    driver.find_element_by_id("com.felink.foregroundpaper:id/submit_login").click()


# 第三方登录