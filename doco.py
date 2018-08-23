
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doco.ui'
#
# Created: Wed Mar 29 13:01:48 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!
# Other code by dearvee
# 2017-4-4 it is suppose [m4a,mp3] 
import os
import sys
import url
import time
import eyed3
import shutil
import pygame
import urllib
import ffmpeg
import random
import requests
from PyQt5.QtCore import *  
from PyQt5 import QtCore, QtGui, QtWidgets

path = 'd:/doco'

#path = os.path.expanduser("~")+'\Music'

pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)
if not os.path.exists(path):
    os.makedirs(path)


names = []
count = 0
format = []
url_names = ['1','2']#url.geturl('lili','names')
mp3_urls = ['1','2']#url.geturl('lili','srcs')
lrc_urls = ['1','2']


one = True
#first play
loop = False
order = True
rand = False
pos = 0
search = False
desklrc = False


class Get():
    def Names():
        global names
        names = []
        global files
        files = os.listdir(path+'/')
        for file in files:
            if os.path.isfile(path+'/'+file):
                if file[-3:]=='mp3':
                    names.append(file[:-4])
                if file[-3:]=='m4a':
                    os.remove(path+'/'+file)
                    print('success delete~')

    def Lrcs():
        global times
        global words
        global words_w
        times = [[] for i in range(len(names))]
        words = [[] for i in range(len(names))]
        words_w = [[] for i in range(len(names))]
        for n in range(len(names)):
            try:
                lrcs = open(path+'/'+names[n]+'.lrc').readlines()
                print(names[n]+'.lrc')
            except:
                lrcs = ['[00:00.00]No find the song\'s lrc file in the path...']+[]
            for lrc in lrcs:
                if lrc.find(']') != -1:
                    if len(lrc.split(']')) > 1:
                        if lrc.split(']')[1] != '\n':
                            times[n].append(lrc.split(']')[0]+']')
                            words[n].append(lrc.split(']')[1])
            words_w[n] = ['']*7 + words[n] + ['']*7

                
    def Show(ui):
        if __name__ == '__main__':
            app = QtWidgets.QApplication(sys.argv)
            Form = QtWidgets.QWidget()
            ui = ui()
            ui.setupUi(Form)
            Form.setGeometry(QRect(250, 200, 420, 714))
            animation = QPropertyAnimation(Form, b"windowOpacity")
            animation.setDuration(256)
            animation.setStartValue(0)
            animation.setEndValue(1)
            animation.start()
            Form.show()
            sys.exit(app.exec_())





Get.Names()
#print(names)
Get.Lrcs()




c = 0
def y(n):
    global c
    c = c + 1
    print('hello y!',n,c)

#打开qss文件
qss = QtCore.QFile('qss/style.qss')
qss.open(QtCore.QFile.ReadOnly)
styleSheet = qss.readAll()
styleSheet = str(styleSheet, encoding='utf8')
   
