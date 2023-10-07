import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget
from PyQt6.QtWidgets import QTextBrowser, QHBoxLayout, QVBoxLayout
from PyQt6.QtWidgets import QGroupBox, QRadioButton, QProgressBar
from PyQt6 import QtCore
from PyQt6 import QtGui
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput

class QuizWindow(QMainWindow):
    
    def __init__(self) -> None:
        super().__init__()
        self.setUpUi()
        self.varA.toggled.connect(self.setPlaySound)
        self.strtBtn.clicked.connect(self.start_btn)
        
    def start_btn(self):
        self.timer.start()
        
    def setUpUi(self):
        self.timesOne = 30
        self.setUp()
        self.setUpTwo()
        self.setSoundSetting()
        self.setMyTimer()
        
    def setMyTimer(self):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(30*100)
        self.timer.timeout.connect(self.timer_out)
    
    def timer_out(self):
        if self.media.isAvailable():
            self.media.stop()
        self.media.setSource(QtCore.QUrl.fromLocalFile("./musics/timeout.mp3"))
        self.media.play()
        print('AA')
        
    
    def setSoundSetting(self):
        self.media = QMediaPlayer()
        self.audioOut = QAudioOutput(self)
        self.media.setAudioOutput(self.audioOut)
        self.media.setSource(QtCore.QUrl.fromLocalFile("./musics/donate.mp3"))
    
    def setPlaySound(self):
        if self.media.isAvailable():
            self.media.stop()
            self.media.play()
        else:
            self.media.play()
                        
    def setUp(self):
        self.setWindowIcon(QtGui.QIcon("./icons/quiz.png"))
        self.setWindowTitle("Main Window")
        w = QApplication.primaryScreen().size().width()
        h = QApplication.primaryScreen().size().height()
        w_w = max(w,h) // 3
        w_h = max(w,h) // 3
        self.setGeometry(w//2 - w_w//2, h //2 - w_h //2, w_w, w_h)

        self.quBrowser = QTextBrowser()
        self.quBrowser.setMaximumHeight((w_h*20)//100)
        self.qLayout = QHBoxLayout()
        self.qLayout.addWidget(self.quBrowser,QtCore.Qt.AlignmentFlag.AlignTop)
        
        self.qVar = QGroupBox()
        self.qVar.setTitle(" ")
        self.varA = QRadioButton("A")
        self.varB = QRadioButton("B")
        self.varC = QRadioButton("C")
        self.varD = QRadioButton("D")
    
        self.varLayout = QVBoxLayout()
        self.varLayout.addWidget(self.varA)
        self.varLayout.addWidget(self.varB)
        self.varLayout.addWidget(self.varC)
        self.varLayout.addWidget(self.varD)
        self.qVar.setLayout(self.varLayout)
    
    def setUpTwo(self):
        #
        self.prvBnt = QPushButton("Prev")
        self.prvBnt.setMinimumHeight(35)
        self.nxtBtn = QPushButton("Next")
        self.nxtBtn.setMinimumHeight(35)
        self.strtBtn = QPushButton("start")
        self.strtBtn.setMinimumHeight(35)
        self.btnLayout = QHBoxLayout()
        self.btnLayout.addWidget(self.prvBnt)
        self.btnLayout.addWidget(self.strtBtn)
        self.btnLayout.addWidget(self.nxtBtn)
        #
        self.tmrProgres = QProgressBar()
        self.tmrProgres.setValue(100)
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.qLayout)
        self.mainLayout.addWidget(self.qVar)
        self.mainLayout.addLayout(self.btnLayout)
        self.mainLayout.addWidget(self.tmrProgres)
        self.centr = QWidget(self)
        self.centr.setLayout(self.mainLayout)
        self.setCentralWidget(self.centr)
        
        

if __name__ == "__main__":
    app = QApplication([])
    sg = QuizWindow()
    sg.show()
    exit(app.exec())