#coding=utf-8
import xlrd, xlutils
from xlutils import copy

#打开码头文件
bookTerminal = xlrd.open_workbook(r'E:\同步文档\TESTe\terminal.xls')
sheetTerminal = bookTerminal.sheet_by_index(0)
wTerminal = copy.copy(bookTerminal)
wsTerminal = wTerminal.get_sheet(0)

#打开港口xls
bookPort = xlrd.open_workbook(r'E:\同步文档\TESTe\port.xls')
sheetPort = bookPort.sheet_by_index(0)
wPort = copy.copy(bookPort)
wsPort = wPort.get_sheet(0)

# 提取港口id和港口名称的对应
portDict = dict()
for i in range(1, sheetPort.nrows):
    portDict[sheetPort.cell(i, 0).value] = sheetPort.cell(i, 1).value
    #print(portDict)



for i in range(sheetTerminal.ncols):
    value = sheetTerminal.cell(0, i).value

    # 找到附近港口列,修改附近的港口id为具体港口名
    if value == 'port_id':
        for j in range(1, sheetTerminal.nrows):
            portId = sheetTerminal.cell(j, i).value
            
            if portId in portDict.keys():
                portId = portDict[portId]
                print(portId)
            else:
                portId = ""
            #print(portIdLine)
            wsTerminal.write(j, i, portId)
    
            
wTerminal.save(r'E:\同步文档\TESTe\terminal.xls')