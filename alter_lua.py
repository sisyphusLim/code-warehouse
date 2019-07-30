#coding=utf-8
# 修改2ui的插件默认配置,自用
import os, winreg

# 找到内容并修改,之后重新写入文件
def alter_lua(file_name, old_str, new_str):
    #path = game_path
    #path = r"D:\World of Warcraft\_retail_\Interface\AddOns\_ShiGuang\Core"
    #根据文件名,组合成路径
    file_name = os.path.join(path, file_name)
    file_data = ""

    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            #找到需要修改的那一行
            if old_str in line:
                print(line)
                line = line.replace(old_str, new_str)
                print(line)
            #将每一行都赋值到file_data中
            file_data += line
    #将结果重新写入到文件中
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(file_data)

# 从注册表获取游戏目录
def game_path(reg_string):
    if "HKEY_" in reg_string:
        # 裁出根键和路径来
        #root_key = reg_string.split("\\\",1)[0]
        sub_key = reg_string.split("\\",1)[1]
    else:
        sub_key = reg_string
    
    # 定位子键位置
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, sub_key)
    #通过子键位置，以及项的名称，获得对应的值，在这里就是游戏路径
    value, _type = winreg.QueryValueEx(key, "InstallPath")
    return(value)


# 注册表位置，不要以\开头(split时会出问题)，同时组成插件目录的路径
reg_string = r"HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Blizzard Entertainment\World of Warcraft"
path = os.path.join(game_path(reg_string), "Interface\AddOns\_ShiGuang\Core")
#print(path)

# 插件默认的设置
old_strs = ['Style = 6', 
'CrazyCatLady = true', 
'Wallpaperkit = true', 
'AutoReagentBank = true', 
'kAutoOpen = true', 
'xMerchant = true']

# 希望修改的设置
new_strs = ['Style = 4', 
'CrazyCatLady = false', 
'Wallpaperkit = false', 
'AutoReagentBank = false', 
'kAutoOpen = false', 
'xMerchant = false']


for i in range(len(old_strs)):
    old_str = old_strs[i]
    new_str = new_strs[i]
    file_name = "GUI.lua"
    alter_lua(file_name, old_str, new_str)

alter_lua("Tutorial.lua", "ChatFrame1:SetWidth(360)", "ChatFrame1:SetWidth(420)")
alter_lua("Tutorial.lua", "ChatFrame1:SetHeight(121)", "ChatFrame1:SetHeight(200)")
