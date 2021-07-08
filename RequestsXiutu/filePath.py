#coding=utf-8
import os

# 指定yaml文件路径
def filepath(path):
    filepath = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(filepath,"yaml")
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    filepath = os.path.join(filepath,"{}.yaml".format(path))
    return filepath

# 读取：
def yaml_read(filepath,path):
    filepath = filepath(path)
    print(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        a = yaml.load(f)
        if a == None:
            return None
        else:
            return a
            
f = yaml_read(filepath, "test")