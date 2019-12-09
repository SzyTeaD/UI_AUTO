import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config.pathes import REPORT_PATH, NOW, DAY


def new_report():
    '''筛选出最新的报告'''
    lists = os.listdir(REPORT_PATH)
    #获取路径下的文件
    lists.sort(key=lambda fn: os.path.getmtime(REPORT_PATH))
    #按照时间顺序排序
    new_report = os.path.join(REPORT_PATH,lists[-1])
    #获取最近时间的
    return new_report


def send_mail():

    senduser = '676307573@qq.com'   #发送邮箱
    sendpswd = 'atcimddyfallbebb'   #授权码
    receusers = ['676307573@qq.com']    #收信邮箱

    report = new_report()   # 获取报告文件
    f = open(report, 'rb')
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
    send_mail()