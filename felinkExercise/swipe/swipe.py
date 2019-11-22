#coding: utf-8

from appium import webdriver

class Swipe():
    def __init__(self, driver):
        self.driver = driver

    def get_window_size(self):
        """
        获取屏幕的长宽
        """
        print("尝试获取当前屏幕大小")
        try:
            size = self.driver.get_window_size()
            width = size['width']
            height = size['height']
            print("获取当前屏幕大小成功:宽 {}, 高 {}".format(width, height))
            return width,height
        except:
            print("获取屏幕大小失败")


    def swipeUp(self, t=500, n=2):
        '''
        向上滑动
        '''
        print("正在准备向上滑动屏幕")
        try:
            size = self.get_window_size()
            x=size[0]*0.5
            y=size[1]*0.8
            x1=size[0]*0.5
            y1=size[1]*0.2
            for i in range(n):
                self.driver.swipe(x,y,x1,y1,t)
                print("屏幕第{}次向上滑动成功".format(i+1))
        except:
            print("屏幕向上滑动失败")