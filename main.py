import ticket,os
class ui(object):
    def __init__(self):
        self.activityID = None
        self.ticketDB = ticket.TicketDB()
    def loadMenu(self):
        os.system("clear")
        print("----加载数据库----\n1.创建数据库\n2.打开数据库\n----------------")
        choice = input("[ ]\b\b")
        if choice == '1':
            self.ticketDB.createDB()
            self.mainMenu()
        if choice == '2':
            path = input('路径> ')
            try:
                f = open(path,'r')
                self.ticketDB.loadDB(f)
                f.close()
                self.mainMenu()
            except FileNotFoundError:
                print("错误: 找不到文件")
                exit()
    def saveMenu(self):
        os.system("clear")
        print("----保存----")
        path = input('路径: ')
        try:
            f = open(path,'w')
            self.ticketDB.saveDB(f)
            f.close()
        except FileNotFoundError:
            print("错误: 找不到文件")
            exit()

    def choiceActivity(self):
        os.system("clear")
        print("----活动列表----")
        print("ID | 名称")
        for x in range(len(self.ticketDB.db['activities'])):
            activity = self.ticketDB.db['activities'][x]
            print(f"{x} | {activity['activityName']}")
        self.activityID = int(input("活动ID: [   ]\b\b\b\b"))
    def addTicket(self):
        while True:
            os.system("clear")
            print("----添加核销码----")
            ticketID = input("核销码: [      ]\b\b\b\b\b\b\b")
            if ticketID != "":
                self.ticketDB.addTicket(self.activityID,ticketID)
            else:
                return 0
    def editTicket(self):
        os.system("clear")
        print("----编辑核销码----")
        ticketID = input("核销码: [      ]\b\b\b\b\b\b\b")
        try:
            enabled = self.ticketDB.db['activities'][self.activityID]['tickets'][ticketID]
            print(f"核销码状态: {enabled}")
            edit = input("编辑? [Y/N]")
            if edit == 'y' or edit == 'Y':
                enabled = eval(input("新状态 [True/False]: "))
                self.ticketDB.editTicket(self.activityID,ticketID,enabled)
            else:
                pass
        except:
            print("错误: 核销码不存在或状态格式错误")
    def addActivity(self):
        os.system("clear")
        print("----新建活动----")
        activityName = input("活动名称: ")
        aid = self.ticketDB.addActivity(activityName)
        print(f"活动ID: {aid}")
    def checkTicket(self):
        while True:
            os.system("clear")
            print("----核销系统----")
            ticketID = input("核销码: [      ]\b\b\b\b\b\b\b")
            if ticketID == "exit":
                return 0
            r = self.ticketDB.checkTicket(self.activityID,ticketID)
            if r == 0:
                print("完成")
            elif r == 1:
                print("禁用的核销码")
            elif r == 2:
                print("核销码不存在")
            input("按下Enter键继续...")
    def mainMenu(self):
        while True:
            os.system("clear")
            if self.activityID == None:
                print("""----主菜单----
0.退出
1.保存数据库
2.选择活动
3.添加活动
[未选择活动,部分功能暂不可用]
-------------
""")
            else:
                print("""----主菜单----
0.退出
1.保存数据库
2.选择活动
3.添加活动
4.开始核销[输入核销码"exit"退出核销模式]
5.添加核销码[留空退出]
6.编辑核销码
-------------
""")
            choice = input("主菜单: [ ]\b\b")
            if choice == '0':
                exit()
            elif choice == '1':
                self.saveMenu()
            elif choice == '2':
                self.choiceActivity()
            elif choice == '3':
                self.addActivity()
            elif choice == '4':
                self.checkTicket()
            elif choice == '5':
                self.addTicket()
            elif choice == '6':
                self.editTicket()

if __name__ == "__main__":
    u = ui()
    u.loadMenu()