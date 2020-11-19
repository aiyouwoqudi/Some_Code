'''
author:     oprater
data:       2020.6.14
vision:     1.3
introduction:
    Achieve the achievement of Academic Affairs,
    Still can't realize verification code  automaticly,
    looking for vision 2
'''

from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
from jsonpath import jsonpath
import xlwt
from PIL import Image


class Login(object):
    # 初始化函数
    def __init__(self):
        flag = 1
        # 请求头
        self.headers = \
        {
            'Referer': 'http://stuzhjw.imust.edu.cn/login',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
            'Host': 'stuzhjw.imust.edu.cn'
        }
        # 登录请求地址
        self.post_url = 'http://stuzhjw.imust.edu.cn/j_spring_security_check'
        # 验证码请求地址
        self.yzm_url = 'http://stuzhjw.imust.edu.cn/img/captcha.jpg'
        #按照课程属性（选修必修）排列的callback网址：
        self.facj_url = 'http://stuzhjw.imust.edu.cn/student/integratedQuery/scoreQuery/coursePropertyScores/callback'
        #按照方案成绩排列的callback网址：
        #self.facj_url = 'http://stuzhjw.imust.edu.cn/student/integratedQuery/scoreQuery/schemeScores/callback'
        # 维持一个session保持登录
        self.session = requests.Session()

    # 模拟登录函数
    def login(self):
        #设置登录成功标志
        flag = 1
        while (flag):
            # 多次重复快捷查询在此处键入个人信息替换下句
            #account = "1767119111"
            #password = "Ma865241"
            account = input("+++++请输入学号：")
            password = input("------请输入密码：")
            #print("输入学号为："+account)
            #print("输入密码为："+password )
            # 请求验证码并保存到本地
            with open("CatchCode.jpg", "wb") as f:
                f.write(self.session.get(self.yzm_url, headers=self.headers).content)

            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("************验证码请求成功**********")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            #显示验证码
            img = Image.open("D:/python37/python_workfile/CatchGreed3/venv/CatchCode.jpg","r")
            img.show()
            # 暂时手动输入验证码
            yzm = input("请查看根目录下的CatchCode中的验证码，并输入:")
            print ("********>您输入的验证码为:"+yzm+"<***********")
            # 抛出的post数据表单
            post_data = {
                'j_username': account,
                'j_password': password,
                'j_captcha': yzm,
            }
            # 请求登录
            loginResponse = self.session.post(self.post_url, data=post_data, headers=self.headers)
            # 打印结果
            print("------>状态码：" + str(loginResponse.status_code)+"<-------")
            answer = loginResponse.status_code
            #打印登陆成功后的HTML界面判断是否正确
            # print(loginResponse.text)
            #此处默认状态码除200之外失败
            if (answer == 200):
                print("*********************************")
                print("**********教务登录成功*************")
                print("*********************************")
                flag = 0
            else:
                print("--->_<--->登录失败<--->_<--------------->请查看刷新后的验证码后重新键入账户信息<------")
                flag = 1
        r = self.session.get(self.facj_url)
        #用状态码验证成绩页面是否登录成功 除200外认为失败
        if (r.status_code == 200):
            print("---------------------------------")
            print("|*****方案成绩网页登录成功**********|")
            print("---------------------------------")
        else:
            print("---+_+-方案成绩网页登录失败-+_+--")
            print("---+-+-请尝试重新登录-+-+--")
        self.html = r.text
        #可利用以下三行将请求到的json数据保存到本地
        # with open("JsonData.txt",'w') as f:
        #     f.write(json.dumps(html))
        #     f.close()
        print("*********************************")
        print("******方案成绩网页数据抓取成功******")
        print("*********************************")



    # 解析函数
    #对请求到的json数据进行解析,并将所需数据生成List
    #此处该有更简洁的办法来解析嵌套的json数据来加快速度
    def GetList(self):
        print("成绩列表生成中.......请稍后...")
        json_data = json.loads(self.html)
        #print(json_data)#检测json数据是否成功读出
        courseName = jsonpath(json_data, "$..courseName")
        # print(courseName)#检测数据表头是否写入，成功则输出数据，失败输出FALSE
        # 以下List为成绩的主要属性，可查看json中其他属性后自行添加，格式相同
        courseNumber = jsonpath(json_data, "$..courseNumber")
        courseName = jsonpath(json_data, "$..courseName")
        credit = jsonpath(json_data, "$..credit")
        gradePointScore = jsonpath(json_data, "$..gradePointScore")
        courseAttributeName = jsonpath(json_data, "$..courseAttributeName")
        examTypeCode = jsonpath(json_data, "$..examTypeCode")
        examTime = jsonpath(json_data, "$..examTime")
        courseScore = jsonpath(json_data, "$..courseScore")
        operator = jsonpath(json_data, "$..operator")
        operatingTime = jsonpath(json_data, "$..operatingTime")
        planName = jsonpath(json_data, "$..planName")
        academicYearCode = jsonpath(json_data, "$..academicYearCode")
        termName = jsonpath(json_data, "$..termName")
        gradeName = jsonpath(json_data, "$..gradeName")
        englishCourseName = jsonpath(json_data, "$..englishCourseName")
        #将所有的list存到data中生成二维成绩表单
        self.data = [courseNumber,courseName, credit, courseScore, gradePointScore, courseAttributeName,
                academicYearCode, termName, gradeName, englishCourseName]
        print("*********************************")
        print("*********成绩列表已生成*************")
        print("*********************************")

    #写入数据到文本函数
    def DownLodeList(self):
        # 文件保存路径(需要在最后自定义一个xlsx文件)
        self.file_path = 'D:/方案成绩文件.xlsx'
        print("正在将成绩列表写入文件中....请稍后....")
        #打开xlsx文件写入表头
        output = open(self.file_path, 'w')
        output.write('课程号\t课程名称\t学分\t分数\t成绩绩点\t课程属性'
                     '\t学年\t学期\t成绩属性\t课程英文名\n')
        for i in range(len(self.data[0])):
            for j in range(len(self.data)):
                output.write(str(self.data[j][i]))
                output.write('\t')  #控制格式
            output.write('\n')
        output.close()
        #输出结果
        print("*************************************************************")
        print('***********数据已成功写入'+self.file_path+'中*******************')
        print("*************************************************************")



def main():
    __name__ == "__main__"
    myLogin = Login()
    myLogin.login()
    myLogin.GetList()
    myLogin.DownLodeList()
    print("*********以抓取课程属性网址成绩************")
    print("****************************************")
    print("**--*^-^*----本次爬取成绩成功咯----*^-^*--**")
    print("****************************************")
    print("------>请到自定义路径查看成绩（默认D盘下）<------")
    print("********程序已退出*********")

main()
