from PyQt5 import QtCore, QtGui, QtWidgets
import json

n = 0


class Ui_CheQuiz(object):

    def setupUi(self, CheQuiz):
        CheQuiz.setObjectName("CheQuiz")
        CheQuiz.setFixedSize(842, 498)
        CheQuiz.setDocumentMode(False)
        CheQuiz.setTabShape(QtWidgets.QTabWidget.Rounded)
        
        self.centralwidget = QtWidgets.QWidget(CheQuiz)
        self.centralwidget.setObjectName("centralwidget")
        #self.centralwidget.setStyleSheet("background-color:#f0f5f5; border-radius:0px")
        
        self.question = QtWidgets.QLabel(self.centralwidget)
        self.question.setGeometry(QtCore.QRect(6, 0, 831, 141))
        self.question.setAlignment(QtCore.Qt.AlignCenter)
        self.question.setWordWrap(False)
        self.question.setObjectName("question")
        self.question.setFont(QtGui.QFont("Garamond Bold", 16))
        self.question.setWordWrap(True)
        #self.question.setStyleSheet("background-color:#f2f2f2; border-radius:5px")
        
        self.answer = QtWidgets.QLabel(self.centralwidget)
        self.answer.setGeometry(QtCore.QRect(6, 310, 831, 141))
        self.answer.setAlignment(QtCore.Qt.AlignCenter)
        self.answer.setObjectName("answer")
        self.answer.setFont(QtGui.QFont("Garamond Bold", 16))
        self.answer.setWordWrap(True)
        #self.answer.setStyleSheet("background-color:#f2f2f2; border-radius:5px")
        
        self.previous = QtWidgets.QPushButton(self.centralwidget)
        self.previous.setGeometry(QtCore.QRect(10, 190, 151, 71))
        self.previous.setObjectName("previous")
        self.previous.clicked.connect(self.previous_question)
        self.previous.setFont(QtGui.QFont("Candara", 14))
        
        self.show_answer = QtWidgets.QPushButton(self.centralwidget)
        self.show_answer.setGeometry(QtCore.QRect(340, 190, 151, 71))
        self.show_answer.setObjectName("show_answer")
        self.show_answer.setFont(QtGui.QFont("Candara", 14))
        self.show_answer.clicked.connect(self.reveal_answer)
        
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(680, 190, 151, 71))
        self.next.setObjectName("next")
        self.next.clicked.connect(self.next_question)
        self.next.setFont(QtGui.QFont("Candara", 14))
        
        self.bottom_line = QtWidgets.QFrame(self.centralwidget)
        self.bottom_line.setGeometry(QtCore.QRect(0, 300, 841, 20))
        self.bottom_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.bottom_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.bottom_line.setObjectName("bottom_line")
        
        self.top_line = QtWidgets.QFrame(self.centralwidget)
        self.top_line.setGeometry(QtCore.QRect(0, 130, 841, 21))
        self.top_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.top_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.top_line.setObjectName("top_line")
        
        CheQuiz.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(CheQuiz)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 842, 21))
        self.menubar.setObjectName("menubar")
        
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        
        CheQuiz.setMenuBar(self.menubar)
        
        self.menuOpen = QtWidgets.QAction("Open", triggered=self.open_json)
        self.menuOpen.setObjectName("menuOpen")
        
        self.menuQuit = QtWidgets.QAction("Exit", triggered=self.quit_button)
        self.menuQuit.setObjectName("menuQuit")
        
        #self.statusbar = QtWidgets.QStatusBar(CheQuiz)
        #self.statusbar.setObjectName("statusbar")
        
        #CheQuiz.setStatusBar(self.statusbar)
        
        self.menubar.addAction(self.menuMain.menuAction())
        self.menuMain.addAction(self.menuOpen)
        self.menuMain.addAction(self.menuQuit)

        self.retranslateUi(CheQuiz)
        
        QtCore.QMetaObject.connectSlotsByName(CheQuiz)

    def retranslateUi(self, CheQuiz):
        _translate = QtCore.QCoreApplication.translate
        
        CheQuiz.setWindowTitle(_translate("CheQuiz", "Check Quiz"))
        self.question.setText(_translate("CheQuiz", "Question"))
        self.answer.setText(_translate("CheQuiz", "Answer?"))
        self.previous.setText(_translate("CheQuiz", "Previous"))
        self.show_answer.setText(_translate("CheQuiz", "Reveal answer"))
        self.next.setText(_translate("CheQuiz", "Next"))
        self.menuMain.setTitle(_translate("CheQuiz", "Main"))
    
    def quit_button(self):
        CheQuiz.close()
        
    def open_file(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(None, "Open JSON File", "", "JSON Files (*.json)")[0]
        data = json.loads(open(str(file_name), encoding='utf-8').read())
        return data
        
    def open_json(self, CheQuiz):
        global questions
        global answers
        
        #file_name = QtWidgets.QFileDialog.getOpenFileName(None, "Open JSON File", "", "JSON Files (*.json)")[0]
        #json_file = json.loads(open(str(file_name), encoding='utf-8').read())
        try:
            json_file = self.open_file()
            questions = list(json_file.keys())
            answers = list(json_file.values())
            self.question.setText(questions[n])
            self.answer.setText("Answer?")
            return questions, answers
        except (FileNotFoundError, AttributeError):
            pass
   
    def next_question(self, CheQuiz):
        global n
        try:
            for index in range(1):
                if n <= len(questions)-2:
                    n += 1
                    self.question.setText(questions[n])
                    self.answer.setText("Answer?")
                elif n == len(questions)-1:
                    print("Finish")
        except IndexError:
            return
        except NameError:
            self.question.setText("Choose JSON file!")


    def previous_question(self, CheQuiz):
        global n
        try:
            for index in range(1):
                if n > 0 and n <= len(questions):
                    n -= 1
                    self.question.setText(questions[n])
                    self.answer.setText("Answer?")
                elif n == 0:
                    self.question.setText(questions[n])
                    self.answer.setText("Answer?")
                    print("It's beggining")
        except IndexError:
            return
        except NameError:
            self.question.setText("Choose JSON file!")
    
    def reveal_answer(self, Chequiz):
        try:
            self.answer.setText(answers[n])
        except NameError:
            pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CheQuiz = QtWidgets.QMainWindow()
    ui = Ui_CheQuiz()
    ui.setupUi(CheQuiz)
    CheQuiz.show()
    sys.exit(app.exec_())
