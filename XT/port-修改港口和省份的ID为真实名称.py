#coding=utf-8
import xlrd, xlutils
from xlutils import copy

bookPort = xlrd.open_workbook(r'E:\同步文档\TESTe\port.xls')
bookProvince = xlrd.open_workbook(r'E:\同步文档\TESTe\province.xls')

sheetPort = bookPort.sheet_by_index(0)
sheetProvince = bookProvince.sheet_by_index(0)

wPort = copy.copy(bookPort)
wProvince = copy.copy(bookProvince)


wsPort = wPort.get_sheet(0)
wsProvince = wProvince.get_sheet(0)

#ws.write(0, 0, "id")
#wb.save(r'E:\同步文档\TESTe\foo.xls')

#for i in range(sheetPort.ncols):

# 提取港口id和港口名称的对应
portDict = dict()
for i in range(1, sheetPort.nrows):
    portDict[sheetPort.cell(i, 0).value] = sheetPort.cell(i, 1).value
    #print(portDict)

provinceDict = dict()
for i in range(1, sheetProvince.nrows):
    provinceDict[sheetProvince.cell(i, 0).value] = sheetProvince.cell(i, 1).value
    print(provinceDict)


for i in range(sheetPort.ncols):
    value = sheetPort.cell(0, i).value

    # 找到附近港口列,修改附近的港口id为具体港口名
    if value == 'nearby_ports':
        for j in range(1, sheetPort.nrows):
            portId = sheetPort.cell(j, i).value
            portIdLine = portId.split(",")
            
            for m in range(len(portIdLine)):
            
                if portIdLine[m] in portDict.keys():
                    portIdLine[m] = portDict[portIdLine[m]] + ","
                else:
                    portIdLine[m] = ""
            #print(portIdLine)
            wsPort.write(j, i, portIdLine)
    
    elif value == 'port_province':
        for j in range(1, sheetPort.nrows):
            provinceId = sheetPort.cell(j, i).value
            # 由于province的excel表中，id的数值与port中的provinceId的值差1，所以这边要加上
            provinceId = str(int(provinceId) + 1)
            if provinceId in provinceDict.keys():
                provinceId = provinceDict[provinceId]
            print(provinceId)
            wsPort.write(j, i, provinceId)
            
wPort.save(r'E:\同步文档\TESTe\port.xls')