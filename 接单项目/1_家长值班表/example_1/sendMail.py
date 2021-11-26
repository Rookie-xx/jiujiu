#!/usr/bin/python
# -*- coding: UTF-8 -*-
#邮件发送模块
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

#邮件发送类
class sendMail:
    m_sender:str = ""  #发送者邮箱
    m_receivers:tuple = []  #接收者邮箱
    m_context:str = ""  #邮件内容
    m_title:str = ""  #邮件标题
    sender_name:str = ""  #发送者名称
    receivers_name:str = "" #接收者名称
    __mail_smtp:str = ""  #邮箱SMTP
    __mial_enc:MIMEMultipart = None
    __mail_ins:MIMEText = None   #邮件实体类
    __default_code:str = "utf-8"   #默认编码
    __empower_code:str = ""  #授权码

    def __init__(self):
        self.__mail_ins = None
        self.__mial_enc = None
        self.m_receivers = []

    #获取授权码
    def getEmpowerCode(self)->str:
        return self.__empower_code;

    #获取SMTP路径
    def getMailSmtp(self)->str:
        return self.__mail_smtp

    #检测邮箱账号格式
    def checkMailFormat(self, address:str)->bool:
        if address.find("@") == - 1:
            print("邮件格式错误!")
            return False;
        return  True

    #设置授权码
    def setEmpowerCode(self, code:str):
        self.__empower_code = code

    #设置邮箱SMTP路径
    def setMailSmtp(self, url:str):
        self.__mail_smtp = url

    #发送前的准备
    # enc -> 若要发送带附件的邮件，则此参数不为空
    def sendMailReady(self, enc:MIMEMultipart = None):
        ucode = self.__default_code
        self.__mail_ins = MIMEText(self.m_context, 'plain', ucode)
        #保留原始兼容方案
        # self.__mail_ins['From'] = Header(self.sender_name, ucode)
        # self.__mail_ins['To'] = Header(self.receivers_name, ucode)
        # self.__mail_ins['Subject'] = Header(self.m_title, ucode)
        if enc != None:
            enc['From'] = "{}".format(self.m_sender)
            enc['To'] = ",".join(self.m_receivers)
            enc['Subject'] = self.m_title
            self.__mial_enc = enc
        else:
            self.__mail_ins['From'] = "{}".format(self.m_sender)
            self.__mail_ins['To'] = ",".join(self.m_receivers)
            self.__mail_ins['Subject'] = self.m_title

    #发送邮件
    def sendMail(self, enc:MIMEMultipart = None):
        try:
            #smtpObj = smtplib.SMTP(self.__mail_smtp)  #老方案
            smtpObj = smtplib.SMTP_SSL(self.__mail_smtp, 465)  # 启用SSL发信, 端口一般是465
            smtpObj.login(self.m_sender, self.__empower_code)  # 邮箱smtp的授权码
            if self.checkMailFormat(self.m_sender) == True:
                index = 0
                reces = len(self.m_receivers)
                #检测邮箱格式
                for key in self.m_receivers:
                    if self.checkMailFormat(key) == True:
                        index += 1
                if index == reces:
                    as_string:str = ""
                    if self.__mial_enc != None:
                        as_string = self.__mial_enc.as_string()
                    else:
                        as_string = self.__mail_ins.as_string()
                    smtpObj.sendmail(self.m_sender, self.m_receivers, as_string)
                    print("邮件发送成功")
                else:
                    print("邮件发送失败, 请查看邮件格式!")
                smtpObj.quit()  #退出邮件服务
            else:
                print("邮件发送失败, 请查看邮件格式!")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")

    #设置带附件的邮件
    def setEnclosureMail(self,els:str, file_name:str)->MIMEMultipart:
        mime = None
        file_src = els + "" + file_name
        try:
            #fileApart = MIMEApplication(open(file_src, "rb").read())
            fileApart = MIMEText(open(file_src, "rb").read(), "base64", "utf-8")
            fileApart["Content-Type"] = "application/octet-stream"
            fileApart.add_header("Content-Disposition", "attachment", filename=("gbk", "", file_src))
            #fileApart.add_header("Content-Type: application/vnd.penxmlformats-officedocument.wordprocessingml.document")
            mime = MIMEMultipart()
            mime.attach(fileApart)
        except FileNotFoundError:
            print(file_name + "文件不存在！")
        return mime

#剔除字符串左右两边的空格与回车
def deleteSpaceStr(stc:str)->str:
    stc = stc.lstrip()
    stc = stc.rstrip()
    stc = stc.replace("\n", "")
    return  stc

def readConfig(url)->dict:
    # 文件读取字典
    file_dict = {
        "m_sender": "",
        "m_title": "",
        "m_smtp": "",
        "m_context": "",
        "m_code": ""
    }
    ctx_tag = False
    fs = open("./config.txt", "r", encoding="utf-8")  # 只读打开
    while 1:
        line = fs.readline()
        if not line:
            break
        else:
            #若内容读取标记打开，则执行内容文本链接
            if ctx_tag == True:
                if line.find("=") != -1:    #当读取到的某行带=号，则表示内容读取结束
                    ctx_tag = False
                file_dict["m_context"] += line
            if line.find("我的邮箱") != -1:
                file_dict["m_sender"] = deleteSpaceStr(line.split("=")[1])
            if line.find("邮箱服务") != -1:
                file_dict["m_smtp"] = deleteSpaceStr(line.split("=")[1])
            if line.find("我的授权码") != -1:
                file_dict["m_code"] = deleteSpaceStr(line.split("=")[1])
            if line.find("邮件标题") != -1:
                file_dict["m_title"] = deleteSpaceStr(line.split("=")[1])
            if line.find("邮件内容") != -1:
                ctx_tag = True
                file_dict["m_context"] += line.split("=")[1]
    fs.close()
    return file_dict

dict_data =  readConfig("")
#邮件发送对象
# mail = sendMail()
# mail.m_sender = str(dict_data["m_sender"])
# mail.m_receivers = ["cj18760099334@163.com"]
# mail.m_context = str(dict_data["m_context"])
# mail.m_title = str(dict_data["m_title"])
# mail.sender_name = "陈健"
# mail.receivers_name = "合金装备"
# mail.setMailSmtp(str(dict_data["m_smtp"]))
# mail.setEmpowerCode(str(dict_data["m_code"]))
# mail.sendMailReady()
# mail.sendMail()
