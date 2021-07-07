#coding=utf-8
import requests
import json, os, time, yaml


headers = {
'EnableStatus': '0',
'MT': '4',
'PID': '20000073',
'IMEI': '6f26dbdfbcb564aa',
'DivideVersion': '3.3.6',
'ProtocolVersion': '3.0',
'Pkg': 'com.felink.videopaper.mi',
'SupPhone': 'PACM00',
'CUID': '2897BA228869141F226A3BAB2F013372%7C0',
'IMSI': '',
'Sign': 'aa82f866cb2ed3b23734f9f76586d04b',
'SupFirm': '10',
'BranchName': 'xiutu',
'SessionId': '',
'Content-Type': 'text/plain; charset=UTF-8',
'Content-Length': '103',
'Host': 'pandahome.ifjing.com',
'Accept-Encoding': 'gzip',
'User-Agent': 'okhttp/3.4.1',
'Connection': 'keep-alive'
}


data = '{"TagIds":"","ResTypes":"80029","SortOrder":1,"PageIndex":1,"PageSize":20,"GetWebp":1,"ClientSDKVer":7}'

r = requests.post("http://pandahome.ifjing.com/action.ashx/ThemeAction/4032", headers=headers, data=data,)
#返回200代表连接成功
print(r.status_code)
#防止返回结果中的中文显示乱码，指定编码格式为utf-8
r.encoding = "UTF-8"
#print(r.text)  
#print(r.json())
print(r.json().get("RecordCount"))
dict = r.json().get("ThemeList")

#找到模板的yaml文件
filePath = os.path.dirname(os.path.realpath(__file__))
filePath = os.path.join(filePath,'testyaml\\testyaml')

# 获取时间，作为yaml中的参数
timeNow = time.strftime("%Y%m%d%H%m%S")
print(timeNow)
#获取列表中的第一个模板编号
themeD = {}
themeDict = {timeNow:themeD}
for i in range(20):
    themeId = dict[i]['ThemeId']
    themeName = dict[i]['Name']
    theme = {themeId:themeName}
    themeD.update(theme)

print(themeDict)

# 获取目录路径
filePath = os.path.dirname(os.path.realpath(__file__))
filePath = os.path.join(filePath,'testyaml')
if not os.path.exists(filePath):
    os.makedirs(filePath)
print(filePath)

'''
#查看上层目录
pwd = os.getcwd()
print(os.path.dirname(pwd))
'''

# 创建yaml文件路径，并将themeDict新增写入
# a,追加写入， w，覆盖写入

yamlPath = os.path.join(filePath,'theme.yaml')



with open(yamlPath,"w",encoding="utf-8") as f:
    print(themeDict,'\n')
    yaml.dump(themeDict,f,default_flow_style=False,encoding="utf-8",allow_unicode=True)


'''
#使用w，会覆盖原有yaml文件
with open(yamlPath,"w",encoding="utf-8") as f:
    print(themeDict)
    yaml.dump(themeDict,f,default_flow_style=False,encoding="utf-8",allow_unicode=True)
'''
f.close