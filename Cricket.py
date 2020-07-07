# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cricket.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Evaluate import Ui_EvaluateWindow as Box
import sqlite3
conn=sqlite3.connect("fantasy.db")
cur=conn.cursor()



class Ui_MainWindow(object):
    def __init__(self):
        self.EvaluateWindow=QtWidgets.QMainWindow()
        self.Eval_Screen=Box()
        self.Eval_Screen.setupUi(self.EvaluateWindow)
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(974, 546)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Selection = QtWidgets.QLabel(self.centralwidget)
        self.Selection.setGeometry(QtCore.QRect(10, 10, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Selection.setFont(font)
        self.Selection.setObjectName("Selection")

        #Batman count label
        self.Batman = QtWidgets.QLabel(self.centralwidget)
        self.Batman.setGeometry(QtCore.QRect(10, 40, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Batman.setFont(font)
        self.Batman.setObjectName("Batman")
        #Batman count lineedit
        self.Batcount = QtWidgets.QLineEdit(self.centralwidget)
        self.Batcount.setGeometry(QtCore.QRect(140, 40, 71, 20))
        self.Batcount.setObjectName("Batcount")
        
        
        #Bowler count label
        self.Bowler = QtWidgets.QLabel(self.centralwidget)
        self.Bowler.setGeometry(QtCore.QRect(230, 40, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Bowler.setFont(font)
        self.Bowler.setObjectName("Bowler")
        #Bowler count lineedit
        self.Bowlercount = QtWidgets.QLineEdit(self.centralwidget)
        self.Bowlercount.setGeometry(QtCore.QRect(350, 40, 71, 20))
        self.Bowlercount.setObjectName("Bowlercount")
        
        
        #Wicketkeeper count label
        self.Wickeeper = QtWidgets.QLabel(self.centralwidget)
        self.Wickeeper.setGeometry(QtCore.QRect(440, 40, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Wickeeper.setFont(font)
        self.Wickeeper.setObjectName("Wickeeper")
        #Wicketkeeper count lineedit
        self.Wickeepercount = QtWidgets.QLineEdit(self.centralwidget)
        self.Wickeepercount.setGeometry(QtCore.QRect(610, 40, 71, 21))
        self.Wickeepercount.setObjectName("Wickeepercount")
        
        
        #Allrounder count label
        self.Allrounder = QtWidgets.QLabel(self.centralwidget)
        self.Allrounder.setGeometry(QtCore.QRect(700, 40, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Allrounder.setFont(font)
        self.Allrounder.setObjectName("Allrounder")
        #Allrounder count lineedit
        self.Allroundcount = QtWidgets.QLineEdit(self.centralwidget)
        self.Allroundcount.setGeometry(QtCore.QRect(840, 40, 71, 20))
        self.Allroundcount.setObjectName("Allroundcount")

        #Point available label
        self.PointAvailable = QtWidgets.QLabel(self.centralwidget)
        self.PointAvailable.setGeometry(QtCore.QRect(10, 90, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PointAvailable.setFont(font)
        self.PointAvailable.setObjectName("PointAvailable")
        #Point available lineedit
        self.PointAvailCount = QtWidgets.QLineEdit(self.centralwidget)
        self.PointAvailCount.setGeometry(QtCore.QRect(140, 90, 113, 20))
        self.PointAvailCount.setObjectName("PointAvailCount")
        

        #Point used label
        self.lPointUsed = QtWidgets.QLabel(self.centralwidget)
        self.lPointUsed.setGeometry(QtCore.QRect(400, 90, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lPointUsed.setFont(font)
        self.lPointUsed.setObjectName("lPointUsed")
        #Point used  lineedit
        self.PointUsedCount = QtWidgets.QLineEdit(self.centralwidget)
        self.PointUsedCount.setGeometry(QtCore.QRect(550, 90, 113, 20))
        self.PointUsedCount.setObjectName("PointUsedCount")

        #Batsman Radio Button
        self.BATMAN = QtWidgets.QRadioButton(self.centralwidget)
        self.BATMAN.setGeometry(QtCore.QRect(20, 140, 61, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.BATMAN.setFont(font)
        self.BATMAN.setObjectName("BATMAN")

        #Bowler Radio Button
        self.BOWLER = QtWidgets.QRadioButton(self.centralwidget)
        self.BOWLER.setGeometry(QtCore.QRect(90, 140, 61, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.BOWLER.setFont(font)
        self.BOWLER.setObjectName("BOWLER")
        
        #Wicketkeeper Radio Button
        self.WICKETKEEPER = QtWidgets.QRadioButton(self.centralwidget)
        self.WICKETKEEPER.setGeometry(QtCore.QRect(170, 140, 51, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WICKETKEEPER.setFont(font)
        self.WICKETKEEPER.setObjectName("WICKETKEEPER")
        
        #Allrounder Radio Button
        self.ALLROUNDER = QtWidgets.QRadioButton(self.centralwidget)
        self.ALLROUNDER.setGeometry(QtCore.QRect(240, 140, 51, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ALLROUNDER.setFont(font)
        self.ALLROUNDER.setObjectName("ALLROUNDER")

        #Team lineedit label
        self.Team = QtWidgets.QLabel(self.centralwidget)
        self.Team.setGeometry(QtCore.QRect(410, 140, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Team.setFont(font)
        self.Team.setObjectName("Team")
        
        self.TEAM = QtWidgets.QLineEdit(self.centralwidget)
        self.TEAM.setGeometry(QtCore.QRect(550, 140, 113, 20))
        self.TEAM.setObjectName("TEAM")

        #Exit Pushbutton
        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(320, 430, 151, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Exit.setFont(font)
        self.Exit.setObjectName("Exit")
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 209, 160, 251))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        #Available player listwidget
        self.PLAYERLIST = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.PLAYERLIST.setObjectName("PLAYERLIST")
        self.horizontalLayout.addWidget(self.PLAYERLIST)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(540, 210, 160, 241))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        #Selectec player listwidget
        self.SELECTEDPLAYER = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.SELECTEDPLAYER.setObjectName("SELECTEDPLAYER")
        self.horizontalLayout_2.addWidget(self.SELECTEDPLAYER)

        #Selected player label
        self.Selectedplayer = QtWidgets.QLabel(self.centralwidget)
        self.Selectedplayer.setGeometry(QtCore.QRect(560, 460, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Selectedplayer.setFont(font)
        self.Selectedplayer.setObjectName("Selectedplayer")

        #Available player label
        self.Availableplayer = QtWidgets.QLabel(self.centralwidget)
        self.Availableplayer.setGeometry(QtCore.QRect(80, 470, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Availableplayer.setFont(font)
        self.Availableplayer.setObjectName("Availableplayer")

        #Menubar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 974, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        #New Team Menubar
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.actionNew_Team.setFont(font)
        self.actionNew_Team.setObjectName("actionNew_Team")
        
        #Open Team Menubar
        self.actionOpen_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.actionOpen_Team.setFont(font)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
 
        #Save Team Menubar
        self.actionSave_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.actionSave_Team.setFont(font)
        self.actionSave_Team.setObjectName("actionSave_Team")
        
        #Evaluate Team Menubar
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.actionEvaluate_Team.setFont(font)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.actionEvaluate_Team.triggered.connect(self.Evaluate)

        self.menuManage_Teams.addAction(self.actionNew_Team)
        self.menuManage_Teams.addAction(self.actionOpen_Team)
        self.menuManage_Teams.addAction(self.actionSave_Team)
        self.menuManage_Teams.addAction(self.actionEvaluate_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        

        

        self.PLAYERLIST.itemDoubleClicked.connect(self.removelist1)      #Available Player List Widget
        self.SELECTEDPLAYER.itemDoubleClicked.connect(self.removelist2)  #Selected Player List Widget


        self.BATMAN.toggled.connect(self.ctg)         #BAT Radio Button
        self.BOWLER.toggled.connect(self.ctg)         #BOW Radio Button
        self.WICKETKEEPER.toggled.connect(self.ctg)   #WIK Radio Button
        self.ALLROUNDER.toggled.connect(self.ctg)     #AR Radio Button

        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menu) #Manage Teams Menubar
        self.Exit.clicked.connect(self.exitt)    #Exit Pushbutton
        
        self.Batmancount=0         #count of batsman
        self.Bowlcount=0           #count of bowler
        self.Wicketkeepercount=0   #count of wicketkeeper
        self.Allroundercount=0     #count of allrounder
        self.Pointavailable=1000   #count of available point
        self.Pointused=0           #count of used point

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.Eval_Screen.calscore_2.clicked.connect(self.Calculate)     #Calculate Pushbutton in Evaluate Window

        self.items=[]
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Selection.setText(_translate("MainWindow", "Your Selections"))
        self.Batman.setText(_translate("MainWindow", "Batsman (BAT)"))
        self.Bowler.setText(_translate("MainWindow", "Bowler (BOW)"))
        self.Wickeeper.setText(_translate("MainWindow", "Wicketkeeper (WK)"))
        self.Allrounder.setText(_translate("MainWindow", "All-Rounder (AR)"))
        self.PointAvailable.setText(_translate("MainWindow", "Points Available"))
        self.lPointUsed.setText(_translate("MainWindow", "Points Used"))
        self.BATMAN.setText(_translate("MainWindow", "BAT"))
        self.BOWLER.setText(_translate("MainWindow", "BOW"))
        self.ALLROUNDER.setText(_translate("MainWindow", "AR"))
        self.Team.setText(_translate("MainWindow", "Team Name"))
        self.Exit.setText(_translate("MainWindow", "EXIT"))
        self.Selectedplayer.setText(_translate("MainWindow", "Selected Players"))
        self.WICKETKEEPER.setText(_translate("MainWindow", "WIK"))
        self.Availableplayer.setText(_translate("MainWindow", "Available Player"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNew_Team.setText(_translate("MainWindow", "New Team"))
        self.actionOpen_Team.setText(_translate("MainWindow", "Open Team"))
        self.actionSave_Team.setText(_translate("MainWindow", "Save Team"))
        self.actionEvaluate_Team.setText(_translate("MainWindow", "Evaluate Team"))
    #Exit button 
    def exitt(self):
        import sys
        self.showdialog("Thank You for playing!")
        sys.exit()
        
    #Menu bar 
    def menu(self,action):
        
        txt=(action.text())
        #New file menu
        if txt=='New Team':
            self.Batmancount=0
            self.Bowlcount=0
            self.Wicketkeepercount=0
            self.Allroundercount=0
            self.Pointavailable=1000
            self.Pointused=0
            self.PLAYERLIST.clear()
            self.SELECTEDPLAYER.clear()
            self.TEAM.clear()
            self.PointUsedCount.clear()
            self.PointAvailCount.clear()
            self.Batcount.clear()
            self.Bowlercount.clear()
            self.Wickeepercount.clear()
            self.Allroundcount.clear()

            text, res=QtWidgets.QInputDialog.getText(MainWindow, "Team", "Enter the team name:")
            if res:
                self.TEAM.setText(text)
                team=[]
                cur.execute("SELECT Name FROM Teams;")
                teamal=cur.fetchall()
                for i in range(len(teamal)):
                    team.append(teamal[i][0])
                for j in set(team):
                    if j==text:
                        self.showdialog("Team name already exist")
                        self.TEAM.clear()
                        break
                    else:
                        self.TEAM.setText(text)
                    
            self.Show()
            
        #Save file menu   
        if txt=='Save Team':
            if self.Batmancount+self.Bowlcount+self.Wicketkeepercount+self.Allroundercount!=11:
                self.showdialog("insufficient Player")
                return
                
            for ind in range(self.SELECTEDPLAYER.count()):
                self.items.append(str(self.SELECTEDPLAYER.item(ind).text()))
            actual=[]
            for player in self.items:
                cur.execute("SELECT Value FROM Stats WHERE Player='"+player+"';")
                actual.append(cur.fetchone())
            score=[]
            for i in range(len(actual)):
                score.append(actual[i][0])
            List= tuple(zip(self.items,score))
            teamname= self.TEAM.text()
            teamm=[]
            cur.execute("SELECT Name FROM Teams;")
            teamall=cur.fetchall()
            for i in range(len(teamall)):
                teamm.append(teamall[i][0])
            for j in set(teamm):
                if j==teamname:
                    for i in range(len(List)):
                        cur.execute("UPDATE Teams SET Players=? , Value=?  WHERE Name=?",(List[i][0],List[i][1],teamname))
                    self.showdialog("Team Saved sucessfully")
                    conn.commit()
                    self.items.clear()
                    self.Eval_Screen.teamedit.addItem(self.TEAM.text())
                    break
            
            for i in range(len(List)):
                cur.execute("INSERT INTO Teams ('Name','Players','Value') VALUES ('%s','%s','%d')"%(teamname,List[i][0],List[i][1]))
            self.showdialog("Team Saved sucessfull")
            conn.commit()
            self.items.clear()
            self.Eval_Screen.teamedit.addItem(self.TEAM.text())
            
            
                    

            
          
                    
                    
        #Open file menu   
        if txt=='Open Team':
            self.Batmancount=0
            self.Bowlcount=0
            self.Wicketkeepercount=0
            self.Allroundercount=0
            self.Pointavailable=1000
            self.Pointused=0
            self.PLAYERLIST.clear()
            self.SELECTEDPLAYER.clear()
            self.Show()
            self.OpenTeam()

    #Show Count of Members and Points    
    def Show(self):
        self.Batcount.setText(str(self.Batmancount))
        self.Bowlercount.setText(str(self.Bowlcount))
        self.Wickeepercount.setText(str(self.Wicketkeepercount))
        self.Allroundcount.setText(str(self.Allroundercount))
        self.PointAvailCount.setText(str(self.Pointavailable))
        self.PointUsedCount.setText(str(self.Pointused))

    #Handling error in Members and Points count
    def criteria(self,ctge,item):
        msg=''
        if ctge=="BAT" and self.Batmancount>=5:
            msg="Batsmen more than 5 are not allowed"
        if ctge=="BWL" and self.Bowlcount>=5:
            msg="bowlers more than 5 are not allowed"
        if ctge=="WK" and self.Wicketkeepercount>=1:
            msg="Wicketkeepers more than 1 are not allowed"
        if ctge=="AR" and self.Allroundercount>=3:
            msg="Allrounders more than 3 are not allowed"
        if msg!='':
            self.showdialog(msg)
            return False
        if self.Pointavailable<=0:
            msg="You Have Exhausted your Points"
            self.showdialog(msg)
            return False
        if ctge=="BAT":
            self.Batmancount+=1
        if ctge=="BWL":
            self.Bowlcount+=1
        if ctge=="WK":
            self.Wicketkeepercount+=1
        if ctge=="AR":
            self.Allroundercount+=1
        sql="SELECT Value from Stats where Player='"+item.text()+"'"
        cur=conn.execute(sql)
        row=cur.fetchone()
        self.Pointavailable-=int(row[0])
        self.Pointused+=int(row[0])
        return True

    #Remove players from Available player list
    def removelist1(self,item):
        ctge=''
        if self.BATMAN.isChecked()==True:
            ctge='BAT'
        if self.BOWLER.isChecked()==True:
            ctge='BWL'
        if self.WICKETKEEPER.isChecked()==True:
            ctge='WK'
        if self.ALLROUNDER.isChecked()==True:
            ctge='AR'
        ret=self.criteria(ctge,item)
        if ret==True:
            self.PLAYERLIST.takeItem(self.PLAYERLIST.row(item))
            self.SELECTEDPLAYER.addItem(item.text())
            self.Show()
            
    #Checked the Radio button           
    def ctg(self):
        ctge=''
        if self.BATMAN.isChecked()==True:
            ctge='BAT'
        if self.BOWLER.isChecked()==True:
            ctge='BWL'
        if self.WICKETKEEPER.isChecked()==True:
            ctge='WK'
        if self.ALLROUNDER.isChecked()==True:
            ctge='AR'
        self.fillList(ctge)
        
    #Remove players from Selected player list      
    def removelist2(self,item):
        self.SELECTEDPLAYER.takeItem(self.SELECTEDPLAYER.row(item))
        curs = conn.execute("SELECT Player,Value, Category from Stats where Player='"+item.text()+"'")
        row=curs.fetchone()
        self.Pointavailable=self.Pointavailable+int(row[1])
        self.Pointused=self.Pointused-int(row[1])
        ctge=row[2]
        if ctge=="BAT":
            self.Batmancount-=1
            if self.BATMAN.isChecked()==True:
                self.PLAYERLIST.addItem(item.text())
                
        if ctge=="BWL":
            self.Bowlcount-=1
            if self.BOWLER.isChecked()==True:
                self.PLAYERLIST.addItem(item.text())
                
        if ctge=="WK":
            self.Wicketkeepercount-=1
            if self.WICKETKEEPER.isChecked()==True:
                self.PLAYERLIST.addItem(item.text())
                
        if ctge=="AR":
            self.Allroundercount-=1
            if self.ALLROUNDER.isChecked()==True:
                self.PLAYERLIST.addItem(item.text())
                
        self.Show()

    #Fill the player of Different category in Available Player list 
    def fillList(self,ctge):
        if self.TEAM.text()=='':
            self.showdialog("Enter team name ")
            return
        self.PLAYERLIST.clear()
        sql="SELECT Player from Players where Ctg='"+ctge+"';"
        cur=conn.execute(sql)
        for row in cur:
            selected=[]
            for i in range(self.SELECTEDPLAYER.count()):
                selected.append(self.SELECTEDPLAYER.item(i).text())
            if row[0] not in selected:
                self.PLAYERLIST.addItem(row[0])
                
    #Open team        
    def OpenTeam(self):
        sql="SELECT Name FROM Teams;"
        cur=conn.execute(sql)
        teams=[]
        openlist=[]
        for row in cur:
            teams.append(row[0])
        team,ok=QtWidgets.QInputDialog.getItem(MainWindow,"OpenTeam","Choose Team",set(teams),0,False)
        if ok and team:
            self.TEAM.setText(team)
        teamname=self.TEAM.text()
       
        sql1="SELECT Players,Value FROM Teams WHERE Name='"+teamname+"';"
        cur=conn.execute(sql1)
        openteam=cur.fetchall()
        for i in range(len(openteam)):
            item=QtWidgets.QListWidgetItem(openteam[i][0])
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            item.setBackground(QtGui.QColor('sea green'))
            self.SELECTEDPLAYER.addItem(item)

        self.showdialog("Please Delete All Members to edit the list")

    

        cur=conn.execute("DELETE FROM Teams WHERE Name='"+teamname+"' ;")
        conn.commit()
        for i in range(len(openteam)):
            openlist.append(openteam[i][1])

        point=0
        for j in openlist:
            point=point+int(j)
        self.Pointused=point
        self.Pointavailable=1000-point
        count=self.SELECTEDPLAYER.count()
        for i in range(count):
            ply=self.SELECTEDPLAYER.item(i).text()
            sql="SELECT Category FROM Stats WHERE Player='"+ply+"';"
            cur=conn.execute(sql)
            row=cur.fetchone()
            ctge=row[0]
            if ctge=="BAT":
                self.Batmancount+=1
            if ctge=="BWL":
                self.Bowlcount+=1
            if ctge=="WK":
                self.Wicketkeepercount+=1
            if ctge=="AR":
                self.Allroundercount+=1
        
        self.Show()
        
    #Calculation of Score in Evaluate Window
    def Evaluate(self):
        self.EvaluateWindow.show()
        
   
    def Calculate(self):
        self.Eval_Screen.scorelist.clear()
        teamtl=0
        total=[]
        import sqlite3
        conn=sqlite3.connect("fantasy.db")
        cur=conn.cursor()
        team = self.Eval_Screen.teamedit.currentText()
        cur.execute("SELECT Players from Teams WHERE name='"+team+"';")
        player= cur.fetchall()
        self.Eval_Screen.playerlist.clear()
        for i in range(len(player)):
            item= QtWidgets.QListWidgetItem(player[i][0])
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            item.setBackground(QtGui.QColor('#ffff99'))
            self.Eval_Screen.playerlist.addItem(item)
        ttl,batscore,bowlscore,fieldscore=0,0,0,0
        for i in range(self.Eval_Screen.playerlist.count()):
            
            nam=self.Eval_Screen.playerlist.item(i).text()
            cur=conn.execute("SELECT * FROM Match WHERE Player='"+nam+"' ")
            row=cur.fetchone()
            batscore=int(row[1]/2)
            if batscore>=50: batscore+=5
            if batscore>=100: batscore+=10
            if row[1]>0:
                sr=row[1]/row[2]
                if sr>=80 and sr<100: batscore+=2
                if sr>=100:batscore+=4
            batscore=batscore+row[3]
            batscore=batscore+2*row[4]
          
            bowlscore=row[8]*10
            if row[8]>=3: bowlscore=bowlscore+5
            if row[8]>=5: bowlscore=bowlscore=bowlscore+10
            if row[7]>0:
                er=6*row[7]/row[5]
               
                if er<=2: bowlscore=bowlscore+10
                if er>2 and er<=3.5: bowlscore=bowlscore+7
                if er>3.5 and er<=4.5: bowlscore=bowlscore+4
            fieldscore=(row[9]+row[10]+row[11])*10
            ttl=batscore+bowlscore+fieldscore
            total.append(str(ttl))
            teamtl=teamtl+ttl
        for i in range(len(total)):
            item= QtWidgets.QListWidgetItem(total[i])
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            item.setBackground(QtGui.QColor('#ffff99'))
            self.Eval_Screen.scorelist.addItem(item)
        self.Eval_Screen.outputscore.setText(str(teamtl))
       
       
    #Show Messagebox
    def showdialog(self,msg):
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("Team selector")
        ret=Dialog.exec()

        



    
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

