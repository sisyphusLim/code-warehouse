#coding=utf-8
# 版本：1.01

import time, io, sys, re, os
import requests
import json
from openpyxl import Workbook

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print("数据爬取成功")
        return r.text

    except:
        return("爬取数据出现异常")

def excelId(A, i):

    excelName =  str(A) + str(i)

    return excelName

#查询海运管家
def queryMarine(shipId, shipName, i, name):
    try:
        print("现在在{}上查询{}".format(name,shipName))
        #构造url 
        url = "http://mm.51haixun.com/voyage/get?shipId=" +shipId
        #处理数据
        marineShip = json.loads(getHTMLText(url))["data"]["aisData"]

        print("数据处理完毕，准备写入excel表")
        #数据写入Excel
        dataShip[excelId("A",i)] = shipName
        dataShip[excelId("B",i)] = marineShip["dprtPort"]
        dataShip[excelId("C",i)] = marineShip["settingSailTime"]
        dataShip[excelId("D",i)] = marineShip["destPort"]
        dataShip[excelId("E",i)] = marineShip["eta"]
        dataShip[excelId("F",i)] = marineShip["updateTime"]
        dataShip[excelId("G",i)] = name
        print("写入完毕")
        print(end=" \n")
        return i

    except:
        dataShip[excelId("A",i)] = shipName
        dataShip[excelId("B",i)] = "无数据或者出现异常"
        dataShip[excelId("G",i)] = name
        return("在{}上查询{}结果异常".format(name, shipName))


#查询船讯网数据
def queryShipxyI(mmsi, shipName, i, name):
    try:
        print("现在在{}上查询{}".format(name, shipName))
        #构造url
        url1 = "http://i.shipxy.com/ship/GetShips?shipIDs=" +mmsi
        url2 = "http://i.shipxy.com/ship/GetCurrvoyageNew?mmsi=" +mmsi



        dataList = json.loads(getHTMLText(url1))["data"]
        message1 = dataList[0]
        message2 = json.loads(json.loads(getHTMLText(url2))["data"])
        print("数据处理完毕，准备写入excel表")
        #数据写入Excel
        dataShip[excelId("A",i)] = shipName
        dataShip[excelId("B",i)] = message2["depportname_en"]
        dataShip[excelId("C",i)] = message2["deptime"]
        dataShip[excelId("D",i)] = message1["dest"]
        dataShip[excelId("E",i)] = message1["eta"]
        dataShip[excelId("F",i)] = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(message1["lastdyn"]))
        dataShip[excelId("G",i)] = name
        print("写入完毕")
        print(end=" \n")
        return i
    except:
        dataShip[excelId("A",i)] = shipName
        dataShip[excelId("B",i)] = "无数据或者出现异常"
        dataShip[excelId("G",i)] = name
        print("在{}上查询{}结果异常".format(name, shipName))

#查询船队在线数据
def queryHifleet(mmsi, shipName, i, name):
    try:
        print("现在在{}上查询{}".format(name, shipName))
        #构造url
        url = "http://www.hifleet.com/getShipsFeatureXml.do?mmsi="+mmsi+"&limit1=0&limit2=1&select_type=5"
        url_updatetime = "http://www.hifleet.com/queryMyFleetsShips.do?mmsis="+mmsi


        #处理数据
        shipHifleet = getHTMLText(url)
        #构造一个新的url去获取最后更新时间
        shipNamePy = re.findall("<shipname>(.+?)</shipname>",shipHifleet)[0].replace(" ", "+")
        url_updatetime = "http://www.hifleet.com/sameShipSearch.do?keyword="+shipNamePy
        shipHifleetUpdate = getHTMLText(url_updatetime)
        print("数据处理完毕，准备写入excel表")
        dataShip[excelId("A",i)] = shipName
        dataShip[excelId("B",i)] = re.findall("<startportcnname>(.+?)</start", shipHifleet)[0]
        dataShip[excelId("C",i)] = re.findall("<starttime>(.+?)</start", shipHifleet)[0]
        dataShip[excelId("D",i)] = re.findall("<endportcnname>(.+?)</end", shipHifleet)[0]
        dataShip[excelId("E",i)] = re.findall("<eta>(.+?)</eta", shipHifleet)[0]
        dataShip[excelId("F",i)] = re.findall('updatetime":"(.+?)",', shipHifleetUpdate)[0]
        dataShip[excelId("G",i)] = name
        print("写入完毕")
        print(end=" \n")
        return i
    except:
        dataShip[excelId("A",i)] = shipName
        dataShip[excelId("B",i)] = "无数据或者出现异常"
        dataShip[excelId("G",i)] = name
        print("在{}上查询{}结果异常".format(name, shipName))

