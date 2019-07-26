#coding=utf-8
import os
import shutil


def is_dir(dirName):
    #循环查询路径是否是文件
    for eachFile in os.listdir(dirName):
        #print(eachFile)
        eachFile1 = os.path.join(dirName,eachFile)
        #如果也是文件,循环函数
        if os.path.isdir(eachFile1) is True:
            is_dir(eachFile1)
        #如果不是,移动文件到指定目录
        else:
            #print(eachFile1)
            try:
                #由于循环执行函数之后,dirName的值会变,所以这里设置目标路径时引用的是des_dir
                newDir = os.path.join(des_dir, eachFile)
                print(des_dir,eachFile)
                #print(newDir)
                shutil.move(eachFile1, newDir)
            except:
                continue
            


if __name__ == "__main__":
    dirName = r"F:\暂存重命名"
    des_dir = dirName
    is_dir(dirName)

