#coding=utf-8
import os,yaml

# 指定yaml文件路径
def filepath(path):
    filepath = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(filepath,"yaml")
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    filepath = os.path.join(filepath,"{}.yaml".format(path))
    return filepath

# 读取：
def yaml_read(path):
    yaml_path = filepath(path)
    if not os.path.exists(yaml_path):
        return "文件不存在"
    with open(yaml_path, "r", encoding="utf-8") as f:
        yaml_text = yaml.load(f)
        if yaml_text  == None:
            return "文件为空"
        else:
            f.close()
            return yaml_text 

def yaml_write(yaml_text, path):
    yaml_path = filepath(path)
    with open(yaml_path,"w+",encoding="utf-8") as f:
        yaml.dump(yaml_text,f,default_flow_style=False,encoding="utf-8",allow_unicode=True)
        f.close()      

#c = yaml_read("headers")
#print(c)
#yaml_write({1:2,3:5},"text")