class Ui_Doco(QtWidgets.QWidget):
    def setupUi(self, Doco):
        Doco.setObjectName("Doco")
        Doco.resize(420, 714)#420, 714
        #Doco.setFixedSize(420, 714)
        Doco.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        icon = QtGui.QIcon('image/doco.ico')
        Doco.setWindowIcon(icon)
        Doco.setStyleSheet('''
            background-image:url(image/skin/1.jpg);
            color:#E8E8E8;
            font-family:黑体;
            border:none;
        ''')



        '''
        my_dir = QFileDialog.getExistingDirectory(
    self,
    "Open a folder",
    "/home/my_user_name/",
    QtGui.QFileDialog.ShowDirsOnly
    )
       '''

        ui_desklrc = self		

        self.trayIcon = QtWidgets.QSystemTrayIcon(Doco)#托盘
        self.trayIcon.setIcon(icon)
        self.trayIcon.show()
        self.trayIcon.activated.connect(Doco.showNormal)


        self.blurWidget = QtWidgets.QListWidget(Doco)
        self.blurWidget.setGeometry(QtCore.QRect(0, 0, 420, 714))
        self.blurWidget.setObjectName("blurWidget")
        self.blurWidget.setStyleSheet('''
			background:rgba(0, 0, 0, 50%);
        ''')



        self.horizontalSlider_time = QtWidgets.QSlider(Doco)
        self.horizontalSlider_time.setGeometry(QtCore.QRect(10, 630, 400, 20))
        self.horizontalSlider_time.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_time.setObjectName("horizontalSlider_time")
        self.horizontalSlider_time.setStyleSheet('''
            background:transparent;
            border:none;
        ''')

        '''
        self.label_img = QtWidgets.QLabel(Doco)
        self.label_img.setGeometry(QtCore.QRect(0, 0, 132, 132))
        self.label_img.setObjectName("label_img")
        self.label_img.setStyleSheet(''''''
        border-image:url(1.jpg);
        '''''')
        '''
        self.label_name = QtWidgets.QLabel(Doco)
        self.label_name.setGeometry(QtCore.QRect(140, 0, 271, 41))
        self.label_name.setObjectName("label_name")
        self.label_name.setStyleSheet('''
            background:transparent;
            border:none;
        ''')

        self.label_time = QtWidgets.QLabel(Doco)
        self.label_time.setGeometry(QtCore.QRect(315, 615, 95, 21))
        self.label_time.setObjectName("label_time")
        self.label_time.setStyleSheet('''
            background:transparent;
            border:none;
        ''')
        
        self.pushButton_play = QtWidgets.QPushButton(Doco,clicked=lambda:Event.play_pause(self))
        self.pushButton_play.setGeometry(QtCore.QRect(55, 680, 51, 51))
        self.pushButton_play.setObjectName("pushButton_play")
        self.pushButton_play.setStyleSheet(styleSheet)

        self.pushButton_pre = QtWidgets.QPushButton(Doco,clicked=lambda:Event.pre(self))
        self.pushButton_pre.setGeometry(QtCore.QRect(10, 680, 41, 41))
        self.pushButton_pre.setObjectName("pushButton_pre")
        self.pushButton_pre.setStyleSheet(styleSheet)

        self.pushButton_nex = QtWidgets.QPushButton(Doco,clicked=lambda:Event.nex(self))
        self.pushButton_nex.setGeometry(QtCore.QRect(95, 680, 41, 41))
        self.pushButton_nex.setObjectName("pushButton_nex")
        self.pushButton_nex.setStyleSheet(styleSheet)
        '''
        QPushButton{
	border-radius:10px;
        border-image:url(image/10.png) no-repeat;
        }
        QPushButton:hover{
	border-radius:10px;
        background:url(image/14.png) no-repeat;
        }
        '''
        
        self.pushButton_vol = QtWidgets.QPushButton(Doco,clicked=self.vol_slider)
        self.pushButton_vol.setGeometry(QtCore.QRect(180, 680, 41, 41))
        self.pushButton_vol.setObjectName("pushButton_vol")
        self.pushButton_vol.setStyleSheet(styleSheet)


        self.pushButton_way = QtWidgets.QPushButton(Doco,clicked=lambda:Event.change_way(self))
        self.pushButton_way.setGeometry(QtCore.QRect(320, 682, 28, 28))
        self.pushButton_way.setObjectName("pushButton_way")
        self.pushButton_way.setStyleSheet('''
            QPushButton{
            background:transparent;
            border-radius:5px;
            border-image:url(image/order.png) no-repeat;
            }
            QPushButton:hover{
            border-radius:5px;
            border-image:url(image/order_hover.png) no-repeat;
            }
            ''')

        self.pushButton_style = QtWidgets.QPushButton(Doco,clicked=lambda:Event.change_style(self,Doco))
        self.pushButton_style.setGeometry(QtCore.QRect(360, 90, 30, 30))
        self.pushButton_style.setObjectName("pushButton_style")
        self.pushButton_style.setStyleSheet('''
            QPushButton{
            background:#333;
            }
            QPushButton:hover{
            }
            ''')

        self.pushButton_word = QtWidgets.QPushButton(Doco,clicked=lambda:Event.show_word(self))
        self.pushButton_word.setGeometry(QtCore.QRect(250, 680, 32, 32))
        self.pushButton_word.setObjectName("pushButton_word")
        self.pushButton_word.setStyleSheet('''background:#333;''')

        self.pushButton_search = QtWidgets.QPushButton(Doco,clicked=lambda:self.show_search(Doco))
        self.pushButton_search.setGeometry(QtCore.QRect(380, 680, 32, 32))
        self.pushButton_search.setObjectName("pushButton_search")
        self.pushButton_search.setStyleSheet('''
        QPushButton{
        background:transparent;
        border-image:url(image/right.png) no-repeat;
        }
        QPushButton:hover{
        border-image:url(image/right_hover.png) no-repeat;
        }
        ''')
        
        
        self.listWidget = QtWidgets.QListWidget(Doco)
        self.listWidget.setGeometry(QtCore.QRect(0, 140, 420, 460))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget.verticalScrollBar().setSingleStep(1)#set step
        self.listWidget.setAlternatingRowColors(True);
        #self.listWidget.setVisible(False)
        self.listWidget.setStyleSheet('''
            QListWidget{
                background:transparent;
                outline:0px;
                alternate-background-color: rgba(0,0,0,2%);
            }
            QListWidget::item:selected {
                background: rgba(0,0,0,50%);
                color: #3366CC;
                border-width: 0px;
            }
            QListWidget::item:hover{
                background: rgba(0,0,0,20%);
                color: #3366cc;
            }
        ''')
        self.listWidget.verticalScrollBar().setStyleSheet('''
            QScrollBar:vertical{
                border:none;
                background: rgba(0,0,0,50%);
                width:10px;
                padding-top:0px;   
                padding-bottom:0px;
            }

            QScrollBar::handle:vertical{
                border:none;
                width:10px;
                background:rgba(0,0,0,50%);
                border-radius:5px;
                min-height:20;
            }

            QScrollBar::handle:vertical:hover{
                border:none;
                width:8px;
                background:rgba(0,0,0,30%);
                border-radius:5px;
                min-height:20;
            }

            QScrollBar::sub-line:vertical, QScrollBar::add-line:vertical {
                background: transparent;
                border-radius: 5px;
            }

            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                background: transparent;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: transparent;
                border:none;
            }
            QScrollArea {
                border:none;
                background:rgba(0,0,0,50%);
            }
        ''')

        self.lineEdit_in = QtWidgets.QLineEdit(Doco)
        self.lineEdit_in.setGeometry(QtCore.QRect(720, 20, 251, 41))#620, 20, 351, 41
        self.lineEdit_in.setObjectName("lineEdit")
        self.lineEdit_in.setPlaceholderText('歌名/歌手/专辑')
        self.lineEdit_in.installEventFilter(self)
        self.lineEdit_in.setStyleSheet('''
        border-radius:20px;
        background:#fff;
        color:#333;
        font-size:18px;
        ''')

        
        
        self.pushButton_sub = QtWidgets.QPushButton(Doco,clicked=lambda:Event.submit(self))
        self.pushButton_sub.setGeometry(QtCore.QRect(930, 21, 38, 38))
        self.pushButton_sub.setObjectName("pushButton")
        self.pushButton_sub.setStyleSheet('''
        QPushButton{
        background:#fff;
	border-radius:15px;
        border-image:url(image/sub.png) no-repeat;
        }
        QPushButton:hover{
        background:#fff;
	border-radius:15px;
        border-image:url(image/sub_hover.png) no-repeat;
        }
        ''')


        
        self.listWidget_search = QtWidgets.QListWidget(Doco)
        self.listWidget_search.setGeometry(QtCore.QRect(430, 80, 760, 620))
        self.listWidget_search.setObjectName("listWidget")
        self.listWidget_search.setVisible(False)
        self.listWidget_search.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget_search.verticalScrollBar().setSingleStep(1)
        self.listWidget_search.setStyleSheet('''
        QListWidget{
        background:transparent;
        outline:0px;
        }
        QListWidget::item:selected {
        background: rgba(0,0,0,50%);
        border-width: 0px;
        }
        QListWidget::item:hover{
        background: rgba(0,0,0,20%);
        }
        ''')
        self.listWidget_search.verticalScrollBar().setStyleSheet('''
            QScrollBar:vertical{
                border:none;
                background: rgba(0,0,0,50%);
                width:10px;
                padding-top:0px;   
                padding-bottom:0px;
            }

            QScrollBar::handle:vertical{
                border:none;
                width:10px;
                background:rgba(0,0,0,50%);
                border-radius:5px;
                min-height:20;
            }

            QScrollBar::handle:vertical:hover{
                border:none;
                width:8px;
                background:rgba(0,0,0,30%);
                border-radius:5px;
                min-height:20;
            }

            QScrollBar::sub-line:vertical, QScrollBar::add-line:vertical {
                background: transparent;
                border-radius: 5px;
            }

            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                background: transparent;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: transparent;
                border:none;
            }
            QScrollArea {
                border:none;
                background:rgba(0,0,0,50%);
            }
        ''')

        self.listWidget_word = QtWidgets.QListWidget(Doco)
        self.listWidget_word.setGeometry(QtCore.QRect(430, 80, 760, 620))
        self.listWidget_word.setObjectName("listWidget")
        self.listWidget_word.setVisible(True)
        self.listWidget_word.verticalScrollBar().setVisible(False)
        self.listWidget_word.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget_word.verticalScrollBar().setSingleStep(1)
        self.listWidget_word.setStyleSheet('''
        QListWidget{
        background:transparent;
        border:none;
        font-size:18px;
        outline:none;
        }
        

        QListWidget::item:selected {
        background: transparent;
        color:#FFF68F;
        }
        QListWidget::item:hover{
        background:transparent;
        }
        ''')

        
        #self.music_list()
        #self.search_list()

        #self.Time(10,Event.Ani)
        self.music_list()
        
        self.timer_pro = QTimer()
        self.timer_pro.timeout.connect(lambda:Event.music_pro(self))
        self.timer_pro.start(1000)

        
        self.timer_lrc = QTimer()
        self.timer_lrc.timeout.connect(lambda:Event.lrc(self))
        self.timer_lrc.start(10)

        #self.search_list()

        
        
        self.horizontalSlider_vol = QtWidgets.QSlider(Doco,valueChanged=lambda:Event.vol_drag(self))
        self.horizontalSlider_vol.setGeometry(QtCore.QRect(210, 688, 90, 19))
        self.horizontalSlider_vol.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_vol.setObjectName("verticalSlider_vol")
        self.horizontalSlider_vol.setVisible(False)
        self.horizontalSlider_vol.setValue(50)


        self.toolButton_close = QtWidgets.QToolButton(Doco,clicked=Doco.close)
        self.toolButton_close.setGeometry(QtCore.QRect(390, 0, 32, 24))
        self.toolButton_close.setObjectName("toolButton_close")
        self.toolButton_close.setStyleSheet('''
        QToolButton{
        background:transparent;
        border-image:url(image/close.png) no-repeat;
        }
        QToolButton:hover{
        border-image:url(image/close_hover.png) no-repeat;
        background:red;
        }
        ''')

        self.toolButton_min = QtWidgets.QToolButton(Doco,clicked=Doco.hide)
        self.toolButton_min.setGeometry(QtCore.QRect(360, 0, 32, 24))
        self.toolButton_min.setObjectName("toolButton_min")
        self.toolButton_min.setStyleSheet('''
        QToolButton{
        background:transparent;
        border-image:url(image/min.png) no-repeat;
        }
        QToolButton:hover{
        border-image:url(image/min_hover.png) no-repeat;
        background:#ccc;
        }
        ''')

        self.toolButton_desklrc = QtWidgets.QToolButton(Doco,clicked=self.Lrcer)
        self.toolButton_desklrc.setGeometry(QtCore.QRect(1170, 684, 32, 32))
        self.toolButton_desklrc.setObjectName("toolButton_desklrc")
        self.toolButton_desklrc.setStyleSheet('''
            background: #333;
            color: #fff;
        ''')

        


        self.retranslateUi(Doco)
        QtCore.QMetaObject.connectSlotsByName(Doco)


    def retranslateUi(self, Doco):
        _translate = QtCore.QCoreApplication.translate
        Doco.setWindowTitle(_translate("Doco", "Doco"))
        self.label_name.setText(_translate("Doco", ""))
        self.label_time.setText(_translate("Doco", ""))
        #self.pushButton_play.setText(_translate("Doco", "play"))
        #self.pushButton_pre.setText(_translate("Doco", "l"))
        #self.pushButton_nex.setText(_translate("Doco", "r"))
        #self.pushButton_vol.setText(_translate("Doco", "v"))
        #self.pushButton_way.setText(_translate("Doco", "pm"))
        #self.pushButton_search.setText(_translate("Doco", ">"))
        #self.pushButton_sub.setText(_translate("Doco", "S"))
        #self.toolButton_close.setText(_translate("Doco", "×"))
        #self.toolButton_min.setText(_translate("Doco", "-"))
        self.pushButton_word.setText(_translate("Doco", "词"))
        self.pushButton_style.setText(_translate("Doco", "S"))
        self.toolButton_desklrc.setText(_translate("Doco", "D"))

    def music_list(self):
        self.listWidget.clear()#clear list
        print(len(names))
        for n in range(0,len(names)):
            # Create QCustomQWidget
            myItemQWidget = ItemQWidget(n,self)
            myItemQWidget.setName()
            myItemQWidget.setPlay()
            myItemQWidget.setEvent(self.listWidget)
            # Create QListWidgetItem
            item = QtWidgets.QListWidgetItem(self.listWidget)
            # Set size hint
            item.setSizeHint(myItemQWidget.sizeHint())
            # Add QListWidgetItem into QListWidget
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, myItemQWidget)
            
            
            
            

    def search_list(self):
        self.listWidget_search.clear()#清空list
        for n in range(0,len(url_names)):
            # Create QCustomQWidget
            myItemQWidget = Search_QWidget(n,self)
            myItemQWidget.setName()
            myItemQWidget.setDown()
            # Create QListWidgetItem
            item = QtWidgets.QListWidgetItem(self.listWidget_search)
            # Set size hint
            item.setSizeHint(myItemQWidget.sizeHint())
            # Add QListWidgetItem into QListWidget
            self.listWidget_search.addItem(item)
            self.listWidget_search.setItemWidget(item, myItemQWidget)




    def word_list(self):
        self.listWidget_word.clear()#clear list
        for n in range(0,len(words_w[pos])):
            # Create QCustomQWidget
            myItemQWidget = Word_QWidget()
            #myItemQWidget.setWord(n)
            # Create QListWidgetItem
            item = QtWidgets.QListWidgetItem(self.listWidget_word)
            # Set size hint
            item.setSizeHint(myItemQWidget.sizeHint())
            item.setText(words_w[pos][n])
            item.setTextAlignment(Qt.AlignCenter)
            item.setSizeHint(QtCore.QSize(100,50))
            # Add QListWidgetItem into QListWidget
            self.listWidget_word.setItemWidget(item, myItemQWidget)
            

    flag_vol = False
    def vol_slider(self):
            self.horizontalSlider_vol.setVisible(not self.flag_vol)
            self.flag_vol = not self.flag_vol

    
    def show_search(self,Doco):
        global search
        if not search:
            self.pushButton_search.setStyleSheet('''
            QPushButton{
            background:transparent;
            border-image:url(image/left.png) no-repeat;
            }
            QPushButton:hover{
            border-image:url(image/left_hover.png) no-repeat;
            }
            ''')
            self.animation = QPropertyAnimation(Doco,b'geometry')#form animation
            self.animation.setDuration(200)
            self.animation.setStartValue(QRect(250, 200, 420,714))
            self.animation.setEndValue(QRect(250, 200, 1200,714))
            self.animation.start()

            self.animationx = QPropertyAnimation(self.blurWidget,b'geometry')#form animation
            self.animationx.setDuration(200)
            self.animationx.setStartValue(QRect(0, 0, 420,714))
            self.animationx.setEndValue(QRect(0, 0, 1200,714))
            self.animationx.start()

            self.animation1 = QPropertyAnimation(self.toolButton_close,b'geometry')
            self.animation1.setDuration(500)
            self.animation1.setStartValue(QRect(390, 0, 32, 24))#close animation
            self.animation1.setEndValue(QRect(1170, 0, 32, 24))
            self.animation1.start()

            self.animation2 = QPropertyAnimation(self.toolButton_min,b'geometry')
            self.animation2.setDuration(800)
            self.animation2.setStartValue(QRect(360, 0, 32, 24))#min animation
            self.animation2.setEndValue(QRect(1140, 0, 32, 24))
            self.animation2.start()


        else:
            self.pushButton_search.setStyleSheet('''
            QPushButton{
            background:transparent;
            border-image:url(image/right.png) no-repeat;
            }
            QPushButton:hover{
            border-image:url(image/right_hover.png) no-repeat;
            }
            ''')
            self.animation = QPropertyAnimation(Doco,b'geometry')
            self.animation.setDuration(200)
            self.animation.setStartValue(QRect(250, 200, 1200,714))
            self.animation.setEndValue(QRect(250, 200, 420,714))
            self.animation.start()

            self.animationx = QPropertyAnimation(self.blurWidget,b'geometry')
            self.animationx.setDuration(200)
            self.animationx.setStartValue(QRect(0, 0, 1200,714))
            self.animationx.setEndValue(QRect(0, 0, 420,714))
            self.animationx.start()

            self.animation1 = QPropertyAnimation(self.toolButton_close,b'geometry')
            self.animation1.setDuration(800)
            self.animation1.setStartValue(QRect(450, 0, 32, 24))#close animation
            self.animation1.setEndValue(QRect(390, 0, 32, 24))
            self.animation1.start()

            self.animation2 = QPropertyAnimation(self.toolButton_min,b'geometry')
            self.animation2.setDuration(500)
            self.animation2.setStartValue(QRect(420, 0, 32, 24))#min animation
            self.animation2.setEndValue(QRect(360, 0, 32, 24))
            self.animation2.start()
        
        search = not search
        #self.timer.stop()
        #self.Time(10,Event.Ani)

        
    '''
    def Time(self,t,way):
        self.timer = QTimer()
        #设置窗口计时器
        self.timer.timeout.connect(lambda:way(self))
        self.timer.start(t)
        
            
        #self.timer.stop()
    '''

    def eventFilter(self,object,event):#事件过滤器
        if object == self.lineEdit_in:
            if event.type() == QtCore.QEvent.FocusIn:
                print('in')
                self.animation = QPropertyAnimation(self.lineEdit_in,b'geometry')
                self.animation.setDuration(200)
                self.animation.setStartValue(QRect(720, 20, 251, 41))#620, 20, 351, 41
                self.animation.setEndValue(QRect(620, 20, 351, 41))
                self.animation.start()
            if event.type() == QtCore.QEvent.FocusOut:
                print('out')
                self.animation = QPropertyAnimation(self.lineEdit_in,b'geometry')
                self.animation.setDuration(200)
                self.animation.setStartValue(QRect(620, 20, 351, 41))#620, 20, 351, 41
                self.animation.setEndValue(QRect(720, 20, 251, 41))
                self.animation.start()
        return False

    def Lrcer(self,Doco):
        global words_w
        global desklrc

        if not desklrc:
            self.Form1 = QtWidgets.QWidget()
            ui = Ui_Lrcer()
            ui.setupUi(self.Form1)#显示desktop lrc
            self.Form1.show()
        else:
            self.Form1.hide()
        self.ui_desklrc = self.Form1
        desklrc = not desklrc#改变desktop桌面歌词状态

