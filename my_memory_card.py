from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory card')
qestion = QLabel("Какой национальности не сущеcтвует?")
RadioGroupBox = QGroupBox("Варианты ответов")
BtnOK = QPushButton("Ответить")

btn_answer1 = QRadioButton('Энцы')
btn_answer2 = QRadioButton('Чумымцы')
btn_answer3 = QRadioButton('Смурфы')
btn_answer4 = QRadioButton('Алеуты')

layout_ans4 = QVBoxLayout()
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans4.addWidget(qestion, alignment=Qt.AlignTop)
layout_ans2.addWidget(btn_answer1)
layout_ans2.addWidget(btn_answer2)
layout_ans3.addWidget(btn_answer3)
layout_ans3.addWidget(btn_answer4)
layout_ans4.addWidget(BtnOK, alignment=Qt.AlignLeft)



class Question():
    def __init__(
        self, qestion, right_answer,
        wrong1, wrong2, wrong3):
            self.qestion=qestion
            self.right_answer=right_answer
            self.wrong1=wrong1
            self.wrong2=wrong2
            self.wrong3=wrong3

def click_BtnOK():
    if BtnOK.text() =='Ответить':
        check_answer()
    else:
        next_question()

def check_answer():
    if btn_answer1.clicked:
        print("true")
    else:
        print("jgvghvgv ")
    
    
def next_question():
    window.cur_question = window.cur_question + 1
    if window.cur_question >=len(qestion_list):
        window.cur_question = 0
    q = questions_list[window.cur_question]
    ask(q)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans4)
layout_ans1.addLayout(layout_ans3)

layout_ans3.setSpacing(10)
RadioGroupBox.setLayout(layout_ans1)

main_win.setLayout(layout_ans1)
BtnOK.clicked.connect(click_BtnOK)
main_win.show()
main_win.resize(400,300)
app.exec_()