#查询船达通
def queryShipdt(mmsi, shipName, i, name):
    try:
        print("现在在{}上查询{}".format(name, shipName))
        #构造url
        url = "http://www.shipdt.com/lvservice/ship/getUnFocusShipData?shipmmsi="+mmsi+"&cookievalue=mcRB9su9uFq8GmWnkTAZoA%3D%3D"
        #处理数据
        shipShipdt = json.loads(getHTMLText(url))["data"]
        print("数据处理完毕，准备写入excel表")
        dataShip[excelId("A",i)] = shipName
        dataShip[excelId("B",i)] = json.loads(shipShipdt)["result0"]["departurePortEnName"]
        dataShip[excelId("C",i)] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(eval(json.loads(shipShipdt)["result0"]["departTime"])))
        dataShip[excelId("D",i)] = json.loads(shipShipdt)["result1"]["dest_port"]
        dataShip[excelId("E",i)] = json.loads(shipShipdt)["result1"]["eta"]
        dataShip[excelId("F",i)] = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(eval(json.loads(shipShipdt)["result1"]["postime"])))
        dataShip[excelId("G",i)] = name
        print("写入完毕")
        print(end=" \n")
        return i
    except:
        dataShip[excelId("A",i)] = shipName
        dataShip[excelId("B",i)] = "无数据或者出现异常"
        dataShip[excelId("G",i)] = name
        print("在{}上查询{}结果异常".format(name, shipName))

#尝试读取txt
def readFile(fileName):
    try:
        list_ship = open("{}".format(fileName))
        listShips = list_ship.readlines()
        return listShips
    except FileNotFoundError as err:
        print("当前目录不存在{}文件:  ".format(fileName) + str(err))

#创建初始excel表
start = time.perf_counter()

excel = Workbook()
dataShip = excel.active
dataShip["A1"] = "船名"
dataShip["B1"] = "起始港"
dataShip["C1"] = "起航时间"
dataShip["D1"] = "目的港"
dataShip["E1"] = "预抵时间"
dataShip["F1"] = "最后更新时间"
dataShip["G1"] = "平台"
i = 2

#从文件中逐行读取需要抓取的船舶信息
list_Ships = readFile("ships.txt")
print("开始读取要查询的船舶...")
print("船舶数据:{}".format(list_Ships))

for each_line in list_Ships:
    try:
        shipId = each_line.split(",")[0]
        mmsi = each_line.split(",")[1]
        shipName = each_line.split(",")[2]
        shipMessage_marine = queryMarine(shipId, shipName, i, name = "海运管家")
        i = i + 1
        shipMessage_shipxyI = queryShipxyI(mmsi, shipName, i, name = "船讯网")
        i = i + 1
        shipMessage_hifleet = queryHifleet(mmsi, shipName, i, name = "船队在线")
        i = i + 1
        shipMessage_shipdt = queryShipdt(mmsi, shipName, i, name = "船达通")
        i = i + 2
    except:
        continue

#以时间戳为名保存为excel
name = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
excel.save(r".\{}.xlsx".format(name))

end = time.perf_counter()
print("本次查询完毕，总共耗时{}秒,结果输出到{}.xlsx".format(end - start, name))
os.system('pause')