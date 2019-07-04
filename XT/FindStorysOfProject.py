#coding=utf-8
import pymysql
import os

#在当前目录创建一个.md文件用于保存数据并打开开开


#连接数据库
db = pymysql.connect("192.168.5.102", "root", "Hzx@120415", "zentao")
#print(db)
#使用cursor()方法创建一个游标对象
cursor = db.cursor()




#获取一个项目对应的所有需求名称和链接
def get_storyname(project_id):

    #构建数据库查询语句，查询项目ID(id)对应的项目名称(name)
    sql_project = 'select name from zt_project where id = {}'.format(project_id)
    #使用execute()方法查询数据库
    cursor.execute(sql_project)
    #使用fetchall()方法输出结果到project_list
    project_list = cursor.fetchall()
    #print(project_list)
    #将项目标题、地址等写到psmd_list里
    psmd_list = '[TOC]' + '\n' + '## [{}项目完成情况](http://192.168.5.102/zentao/project-task-{}.html)'.format(project_list[0][0], project_id)
    psmd_list = psmd_list + '\n' + '----'

    #构建数据库查询语句，查询zt_projectstory下project_id对应的所有story_id
    sql_projectStory = 'select story from zt_projectstory where project = {}'.format(project_id)    #使用execute()方法执行SQL查询
    cursor.execute(sql_projectStory)
    story_id_list = cursor.fetchall()
    #print(story_id_list)
    

    #将具体id从数组中提取到列表中
    for i in range(len(story_id_list)):
        sql_story = 'select title from zt_story where id = {}'.format(story_id_list[i][0])
        cursor.execute(sql_story)
        story_name = cursor.fetchone()
            

        #构建保存数据
        psmd_list = psmd_list + '\n' + '\n'\
            + '### [{0} {1}](http://192.168.5.102/zentao/story-view-{0}.html)'.format(story_id_list[i][0], story_name[0])\
            + '\n' +'完成情况:' + '\n' + '<small>待确认</small>'
        #print(psmd_list)
    
        i = i+1
    print(psmd_list)    
    write_into_md(psmd_list, project_list[0][0])
    #创建一个.md文件用来保存数据

def write_into_md(psmd, project_name):
    with open("{}项目完成情况.md".format(project_name), mode='w+', encoding='utf-8') as f:
        f.write(psmd)
        f.close
        


if __name__ == "__main__":
    project_id = input("请输入项目id(数字)：")
    if project_id.isdigit():
        try:
            get_storyname(project_id)
        except IndexError:
            print("可能不存在编号为{}的项目，请检查后重试".format(project_id))
    else:
        print("输入错误")
        
    #构建数据库查询语句，查询zt_story下story_id对应的需求名称(title)
    #sql_story = 'select * from zt_story where id = ' + story_id
