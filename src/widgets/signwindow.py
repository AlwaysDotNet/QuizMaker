import typing
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QRadioButton
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt6 import QtCore
from PyQt6 import QtGui
from PyQt6.QtWidgets import QLabel

class SignInWindow(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        self.setUp()
        self.setStyleSheets()
        self.setMyFont()
        
    
    def setMyFont(self):
        fn = QtGui.QFont("Times New Roman", 12, 2)
        self.emlEdit.setFont(fn)
        self.passworEdit.setFont(fn)
        self.sInBtn.setFont(fn)
        self.sUpbtn.setFont(fn)
    
    def setUp(self):
        self.setWindowIcon(QtGui.QIcon("./icons/quiz.png"))
        self.setWindowTitle("Sign In")
        w = QApplication.primaryScreen().size().width()
        h = QApplication.primaryScreen().size().height()
        w_w = max(w,h) // 4
        w_h = max(w,h) // 4
        self.setGeometry(w//2 - w_w//2, h //2 - w_h //2, w_w, w_h)
        #Asosiy widgetlar
        self.logoLbl = QLabel()
        self.logoLbl.setMinimumSize(w_w // 4, w_h // 4)
        self.logoLbl.setMaximumSize(w_w//2, w_h//2)
        self.logoLbl.setPixmap(QtGui.QPixmap("./icons/logo.png"))
        self.logoLbl.setScaledContents(True)
        
        self.logLayout = QHBoxLayout()
        self.logLayout.addStretch(2)
        self.logLayout.addWidget(self.logoLbl)
        self.logLayout.addStretch(2)
        #
        self.emlEdit = QLineEdit()
        self.emlEdit.setMinimumSize(200, 35)
        self.passworEdit= QLineEdit()
        self.passworEdit.setMinimumSize(200,35)
        #
        self.edtLayout = QVBoxLayout()
        self.edtLayout.addWidget(self.emlEdit)
        self.edtLayout.addWidget(self.passworEdit)
        #
        self.sInBtn = QPushButton("Sign In")
        self.sInBtn.setMinimumHeight(35)
        self.sUpbtn = QPushButton("Sign Up")
        self.sUpbtn.setMinimumHeight(35)
        #ButtonLayout
        self.btnLayout = QHBoxLayout()
        self.btnLayout.addWidget(self.sInBtn)
        self.btnLayout.addWidget(self.sUpbtn)
        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.addLayout(self.logLayout)
        self.mainLayout.addLayout(self.edtLayout)
        self.mainLayout.addLayout(self.btnLayout)
        #Widget Layout
        self.setLayout(self.mainLayout)
    
    def setStyleSheets(self):
        
        qbut_css = """
        QPushButton{
         border: 2px solid #8f8f91;
        border-radius: 6px;
        background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #f6f7fa, stop: 1 #dadbde);
        min-width: 80px;}

        QPushButton:hover {
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}
        QLineEdit { 
                         border-radius: 4px; 
                         color:rgb(0, 0, 0); 
                         background-color:rgb(255, 255, 255); 
                   }

                         QLineEdit:focus { 
                         border-style:outset;
                         border-width:4px;
                         border-radius: 4px;
                         border-color: rgb(41, 237, 215);
                         color:rgb(0, 0, 0);
                         background-color: rgb(150, 150, 150); 
                         }
        """   
        self.setStyleSheet(qbut_css)
    