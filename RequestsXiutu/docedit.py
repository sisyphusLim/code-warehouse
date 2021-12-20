#coding=utf-8
import os,yaml

def theme_path():
    path = os.popen('adb shell ls sdcard/Pictures/羞兔').read().splitlines()

def dir_rename(oldDir,newDir):

    


    