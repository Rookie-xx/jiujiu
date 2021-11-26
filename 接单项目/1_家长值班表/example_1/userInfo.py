#数据类
class tableInfo:
    __id:int = 0  #序号
    student_name:str = ""  #学生姓名
    parent_name:str = ""  #父母姓名
    phone:str = ""   #联系方式
    mail:str = ""  #邮箱
    dutys:list = []  #方便值班时间
    duty_total:int = 0    #值班次数
    duty_can:int = 0   #可值班次数
    duty_tab:dict = {}  #每周值班表

    def __init__(self):
        self.dutys = []
        self.duty_tab = {}

    def setID(self, id:int):
        self.__id = id

    def getID(self)->int:
        return self.__id

    def createDutyTab(self):
        index = 1
        tag = 0
        for value in self.dutys:
            #不可值班
            if value == "" or value == None:
                tag = -1
            else:
                tag = 1
                self.duty_can += 1  #每周可值班的总次数加一
            self.duty_tab[str(index)] = tag
            index += 1
