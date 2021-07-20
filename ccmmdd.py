#coding=utf-8
import subprocess
import time



subprocess.Popen('adb shell screencap -p /sdcard/app.png\n',stdin = subprocess.PIPE)
time.sleep(5)
subprocess.Popen('adb pull /sdcard/app.png E:/app.png',stdin = subprocess.PIPE)
time.sleep(1)
subprocess.Popen('adb shell uiautomator dump /sdcard/app.uix',stdin = subprocess.PIPE)
time.sleep(5)
subprocess.Popen('adb pull /sdcard/app.uix E:/app.uix',stdin = subprocess.PIPE)
#procId.communicate('adb shell screencap -p /sdcard/app.png\n')
#time.sleep(1)
#subprocess.Popen('uiautomatorviewer',stdin = subprocess.PIPE)