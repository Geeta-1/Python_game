# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
conn=sqlite3.connect("fantasy.db")

class Ui_EvaluateWindow(object):
    def setupUi(self, EvaluateWindow):
        EvaluateWindow.setObjectName("EvaluateWindow")
        EvaluateWindow.resize(476, 400)
        self.centralwidget = QtWidgets.QWidget(EvaluateWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 461, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chooseteam = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.chooseteam.setFont(font)
        self.chooseteam.setObjectName("chooseteam")
        self.horizontalLayout.addWidget(self.chooseteam)
        self.teamedit = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.teamedit.setObjectName("teamedit")
        self.horizontalLayout.addWidget(self.teamedit)
        self.choosematch = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.choosematch.setFont(font)
        self.choosematch.setObjectName("choosematch")
        self.horizontalLayout.addWidget(self.choosematch)
        self.matchedit = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.matchedit.setObjectName("matchedit")
        self.teamedit.addItem("")
        self.matchedit.addItem("")
        self.matchedit.addItem("")
        self.matchedit.addItem("")
        self.matchedit.addItem("")
        self.matchedit.addItem("")
        self.horizontalLayout.addWidget(self.matchedit)
        self.player = QtWidgets.QLabel(self.centralwidget)
        self.player.setGeometry(QtCore.QRect(60, 110, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.player.setFont(font)
        self.player.setObjectName("player")
        self.scores = QtWidgets.QLabel(self.centralwidget)
        self.scores.setGeometry(QtCore.QRect(310, 110, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.scores.setFont(font)
        self.scores.setObjectName("scores")
        self.playerlist = QtWidgets.QListWidget(self.centralwidget)
        self.playerlist.setGeometry(QtCore.QRect(40, 130, 121, 192))
        self.playerlist.setObjectName("playerlist")
        self.scorelist = QtWidgets.QListWidget(self.centralwidget)
        self.scorelist.setGeometry(QtCore.QRect(290, 130, 121, 192))
        self.scorelist.setObjectName("scorelist")
        self.outputscore = QtWidgets.QLineEdit(self.centralwidget)
        self.outputscore.setGeometry(QtCore.QRect(290, 330, 121, 20))
        self.outputscore.setObjectName("outputscore")
        self.calscore_2 = QtWidgets.QPushButton(self.centralwidget)
        self.calscore_2.setGeometry(QtCore.QRect(40, 330, 131, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.calscore_2.setFont(font)
        self.calscore_2.setObjectName("calscore_2")
        EvaluateWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EvaluateWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 476, 21))
        self.menubar.setObjectName("menubar")
        EvaluateWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EvaluateWindow)
        self.statusbar.setObjectName("statusbar")
        EvaluateWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EvaluateWindow)
        QtCore.QMetaObject.connectSlotsByName(EvaluateWindow)

    def retranslateUi(self, EvaluateWindow):
        _translate = QtCore.QCoreApplication.translate
        EvaluateWindow.setWindowTitle(_translate("EvaluateWindow", "MainWindow"))
        self.chooseteam.setText(_translate("EvaluateWindow", "Choose Team"))
        self.choosematch.setText(_translate("EvaluateWindow", "Choose Match"))
        self.player.setText(_translate("EvaluateWindow", "Players"))
        self.scores.setText(_translate("EvaluateWindow", "Scores"))
        self.calscore_2.setText(_translate("EvaluateWindow", "Calculate Score"))
        self.teamedit.setItemText(0,_translate("EvaluateWindow", "--SELECT TEAM--"))
        self.matchedit.setItemText(0,_translate("EvaluateWindow", "--SELECT MATCH--"))
        self.matchedit.setItemText(1,_translate("EvaluateWindow", "match1"))
        self.matchedit.setItemText(2,_translate("EvaluateWindow", "match2"))
        self.matchedit.setItemText(3,_translate("EvaluateWindow", "match3"))
        self.matchedit.setItemText(4,_translate("EvaluateWindow", "match4"))
        cur= conn.cursor()
        cur.execute("SELECT Name from Teams;")
        team= cur.fetchall()
        teamlist=[]
        for i in range(len(team)):
            teamlist.append(team[i][0])

        for name in set(teamlist):
            self.teamedit.addItem(name)
            
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EvaluateWindow = QtWidgets.QMainWindow()
    ui = Ui_EvaluateWindow()
    ui.setupUi(EvaluateWindow)
    EvaluateWindow.show()
    sys.exit(app.exec_())

