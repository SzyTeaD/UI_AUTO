import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config.pathes import REPORT_PATH, NOW, DAY


def new_report():
    lists = os.listdir(REPORT_PATH)
    #获取路径下的文件
    lists.sort(key=lambda fn: os.path.getmtime(REPORT_PATH))
    #按照时间顺序排序
    new_report = os.path.join(REPORT_PATH,lists[-1])
    #获取最近时间的
    return new_report


def send_mail():

    senduser = '676307573@qq.com'
    sendpswd = 'erfiwskmmmwlbahh'
    receusers = ['yangxin@htyunwang.com','zhangminghui@htyunwang.com']

    report = new_report()
    # # 获取报告文件
    # f = open(report, 'rb')
    # body_main = f.read()
    msg = MIMEMultipart()
    # 邮件标题
    msg['Subject'] = Header('云端营销自动化测试报告' + NOW, 'utf-8')
    # 邮件内容
    text = MIMEText('云端营销测试报告，请查收！\n'+'自动发送请勿回复！', 'html', 'utf-8')
    msg.attach(text)
    # 发送附件
    # att = MIMEApplication(open(report, 'rb').read())
    att = MIMEText(open(report, 'rb').read(), 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    #att["Content-Disposition"] = 'attachment; filename="houseinformation.txt"'
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