class Ui_Lrcer(object):
    def setupUi(self, Lrcer):
        Lrcer.setObjectName("Lrcer")
        #Doco.setFixedSize(420, 714)
        #Lrcer.setWindowFlags(QtCore.Qt.FramelessWindowHint)#去掉默认边框和标题栏
        Lrcer.setWindowFlags(QtCore.Qt.FramelessWindowHint |#窗口透明须设置该项
                             QtCore.Qt.SplashScreen |#同时去掉任务栏图标
                             QtCore.Qt.WindowStaysOnTopHint)#窗体总在最前
        
        Lrcer.setStyleSheet('''
            font-family:黑体;
            border:none;
        ''')

        Lrcer.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)#窗口透明，控件文本不透明

        desktop = QtWidgets.QApplication.desktop()#桌面对象
        Lrcer.setGeometry(QRect(0,desktop.height()-100,desktop.width(),100))
        Lrcer.label_desklrc = QtWidgets.QLabel(Lrcer)
        Lrcer.label_desklrc.setGeometry(QtCore.QRect(0, 32, desktop.width(), 100))
        Lrcer.label_desklrc.setObjectName("label_desklrc")
        '''
        self.label_desklrc.setVisible(True)
        self.label_desklrc.verticalScrollBar().setVisible(False)
        self.label_desklrc.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.label_desklrc.verticalScrollBar().setSingleStep(1)
        '''


        Lrcer.label_desklrc.setText('Doco Player桌面歌词.')
        Lrcer.label_desklrc.setAlignment(Qt.AlignCenter)#文本居中

        Lrcer.toolButton_clockclose = QtWidgets.QToolButton(Lrcer,clicked=lambda:Event.desklrc_clockclose(Lrcer))
        Lrcer.toolButton_clockclose.setGeometry(QtCore.QRect((desktop.width()-32)//2, 0, 20, 20))
        Lrcer.toolButton_clockclose.setObjectName("toolButton_clockclose")
        Lrcer.toolButton_clockclose.setStyleSheet('''
        QToolButton{
            background: rgba(0,0,0,0.01);
        }
        QToolButton:hover{
            border-image: url(image/clockclose_clock.png);
        }
        ''')
        Lrcer.label_desklrc.setStyleSheet('''
        QLabel{
            color: #333;
            font-size: 36px;
            border:none;
            outline:none;
            font-weight: bold;
        }
        ''')

        

class ItemQWidget(QtWidgets.QWidget):
    def __init__(self,n,ui,parent = None):
        super(ItemQWidget, self).__init__(parent)
        self.setStyleSheet('''
            border:none;
            background:transparent;
        ''')
        self.n = n
        self.ui = ui
        self.textQHBoxLayout = QtWidgets.QHBoxLayout()
        self.name            = QtWidgets.QLabel()#歌曲名
        self.play_btn        = QtWidgets.QToolButton()#播放
        #self.play_btn.setText('♫')
        self.play_btn.setStyleSheet('''
        QToolButton{
        border:none;
        background:transparent;
        border-image:url(image/play.png) no-repeat;
        }
        QToolButton:hover{
        border:none;
        border-image:url(image/play_hover.png) no-repeat;
        }
           ''')
        self.textQHBoxLayout.addWidget(self.name)
        self.textQHBoxLayout.addWidget(self.play_btn)
        self.allQHBoxLayout  = QtWidgets.QHBoxLayout()
        self.allQHBoxLayout.addLayout(self.textQHBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)

    def setName (self):
        x = names[self.n]
        if len(x)>25:
            x = x[:25]+'...'
        self.name.setText(x)

    def setPlay(self):
        self.play_btn.clicked.connect(lambda:Event().play_btn(self.n,self.ui))

    def setEvent(self,x):
        x.clicked.connect(lambda:Event().play_btn(self.n,self.ui))
    def mousePressEvent(self, e):##重载一下鼠标点击事件
        #print('clicked')
        Event().play_btn(self.n,self.ui)
    

class Search_QWidget(QtWidgets.QWidget):
    def __init__(self,n,ui,parent = None):
        super(Search_QWidget, self).__init__(parent)
        self.n = n
        self.ui = ui
        self.setStyleSheet('''
        border:none;
        background:transparent;
        ''')
        self.textQHBoxLayout = QtWidgets.QHBoxLayout()
        self.progress        = QtWidgets.QProgressBar()
        self.progress.setValue(0)
        self.progress.setFixedHeight(3)
        self.progress.setStyleSheet('''
            QProgressBar{
                
            }
        ''')
        self.name            = QtWidgets.QLabel()#歌曲名
        self.name.move(0,0)
        self.down_btn        = QtWidgets.QToolButton()#播放
        #self.down_btn.setText('↓')
        self.down_btn.setStyleSheet('''
        QToolButton{
        background:transparent;
        border-image:url(image/down.png) no-repeat;
        }
        QToolButton:hover{
        border-image:url(image/down_hover.png) no-repeat;
        }
        ''')
        self.textQHBoxLayout.addWidget(self.name)
        self.textQHBoxLayout.addWidget(self.down_btn)
        
        self.allQHBoxLayout  = QtWidgets.QVBoxLayout()
        self.allQHBoxLayout.addLayout(self.textQHBoxLayout, 1)
        self.allQHBoxLayout.addWidget(self.progress)
        self.setLayout(self.allQHBoxLayout)
        # setStyleSheet
        
    def setName (self):
        x = url_names[self.n]
        if len(x)>39:
            x = x[:39]+'...'
        self.name.setText(x)

    def setDown(self):
        self.down_btn.clicked.connect(lambda:Event().down(self.n,self.ui,self.progress))

class Word_QWidget(QtWidgets.QWidget):
    def __init__(self,parent = None):
        super(Word_QWidget, self).__init__(parent)
        self.setStyleSheet('''
        border:none;
        background:transparent;
        
        ''')
        #self.word.setAlignment(Qt.AlignCenter)      #center
        self.textQHBoxLayout = QtWidgets.QHBoxLayout()
        '''
        self.word            = QtWidgets.QLabel()   #word
        self.word.setAlignment(Qt.AlignCenter)      #center
        self.textQHBoxLayout.addWidget(self.word)
        '''
        self.allQHBoxLayout  = QtWidgets.QHBoxLayout()
        self.allQHBoxLayout.addLayout(self.textQHBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)

    '''
    def setWord (self, n):
        self.word.setText(words_w[pos][n])
    '''

class SThread(QtCore.QThread):
    strigger = pyqtSignal()
    def __init__(self,word, parent=None):
        super(SThread, self).__init__(parent)
        self.word = word
    def run(self):
        global url_names
        global mp3_urls
        global lrc_urls
        global format
        print('submit...start'+self.word)
        url_names = []
        mp3_urls = []
        format = []
        (url_names,mp3_urls,lrc_urls) = url.getKugou(self.word)
        print(len(url_names),len(mp3_urls),len(lrc_urls))
        (url_names1,mp3_urls1,lrc_urls1) = url.getQQ(self.word)
        format = format + ['mp3']*len(mp3_urls)#QQmusic 格式为m4a 酷狗为mp3
        #cache = 0#len(mp3_urls)
        format = format + ['m4a']*len(url_names1)
        url_names = url_names + url_names1
        mp3_urls = mp3_urls + mp3_urls1
        lrc_urls = lrc_urls +lrc_urls1
        print(len(url_names),len(mp3_urls),len(lrc_urls))
        print('end')

        self.strigger.emit()

class DThread(QtCore.QThread):
    dtrigger = pyqtSignal()
    def __init__(self,n,progress, parent=None):
        super(DThread, self).__init__(parent)
        self.n = n
        self.progress = progress
    def run(self):
        print('Start download...'+str(self.n))
        urllib.request.urlretrieve(mp3_urls[self.n],path+'/'+url_names[self.n]+'.'+format[self.n],self.dprogress)
        fp = open(path+'/'+url_names[self.n]+'.lrc','w')
        fp.write(lrc_urls[self.n])
        fp.close()
    
        print('Download complete')
        if not format[self.n] == 'mp3':
            print('start chang***************')
            ffmpeg.formatch('m4a',url_names[self.n])
            print('loading...')
            time.sleep(12)
            print('chang end*******************')


        self.dtrigger.emit()

    def dprogress(self,a,b,c):

        print(self.progress.value())
        '''
        self.animation_desklrc = QPropertyAnimation(self.progress,b'value')
        self.animation_desklrc.setDuration(10)
        self.animation_desklrc.setStartValue(0)
        self.animation_desklrc.setEndValue(100)
        self.animation_desklrc.start()
        '''

        per = 100.0 * a * b / c
        if per > 100:
            per = 100
        print ('%.2f%%' % per)
        self.progress.setValue(int(per))
        






'''
class Thread(QtCore.QThread):
    trigger = pyqtSignal()
    def __init__(self,word,n, parent=None):
        super(Thread, self).__init__(parent)
        self.word = word
        self.n = n
    def run(self):
        global url_names
        global mp3_urls
        global lrc_urls
        global format
        if self.n == -1:
            print('submit...start'+self.word)
            url_names = []
            mp3_urls = []
            format = []
            (url_names,mp3_urls,lrc_urls) = url.getKugou(self.word)
            print(len(url_names),len(mp3_urls),len(lrc_urls))
            (url_names1,mp3_urls1,lrc_urls1) = url.getQQ(self.word)
            format = format + ['mp3']*len(mp3_urls)#QQmusic 格式为m4a 酷狗为mp3
            #cache = 0#len(mp3_urls)
            format = format + ['m4a']*len(url_names1)
            url_names = url_names + url_names1
            mp3_urls = mp3_urls + mp3_urls1
            lrc_urls = lrc_urls +lrc_urls1
            print(len(url_names),len(mp3_urls),len(lrc_urls))
            print('end')
        elif self.n >= 0:
            print('Start download...')
            urllib.request.urlretrieve(mp3_urls[self.n],path+'/'+url_names[self.n]+'.'+format[self.n])
            fp = open(path+'/'+url_names[self.n]+'.lrc','w')
            fp.write(lrc_urls[self.n])
            fp.close()
    
            print('Download complete')
            if not format[self.n] == 'mp3':
                print('start chang***************')
                ffmpeg.formatch('m4a',url_names[self.n])
                print('loading...')
                time.sleep(12)
                print('chang end*******************')
            
        self.trigger.emit()
'''

'''
class DThread(QtCore.QThread):
    dtrigger = pyqtSignal()
    def __init__(self,n,parent=None):
        super(DThread, self).__init__(parent)
        self.n = n
    def run(self):
        print('Start download...')
        urllib.request.urlretrieve(mp3_urls[self.n],'d:/doco/'+url_names[self.n]+'.mp3')
        print('Download complete')
        ''''''
        print('DThread')
        time.sleep(5)
        ''''''
        self.dtrigger.emit()
'''
'''
class Thread2(QtCore.QThread):
    trigger2 = pyqtSignal()
    def __init__(self, parent=None):
        super(Thread2, self).__init__(parent)

    def run(self):
        print('start2')
        time.sleep(5)
        print('end2')
        self.trigger2.emit()
'''
#def p(x):
#    print(x.isRunning())
class Event():
    t = 0
    y = 0
    play_flag = False
    all_time = 300
    def play_btn(self,n,ui):
        global one
        global path                                                                  
        one = False
        pa = path+'/'+names[n]+'.mp3'
        pa = pa.encode('utf-8')
        pygame.mixer.music.load(pa)
        #print('something is wrong~\n but i see you.')
        #pygame.mixer.music.load('d:/doco/cache/1.mp3')
        #shutil.copyfile(path,'d:/doco/cache/play.mp3')
        #path = 'd:/doco/cache/play.mp3'
        #pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        
        Event.play_flag = True
        pa = path+'/'+names[n]+'.mp3'
        try:
            Event.all_time = eyed3.load(pa).info.time_secs#总时长
        except:
            Event.all_time = 300
        global pos
        pos = n
        ui.word_list()
        Event.t = 0
        Event.y = 0
    def down(self,n,ui,progress):
        print('th')
        print('self',self)
        ui.thread1 = DThread(n,progress)
        ui.thread1.start()
        ui.thread1.dtrigger.connect(lambda:Event.renovate(ui))
        print(1)
    '''
    def down(self,n):
        print('1')
        Event.nex()
        self.dthread = DThread()
        self.dthread.start()#子线程下载
        
        self.dthread.trigger1.connect(Event.nex)
    '''
        
    def submit(self):
        '''
        print('1')
        Event.nex()
        self.dthread = DThread()
        self.dthread.start()#子线程下载
        
        self.dthread.trigger1.connect(Event.nex)
        '''
        word = self.lineEdit_in.text()
        self.sthread = SThread(word)
        self.sthread.start()#search thread
        self.sthread.strigger.connect(lambda:self.search_list())#self.search_list()
        Event.show_word(self)
    def play_pause(self):
        if not pygame.mixer.music.get_busy():
            if rand:
                Event.way
            Event().play_btn(pos,self)
        else:
            if Event.play_flag:
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()
            Event.play_flag = not Event.play_flag
    def pre(self):
        global pos
        global order
        global loop
        global rand
        if rand:
            Event.way()
        else:
            pos = (pos - 1 + len(names))%(len(names))
        Event().play_btn(pos,self)

    def nex(self):
        global pos
        global order
        global loop
        global rand
        if order|rand:
            Event.way()
        else:
            pos = (pos + 1)%(len(names))
        Event().play_btn(pos,self)
    x = 0
    def music_pro(self):
        global pos
        global order
        global loop
        global rand
        play_time = pygame.mixer.music.get_pos()//1000
        if play_time < 0:
            play_time = 0
        self.horizontalSlider_time.setValue(play_time/Event.all_time*100)#进度条
        self.label_time.setText(Event.str_time(play_time)+'/'+Event.str_time(Event.all_time))
        self.label_name.setText(names[pos])
        self.listWidget.setCurrentRow(pos)#改变item标点  
        #print(one)
        if not (pygame.mixer.music.get_busy() | one):
            Event.way()
            Event().play_btn(pos,self)

        if  Event.play_flag:#play ss
            self.pushButton_play.setStyleSheet('''
            QPushButton#pushButton_play{
            border:none;
            background:url(image/3.png) no-repeat;
            }
            QPushButton#pushButton_play:hover{
            border:none;
            background:url(image/4.png) no-repeat;
            }
                                               '''       
                                               )
        else:
            self.pushButton_play.setStyleSheet(styleSheet)
        
        


        
    '''
    def Ani(self):
        global count
        count = count + 1
        Event.music_pro(self)
        if count == 1:
            self.timer.stop()
            self.Time(1000,Event.music_pro)
            count = 0
        Get.Names()
        self.music_list()
        self.search_list()
    '''

    '''
    def music_drag(self):
        self.timer.stop()
        pygame.mixer.music.set_pos(self.horizontalSlider_time.value()/100*Event.all_time)   
    '''
    
    def renovate(self):
        Get.Names()
        Get.Lrcs()
        self.music_list()

    def way():
        global pos
        global order
        global loop
        global rand
        if order:
            pos = (pos + 1)%len(names)#order
        elif loop:                    #loop
            pass
        elif rand:                    #rand
            pos = random.randint(0,len(names)-1)
    
    def vol_drag(self):
        pygame.mixer.music.set_volume(self.horizontalSlider_vol.value()/100)
        #print(self.verticalSlider_vol.value()/100)

        if self.horizontalSlider_vol.value()>=60:
           self.pushButton_vol.setStyleSheet(
            '''
            QPushButton{
            border:none;
            background:url(image/11.png) no-repeat;
            }
            QPushButton:hover{
            border:none;
            background:url(image/15.png) no-repeat;
            }
            ''')
        elif self.horizontalSlider_vol.value()>=20:
             self.pushButton_vol.setStyleSheet(
             '''
             QPushButton{
             border:none;
             background:url(image/10.png) no-repeat;
             }
             QPushButton:hover{
             border:none;
             background:url(image/14.png) no-repeat;
             }
             ''')
        elif self.horizontalSlider_vol.value()>0:
             self.pushButton_vol.setStyleSheet(
             '''
             QPushButton{
             border:none;
             background:url(image/9.png) no-repeat;
             }
             QPushButton:hover{
             border:none;
             background:url(image/13.png) no-repeat;
             }
             ''')
        elif self.horizontalSlider_vol.value()==0:
             self.pushButton_vol.setStyleSheet(
             '''
             QPushButton{
             border:none;
             background:url(image/12.png) no-repeat;
             }
             QPushButton:hover{
             border:none;
             background:url(image/16.png) no-repeat;
             }
             ''')
    word_exit = True
    def show_word(self):
        self.listWidget_word.setVisible(not Event.word_exit)
        self.listWidget_search.setVisible(Event.word_exit)
        Event.word_exit = not Event.word_exit

    
    
    def change_way(self):
        global order
        global loop
        global rand
        if order:
            order = False
            loop = True
            self.pushButton_way.setStyleSheet('''
            QPushButton{
            background:transparent;
            border-radius:5px;
            border-image:url(image/loop.png) no-repeat;
            }
            QPushButton:hover{
            border-radius:5px;
            border-image:url(image/loop_hover.png) no-repeat;
            }
            ''')
        elif loop:
            loop = False
            rand = True
            self.pushButton_way.setStyleSheet('''
            QPushButton{
            background:transparent;
            border-radius:5px;
            border-image:url(image/rand.png) no-repeat;
            }
            QPushButton:hover{
            border-radius:5px;
            border-image:url(image/rand_hover.png) no-repeat;
            }
            ''')
        else:
            rand = False
            order = True
            self.pushButton_way.setStyleSheet('''
            QPushButton{
            background:transparent;
            border-radius:5px;
            border-image:url(image/order.png) no-repeat;
            }
            QPushButton:hover{
            border-radius:5px;
            border-image:url(image/order_hover.png) no-repeat;
            }
            ''')
    c = 2
    def change_style(self,Doco):
        if not os.path.isfile('''image/skin/'''+str(Event.c)+'''.jpg'''):
            Event.c = 1

        self.animation_img = QPropertyAnimation(Doco,b'windowOpacity')
        self.animation_img.setDuration(800)
        self.animation_img.setStartValue(1)
        self.animation_img.setEndValue(0.6)
        self.animation_img.start()

        Doco.setStyleSheet('''
            background:transparent;
            background-image:url(image/skin/'''+str(Event.c)+'''.jpg);
            color:#E8E8E8;
            font-family:黑体;
            border:none;
        ''')

        self.animation_img = QPropertyAnimation(Doco,b'windowOpacity')
        self.animation_img.setDuration(800)
        self.animation_img.setStartValue(0.6)
        self.animation_img.setEndValue(1)
        self.animation_img.start()
            
        
        Event.c = Event.c + 1
            

    '''
    def show_search(self,Doco):
        global search
        
        if not search:
            Doco.resize(1200, 714)#420, 714
            Doco.setFixedSize(1200, 714)
        else:
            Doco.resize(420, 714)#420, 714
            Doco.setFixedSize(420, 714)
    


        
        #Event.renovate(self)
        search = not search
    '''
        
    def str_time(time):#格式化时间
        return str(time//60//10)+str(time//60%10)+':'+str(time%60//10)+str(time%60%10)


    def ms_time(time):
        m = int(time.strip('[]')[:2])
        s = int(time.strip('[]')[3:][:2])
        ms = int(time.strip('[]')[6:])
        return m*60*1000+s*1000+ms


    
    def lrc(self):
        if pygame.mixer.music.get_busy():
            '''
            if pygame.mixer.music.get_pos()>Event.ms_time(times[Event.t]):
                print('++')
                Event.t = Event.t + 1
            '''
            if (Event.t<len(times[pos])):
                if(pygame.mixer.music.get_pos() >= Event.ms_time(times[pos][Event.t])):
                   Event.t = Event.t + 1

                   self.animation_word = QPropertyAnimation(self.listWidget_word.verticalScrollBar(),b'value')
                   self.animation_word.setDuration(200)
                   self.animation_word.setStartValue(Event.y)#min animation
                   self.animation_word.setEndValue(Event.y+50)
                   self.animation_word.start()

                   Event.y = Event.y + 50
                   self.listWidget_word.setCurrentRow(Event.t+6)

                   if desklrc:
                       Event.desklrc(self,self.ui_desklrc)

    def desklrc(self,ui):
        
        self.animation_desklrc = QPropertyAnimation(ui,b'windowOpacity')
        self.animation_desklrc.setDuration(600)
        self.animation_desklrc.setStartValue(1)
        self.animation_desklrc.setEndValue(0)
        self.animation_desklrc.start()

        ui.label_desklrc.setText(words_w[pos][Event.t+6])

        self.animation_desklrc = QPropertyAnimation(ui,b'windowOpacity')
        self.animation_desklrc.setDuration(600)
        self.animation_desklrc.setStartValue(0)
        self.animation_desklrc.setEndValue(1)
        self.animation_desklrc.start()
    desklrc_clock = True
    def desklrc_clockclose(self):
        if Event.desklrc_clock:
            self.toolButton_clockclose.setStyleSheet('''
                QToolButton{
                    background: rgba(0,0,0,0.01);
                }
                QToolButton:hover{
                    border-image: url(image/clockclose_close.png);
                }
            ''')
        else:
            global desklrc
            self.hide()
            desklrc = not desklrc
        Event.desklrc_clock = not Event.desklrc_clock



Get.Show(Ui_Doco)



'''       
if __name__ == '__main__':   
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Doco()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
'''
