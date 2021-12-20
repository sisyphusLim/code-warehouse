# coding: utf-8

import time
from connetFP.connetFP import connet_XT
from login.login import login_user
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy

driver = connet_XT()
driver.implicitly_wait(10)