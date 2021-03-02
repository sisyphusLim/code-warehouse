#coding=utf-8
import requests
import json


headers = {
'EnableStatus': '0',
'MT': '4',
'PID': '20000073',
'IMEI': '004b6784c4e79e89',
'DivideVersion': '3.3.2',
'ProtocolVersion': '3.0',
'Pkg': 'com.felink.videopaper.mi',
'SupPhone': 'Redmi K30',
'CUID': '84CAFFCD6EA60F5E2E783842EFB2751D%7C0',
'IMSI': '',
'Sign': '2d5040323217921bea97e62a41c3de38',
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


data = '{"TagIds":"","ResTypes":"80029","SortOrder":1,"PageIndex":1,"PageSize":20,"GetWebp":1,"ClientSDKVer":6}'

r = requests.post("http://pandahome.ifjing.com/action.ashx/ThemeAction/4032", headers=headers, data=data,)
#返回200代表连接成功
print(r.status_code)
#防止返回结果中的中文显示乱码，指定编码格式为utf-8
r.encoding = "UTF-8"  
#print(r.json())
print(r.json().get("RecordCount"))
dict = r.json().get("ThemeList")
#获取列表中的第一个模板编号
themeList = []
for i in range(10):
    themeId = dict[i]['ThemeId']
    themeList.append(themeId)

print(themeList)

