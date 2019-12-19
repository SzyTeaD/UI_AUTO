import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config.pathes import REPORT_PATH, NOW, DAY, PROJECTINFO
from utils.FileReader import YamlReader


class Mail():
    def __init__(self,project):
        self.project = project
        self.senduser = YamlReader(PROJECTINFO).get(self.project).get('mail')['senduser']   # 发送邮箱
        self.sendpswd = YamlReader(PROJECTINFO).get(self.project).get('mail')['sendpswd']   # 授权码
        self.receusers = YamlReader(PROJECTINFO).get(self.project).get('mail')['receusers']    # 收信邮箱
        self.report = self.new_report()   # 获取报告文件
        self.log = self.new_log()   # 获取日志

    def new_log(self):
        log = open(self)

    def new_report(self):
        '''筛选出最新的报告'''
        lists = os.listdir(REPORT_PATH)
        #获取路径下的文件
        lists.sort(key=lambda fn: os.path.getmtime(REPORT_PATH))
        #按照时间顺序排序
        new_report = os.path.join(REPORT_PATH,lists[-1])
        #获取最近时间的
        return new_report

    def send_mail(self):
        f = open(self.report, 'rb')
        body_main = f.read()
        msg = MIMEMultipart()
        msg['Subject'] = Header('今日情况' + NOW, 'utf-8')  # 邮件标题
        text = MIMEText('%s '% body_main, 'html', 'utf-8') # 邮件内容


        msg.attach(text)
        att = MIMEText(open(report, 'rb').read(), 'base64', 'utf-8')    # 发送附件
        att['Content-Type'] = 'application/octet-stream'
        att.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', DAY + "_report.html"))
        msg.attach(att)

        smtp = smtplib.SMTP()
        smtp.connect('smtp.qq.com')
        smtp.login(senduser, sendpswd)
        msg['From'] = senduser
        for receuser in receusers :
            msg['To'] = receuser
            smtp.sendmail(senduser, receuser, msg.as_string())



if __name__ == '__main__':
    eml = Mail('OA')
