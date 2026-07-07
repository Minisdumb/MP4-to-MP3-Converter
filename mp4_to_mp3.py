
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton , QApplication, QFileDialog
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
)

import sys, proglog
from moviepy import *

class MyLogger(proglog.ProgressBarLogger):
    def bars_callback(self, bar, attr, value, old_value=None):
        if attr == "index":
            total = self.bars[bar]["total"]
            percent = value / total
            print(percent)  # 0.0–1.0


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        screen = self.screen()
        self.screensize = screen.size()
        self.title = 'MP4 to MP3 Converter'
        self.left = int(self.screensize.width()) / 2.5
        self.top = int(self.screensize.height()) / 2.5
        self.width = 440
        self.height = 280
        self.initUI()
        self.Mylogger = None
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(int(self.left), int(self.top), self.width, self.height)
        self.lable = QLabel("Put in the path for the MP4 file:", self)
        self.lable.setGeometry(50, 10, 300, 30)
        self.lable.move(10, 10)
        self.inputi = QLineEdit(self)
        self.inputi.setFixedSize(QSize(300,30))
        self.inputi.move(10, 50)
        self.brow = QPushButton("Browse File", self)
        self.brow.move(310, 50)
        self.brow.setFixedSize(QSize(125,30))
        self.convertio = QPushButton("Convert to MP3", self)
        self.convertio.move(60, 175)
        self.convertio.setFixedSize(QSize(300,50))
        self.lelabel = QLabel("Name for the output file:", self,)
        self.lelabel.setGeometry(10, 100, 200, 30)
        self.lelabel.move(10, 100)
        self.inputiiii = QLineEdit(self)
        self.inputiiii.move(10, 130)
        self.inputiiii.setFixedSize(QSize(200,30))
        self.progress = QProgressBar(self)
        self.progress.setGeometry(10, 150, 420, 30)
        self.progress.move(30, 240)
        self.progress.hide()   
        self.convertio.clicked.connect(self.on_button_clicked)
        self.brow.clicked.connect(self.browsefiles)
        self.show()

    def browsefiles(self):
        fname=QFileDialog.getOpenFileName()
        self.inputi.setText(fname[0])
    
    


        
    def on_button_clicked(self):
        printable = True
        path = self.inputi.text()
        path2 = self.inputiiii.text()
        if path == "" or path2 == "":
            self.lable.setText("Please enter the path for the MP4 file and the output file name.")
            printable = False
        else:
            printable = True
            self.lable.setText("Conversion in progress...")
        

                    
        if printable:
            self.progress.show()
            self.progress.setValue(0)
            
            video = VideoFileClip(path)
            audiofile = video.audio.write_audiofile(path2+".mp3",logger="bar")
            self.progress.setValue(100) 
    
        
       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())