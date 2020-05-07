from appium import webdriver
import time



def connetFP():

    try:
        print("开始连接手机,打开全局透明壁纸")
        caps = {}
        caps['automationName'] = 'uiautomator2'
        caps["appPackage"] = "com.felink.foregroundpaper"
        caps["appActivity"] = ".SplashActivity"
        caps["platformName"] = "Android"
        caps["deviceName"] = "16th_Plus"
        caps["platformVersion"] = "8.1.0"
        caps["autoAcceptAlerts"] = "True"
        caps["noReset"] = "True"
        caps["skipServerInstallation"] = "True"
        caps["skipDeviceInitialization"] = "True"
    
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        print("连接成功")
        return driver
    except:
        print("连接失败,请检查")

