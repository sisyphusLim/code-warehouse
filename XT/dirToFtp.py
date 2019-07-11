#coding=utf-8
#连接ftp服务器并上传文件至指定目录

from ftplib import FTP
import sys
import os


def ftpConnect():
    ftp_server = '192.168.1.54'
    username = 'yezhiyang'
    password = '_hzx151204'
    ftp=FTP()
    ftp.set_debuglevel(0)
    #修改服务器的ftp编码
    ftp.encoding = "GBK"
    #连接ftp服务器，需要输入IP，端口，以及超时时间
    ftp.connect(ftp_server,21,600)
    #连接的用户名、密码
    ftp.login(username,password)
    return ftp

def upLoadFile(localFile, remoteFile, local):
    global ftp
    #ftp = ftpConnect()
    bufsize = 1024
    #ftpmkd(remoteFile)
    print(remoteFile)

    #从本地上传文件到指定目录
    with open(localFile, "rb" ) as fp:
        ftp.storbinary("STOR " + remoteFile + "\\" + local, fp, bufsize)
        #ftp.set_debuglevel(2)
        #ftp.quit()

def upLoadFiles(localDir, remoteDir):
    print(localDir, remoteDir)
    global ftp
    #ftp = ftpConnect()
    localNames = os.listdir(localDir)
    ftpmkd(remoteDir)
    

    for local in localNames:
        src = os.path.join(localDir, local)
        redir = os.path.join(remoteDir, local)
        
        if os.path.isdir(src) is True:
            ftpmkd(redir)
            upLoadFiles(src, redir)
        else:
            #remoteDir = os.path.join(remoteDir, local)
            print(src, remoteDir,local)
            upLoadFile(src,remoteDir, local)

    #ftp.quit()    

# 在ftp上尝试创建目录,如已存在,则跳过
def ftpmkd(remoteFile):
    global ftp
    #ftp = ftpConnect()
    try:
        ftp.mkd(remoteFile)
    except :
        pass



# 获取输入,返回本地路径和ftp路径
def getInput():
    project = input('请选择并输入产品名称(HYGJ,ERP,ProjectReport):')
    if project.lower() in ["hygj", "erp", "projectreport"]:
        localDir = input('请输入要上传的文件或目录路径,结尾不能是"\\"或者"/"：')
        localDir = localDir.replace('/', "\\")
        if os.path.isdir(localDir) is True:
            local = localDir.split("\\")[-1]
            remoteDir = "/{}/{}".format(project, local) 
        else:
            remoteDir = "/" + project
        return(localDir, remoteDir)
    else:
        print("您的输入可能有误，请按要求输入")
        getInput()


if __name__ == "__main__":
    ftp = ftpConnect()
    path = getInput()
    upLoadFiles(path[0], path[1])
    ftp.quit()