import yaml
import os

#获取当前文件夹路径
filePath = os.path.dirname(os.path.realpath(__file__))
print(filePath)
filePath2 = os.path.abspath(".")
print(filePath2)
f = open(r"D:\\30 code\github\code-warehouse\felinkExercise\yaml\mobilePhone.yaml", "r", encoding="utf-8")
#a = yaml.load(f.read())
#print(a)
#print(type(a))
#b = yaml.load(a)
#print(b)
#print(b["oppo"]["platformName"])

yamlPath = os.path.join(filePath,'theme.yaml')
f = open(yamlPath,"w",encoding="utf-8")
yaml.dump