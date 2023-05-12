import os, sys
from PyQt5 import QtCore, QtGui
# import mysql.connector
from pathlib import Path
from appdirs import AppDirs
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

sys.path.append(str(Path(__file__).resolve().parents[1]))

class Ui_Dialog(QDialog, QWidget, object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Choose")
        Dialog.resize(450,300)
        self.cwd = os.getcwd()
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(20)

        # render help text
        self.text_brow = QTextBrowser()

        # choose path button
        self.btn_Extensions = QPushButton("Extensions", self)  
        self.btn_Extensions.setObjectName("btn_Extensions")  
        self.btn_Extensions.clicked.connect(self.slot_btn_Extensions)
        self.btn_Extensions.setFont(font)
        self.btn_Extensions.setFixedWidth(400)

        # choose file button
        self.btn_Data = QPushButton("Data", self)  
        self.btn_Data.setObjectName("btn_Data")  
        self.btn_Data.clicked.connect(self.slot_btn_Data)
        self.btn_Data.setFont(font)
        self.btn_Data.setFixedWidth(400)
        
        self.layout1 = QVBoxLayout()
        self.layout1.addWidget(self.btn_Extensions)
        self.layout1.addWidget(self.btn_Data)
        self.layout2 = QVBoxLayout(Dialog)
        self.layout2.setObjectName("Layout2")    
        self.layout2.addWidget(self.text_brow)             

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setObjectName("buttonBox")
        self.layout2.addWidget(self.buttonBox)

        self.layout2.addWidget(self.btn_Extensions)
        self.layout2.addWidget(self.btn_Data)

        self.retranslateUi(Dialog) 
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def event(self, event):
        if event.type()==QtCore.QEvent.EnterWhatsThisMode:
            QWhatsThis.leaveWhatsThisMode()
            self.text_brow.setText("Please check your extension\nfor extra required packages\nsuch as tomas\nand pip install them")
        return QDialog.event(self,event)

    def slot_btn_Extensions(self):
        Extensions = QFileDialog.getExistingDirectory(self,"Choose Extensions",self.cwd) # 起始路径
        if Extensions == "":
            print("\nchoose canceled")
            return

        # write extension into user_data_dir
        text_create('extension_path', Extensions)
        print("\nExtensions:",Extensions)

    def slot_btn_Data(self):
        Data, file_type = QFileDialog.getOpenFileName(self,"Choose Data", self.cwd)   # 设置文件扩展名过滤,用双分号间隔

        if Data == "":
            print("\nchoose canceled")
            return

        # write Data into user_data_dir
        text_create('data_file', Data)
        print("\nData:",Data)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Choose", "Choose"))


def mkdir(path):
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print(path + ' successful creat')
        return True
    else:
        print(path + ' already exist')


def text_create(name, msg):
    path = dir + "\\" + name + '.txt'
    print("-========- path:", path)
    with open(path, "w") as f:
        f.truncate(0)
        f.close()
    file = open(path, 'w')
    file.write(msg)
    file.close()


def main():
    global dir
    # create the file to write data
    appname = "scpantheon"
    appauthor = "xinzhu"
    version = "0.2.1"
    dirs = AppDirs(appname, appauthor, version)
    dir = dirs.user_data_dir
    mkdir(path=dir)
    # create qt app
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    app.exec()
    return 'app closed'

