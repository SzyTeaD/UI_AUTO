from project.chandao.login import login
from utils.basic import browser, Basic
from utils.FileReader import ExcelReader


class CreatTask():
    def __init__(self,phases,assignor = 1):
        self.url='http://172.20.4.25/index.php?m=project&f=task&projectID=38&type=unclosed'
        self.driver = browser()
        self.dr = Basic(self.driver)
        self.dr.get_url(self.url)
        self.assignor = assignor
        self.phases = phases

    def mode(self):
        #所属模块
        self.dr.click('class','chosen-single')
        self.driver.find_element_by_class_name('chosen-single').send_keys('云端营销')
        # self.dr.input('class','chosen-single','云端营销')

    def  name(self,index,name):
        #任务名称
        self.dr.input('id','name['+ index +']',self.phases + name)

    def type(self):
        #类型
        self.driver.find_element_by_id('type0').send_keys('测试')
        # self.dr.input('id','type0','测试')

    def assignedTo(self,name):
        #指派给
        self.driver.find_element_by_css_selector('[style="overflow:visible"]').send_keys(name)
        # self.dr.input('css','[style="overflow:visible"]',name)
        #self.dr.input('id','assignedTo0',name)

    def estimate(self,index,time):
        #预计时间
        self.dr.input('id','estimate['+ index +']',time)

    def desc(self,index,desc):
        #任务描述
        self.dr.input('id','desc['+ index +']',desc)

    def pri(self,index,pri):
        #优先级别
        self.driver.find_element_by_id('pri'+index).send_keys(pri)
        # self.dr.input('id','pri'+index,pri)

    def loggin(self):
        usr = 'yangxin'
        psw = 'BzhO%07Bv29AuTg3sV'
        login(self.dr,usr,psw)

    def creat(self):
        self.dr.click('css','[class="btn btn btn-secondary"]')

    def folwType(self, i=0):
        f = r'F:\Python\py_work\UI_AOTO\project\chandao\creat_task.xlsx'
        reader = ExcelReader(f, title_line=True)
        folw_type = reader.data[i]
        return folw_type

    def main(self):
        '''
        :param assignor: 1 = 杨鑫  0 = 张明辉
        :return:
        '''
        self.mode()
        self.type()
        if self.assignor == '0':
            pass
            #self.assignedTo('张明辉')
        else:
            #self.assignedTo('杨鑫')
            self.name(str(7),'【云端营销】本周测试任务分配')
            self.estimate(str(7),'0.5')
            self.desc(str(7),'本周测试任务分配')
            self.pri(str(7),2)
            self.name(str(6),'【云端营销】创建本周测试计划、测试单、套件，分配执行人等')
            self.estimate(str(6),'0.5')
            self.desc(str(6),'创建本周测试计划、测试单、套件，分配执行人等')
            self.pri(str(6),2)
        for i in range(6):
            self.name(str(i),self.folwType(i)['name'])
            self.estimate(str(i),int(self.folwType(i)['estimate']))
            self.desc(str(i),self.folwType(i)['desc'])
            self.pri(str(i),int(self.folwType(i)['pri']))



if __name__ == '__main__':
    print('0是张明辉的任务')
    print('1是杨鑫的任务')
    assignor = input('请输入编号')
    phases = '【7.22-7.26】'
    a = CreatTask(phases,assignor)
    a.loggin()
    a.creat()
    a.main()