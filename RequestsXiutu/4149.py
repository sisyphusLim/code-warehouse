#coding=utf-8
import requests
import json, os, time, yaml
import filepath

#动态壁纸tab列表获取，注意调试模式下通过id搜索壁纸功能不可用

headers = filepath.yaml_read("headers")["xiutu_headers"]
#print(headers)
data = '{"PageIndex":1,"PageSize":20,"Density":2.75,"GetWebp":1,"Resolution":"1080x2400"}'
r = requests.post("http://pandahome.ifjing.com//action.ashx/themeaction/4149",headers=headers,data=data)
#print(r.status_code)
r.encoding = "UTF-8"

#print(r.json())
a = r.json().get("ResList")
#b = a[4]["Data"]["ResId"]
#c = a[4]["Data"]["ResName"]
for i in range(20):
    b = a[i+1]["Data"]["ResId"]
    c = a[i+1]["Data"]["ResName"]
    print(b,c)
# 需要处理获取的数据中包含“排行榜”等字段的问题
