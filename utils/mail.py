import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config.pathes import REPORT_PATH, NOW, DAY, PROJECTINFO, LOG_PATH
from utils.FileReader import YamlReader


class Mail(object):
    def __init__(self, project, receusers=None):
        self.m = YamlReader(PROJECTINFO).get(project).get('mail')
        if not os.path.exists(REPORT_PATH):
            os.mkdir(REPORT_PATH)
        self.senduser = self.m['senduser']   # 发送邮箱
        self.sendpswd = self.m['sendpswd']   # 授权码
        self.receusers = receusers if receusers else self.m['receusers']  # 收信邮箱

    def new_report(self):
        """筛选出最新的报告"""
        lists = os.listdir(REPORT_PATH)        # 获取路径下的文件
        lists.sort(key=lambda fn: os.path.getmtime(REPORT_PATH))        # 按照时间顺序排序
        new_report = os.path.join(REPORT_PATH, lists[-1])        # 获取最近时间的
        return new_report

    def new_log(self):
        lists = os.listdir(LOG_PATH)
        lists.sort(key=lambda fn: os.path.getmtime(LOG_PATH))
        new_log_file = os.path.join(LOG_PATH, lists[-1])
        new_log = open(new_log_file, 'r', encoding='utf-8').read()
        return new_log

    def remove_log(self):
        """删除多余邮件"""
        while True:
            lists = os.listdir(REPORT_PATH)
            log_count = len(set(lists))
            if log_count <= 5:
                break
            else:
                lists.sort(key=lambda fn: os.path.getmtime(REPORT_PATH))
                old_log_file = os.path.join(REPORT_PATH, lists[0])
                os.remove(old_log_file)

    def send_mail(self):
        self.remove_log()
        body_main = self.new_log()
        report = self.new_report()
        msg = MIMEMultipart()
        msg['Subject'] = Header('今日情况' + NOW, 'utf-8')  # 邮件标题
        text = MIMEText(body_main, 'html', 'utf-8')  # 邮件内容
        msg.attach(text)
        att = MIMEText(open(report, 'rb').read(), 'base64', 'utf-8')    # 发送附件
        att['Content-Type'] = 'application/octet-stream'
        att.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', DAY + "_report.html"))
        msg.attach(att)
        smtp = smtplib.SMTP()
        smtp.connect('smtp.qq.com')
        smtp.login(self.senduser, self.sendpswd)
        msg['From'] = self.senduser
        for receuser in self.receusers:
            msg['To'] = receuser
            smtp.sendmail(self.senduser, receuser, msg.as_string())


if __name__ == '__main__':
    l = []
    receusers = YamlReader(PROJECTINFO).get('OA').get('mail')['receusers'][0]
    l.append(receusers)
    print(l)
    eml = Mail('OA')
    eml.send_mail()

