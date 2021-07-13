#coding=utf-8
import requests
import json, os, time, yaml
import filepath

headers = {
'EnableStatus': '4',
'MT': '4',
'PID': '20000073',
'IMEI': '6f26dbdfbcb564aa',
'DivideVersion': '3.3.6.5',
'ProtocolVersion': '3.0',
'Pkg': 'com.felink.videopaper.mi',
'SupPhone': 'PACM00',
'CUID': '2897BA228869141F226A3BAB2F013372%7C0',
'IMSI': '91',
'Sign': '9f631a2c7b55450183fc9973089ec55b',
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
r = requests.post("http://pandahome.ifjing.com/action.ashx/ThemeAction/4032", headers=headers, data=data)
#返回200代表连接成功
#print(r.status_code)
#防止返回结果中的中文显示乱码，指定编码格式为utf-8
r.encoding = "UTF-8"
#print(r.text)  
#print(r.json())
#record_count = r.json().get("RecordCount")
theme_requests = r.json().get("ThemeList")
text = filepath.yaml_read("动态模板")
print(text["theme_list"])
#print(text["RecordCount"])

#确认是否新增
print(r.json().get("RecordCount"))

def get_new_theme_list():
    record_count = r.json().get("RecordCount") - text["RecordCount"]
    #增加容错
    record_count += 3

    theme_list = []
    for i in range(record_count):
        theme_id = theme_requests[i]["ThemeId"]
        #print(theme_id)
        if theme_id not in text["theme_list"]:
            theme_list.insert(0,theme_id)
    return(theme_list)

theme_list = get_new_theme_list()
print("新的模板列表为:{}".format(theme_list))
#更新数据，为使得新增的模板编号显示在上方，故而先将text中的模板数据
#写入到获得的列表之后
theme_list = theme_list + text["theme_list"]
text["RecordCount"] = r.json().get("RecordCount")
text["theme_list"] = theme_list
print(text)

# 指定yaml文件路径

yaml_path = filepath.filepath("动态模板")



#调用filepath.yaml_write，写入内容
with open(yaml_path, "w+", encoding="utf-8") as f:
    yaml.dump(text, f,default_flow_style=False,encoding="utf-8",allow_unicode=True)

f.close()
