#coding=utf-8

import logging, time
from selenium.webdriver.support.wait import WebDriverWait


def find_Element(self, type, value, wait=15):
    loggin.info("使用find_element方法开始查找元素")

    try:
        if type == "id":
            try:
                return self.driver.find_element(By.ID, value)
            except:
                logging.error(u"未能找到 %s 元素"%(value))
                return False
        elif type == "name":
            try:
                return self.driver.find_element(By.NAME, value)
            except:
                logging.error(u"未能找到 %s 元素"%(value))
                return False
    except:
        logging.warn(msg)

