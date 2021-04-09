from appium import webdriver
import time



def connet_FP():

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
        print("连接全局透明壁纸失败,请检查")

def connet_XT():

    try:
        print("开始连接手机,打开羞兔")
        caps = {}
        caps['automationName'] = 'uiautomator2'
        caps["appPackage"] = "com.felink.videopaper.mi"
        caps["appActivity"] = "com.felink.videopaper.activity.WelcomActivity"
        caps["platformName"] = "Android"
        caps["deviceName"] = "meizu"
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

