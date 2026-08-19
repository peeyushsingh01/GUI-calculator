import sys
from PySide6.QtWidgets import QApplication,QWidget,QLineEdit,QPushButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize,QTimer
app = QApplication(sys.argv)

#window
window = QWidget()
window.setWindowTitle("calculator")
window.setFixedSize(800,500)
window.setStyleSheet("""
           background-color: #D3D3D3;
""")

#display
display = QLineEdit(window)
display.setGeometry(250,20,300,50)
display.setText("0")
display.setReadOnly(True)
display.setStyleSheet("""
      background-color:grey;
      color: black;
      font-size :24px;
      border: 2px solid black ;
""")

#buttons

#numbers
b7 = QPushButton("7",window)
b7.setGeometry(250,130,50,50)
b7.setStyleSheet("""
         background-color: white;
         color : black ;
         font-size : 24px;
         border : 3px solid black;
""")

b8 = QPushButton("8",window)
b8.setGeometry(310,130,50,50)
b8.setStyleSheet("""
         background-color: white;
         color : black ;
         font-size : 24px;
         border : 3px solid black;
""")

b9 = QPushButton("9",window)
b9.setGeometry(370,130,50,50)
b9.setStyleSheet("""
         background-color: white;
         color : black ;
         font-size : 24px;
         border : 3px solid black;
""")

b4 = QPushButton("4",window)
b4.setGeometry(250,190,50,50)
b4.setStyleSheet("""
         background-color: white;
         color : black ;
         font-size : 24px;
         border : 3px solid black;
""")

b5 = QPushButton("5",window)
b5.setGeometry(310,190,50,50)
b5.setStyleSheet("""
         background-color: white;
         color : black ;
         font-size : 24px;
         border : 3px solid black;
""")

b6 = QPushButton("6",window)
b6.setGeometry(370,190,50,50)
b6.setStyleSheet("""
         background-color: white;
         color : black ;
         font-size : 24px;
         border : 3px solid black;
""")

b1 = QPushButton("1",window)
b1.setGeometry(250,250,50,50)
b1.setStyleSheet("""
         background-color: white;
         color : black ;
         font-size : 24px;
         border : 3px solid black;
""")

b2 = QPushButton("2",window)
b2.setGeometry(310,250,50,50)
b2.setStyleSheet("""
         background-color: white;
         color : black ;
         font-size : 24px;
         border : 3px solid black;
""")

b3 = QPushButton("3",window)
b3.setGeometry(370,250,50,50)
b3.setStyleSheet("""
         background-color: white;
         color : black ;
         font-size : 24px;
         border : 3px solid black;
""")

b0 = QPushButton("0",window)
b0.setGeometry(310,310,50,50)
b0.setStyleSheet("""
         background-color: white;
         color : black ;
         font-size : 24px;
         border : 3px solid black;
""")

#operations

b_dot = QPushButton(".",window)
b_dot.setGeometry(250,310,50,50)
b_dot.setStyleSheet("""
         background-color: #ADD8E6;
         color : black ;
         font-size : 30px;
         border : 3px solid black;
""")

b_bs = QPushButton(window)
b_bs.setGeometry(370,310,50,50)
b_bs.setIcon(QIcon("bs.png"))
b_bs.setIconSize(QSize(30,30))
b_bs.setStyleSheet("""
      background-color : red;
      border : 3px solid black ;
""")

b_p = QPushButton("+",window)
b_p.setGeometry(450,130,50,50)
b_p.setStyleSheet("""
         background-color: white;
         color : black ;
         font-size : 24px;
         border : 3px solid black;
""")

b_s = QPushButton("-",window)
b_s.setGeometry(450,190,50,50)
b_s.setStyleSheet("""
         background-color: white;
         color : black ;
         font-size : 24px;
         border : 3px solid black;
""")

b_m = QPushButton("x",window)
b_m.setGeometry(450,250,50,50)
b_m.setStyleSheet("""
         background-color: white;
         color : black ;
         font-size : 24px;
         border : 3px solid black;
""")

b_d = QPushButton("/",window)
b_d.setGeometry(450,310,50,50)
b_d.setStyleSheet("""
         background-color: white;
         color : black ;
         font-size : 24px;
         border : 3px solid black;
""")

b_c = QPushButton("C",window)
b_c.setGeometry(510,130,40,50)
b_c.setStyleSheet("""
         background-color: #E0115F;
         color : black ;
         font-size : 24px;
         border : 3px solid black;
""")

b_e = QPushButton("=",window)
b_e.setGeometry(510,190,40,170)
b_e.setStyleSheet("""
         background-color: #5B7C99;
         color : black ;
         font-size : 24px;
         border : 3px solid black;
""")

window.show()
textOnDisplay = ""
operator = ""
n1 = ""
n2 = ""
df = "1" #deciding factor


#button functions
#numbers_except_0
def cac(a):
    global n1
    global n2
    global textOnDisplay
    if df == "1":
        n1 = n1+ a
        textOnDisplay = n1 + operator + n2
        display.setText(textOnDisplay)
    elif df == "2":
        n2 = n2 +a
        textOnDisplay = n1 + operator + n2
        display.setText(textOnDisplay)

def cacd():
    global n1
    global n2
    global textOnDisplay
    if df == "1":
        if "." not in n1 :
            if any(c in n1 for c in "123456789"):
                n1 = n1 + "."
                textOnDisplay = n1 + operator + n2
                display.setText(textOnDisplay)
            elif n1 =="-":
                n1 = "-0."
                textOnDisplay = n1 + operator + n2
                display.setText(textOnDisplay)
            else:
                n1 = "0."
                textOnDisplay = n1 + operator + n2
                display.setText(textOnDisplay)
    elif df == "2":

            if "." not in n2:
                if any(c in n2 for c in "123456789"):
                    n2 = n2 + "."
                    textOnDisplay = n1 + operator + n2
                    display.setText(textOnDisplay)
                else:
                    n2 = "0."
                    textOnDisplay = n1 + operator + n2
                    display.setText(textOnDisplay)


#0
def caco():
    global n1
    global n2
    global textOnDisplay
    if df == "1":
        if len(n1) > 0:

            n1 = n1 + "0"
            textOnDisplay = n1 + operator + n2
            display.setText(textOnDisplay)
    elif df == "2":
        n2 = n2 + "0"
        textOnDisplay = n1 + operator + n2
        display.setText(textOnDisplay)



def equal():
    global n1
    global n2
    global textOnDisplay
    global operator
    global df
    if n1 == "":
        display.setText("0")

    elif n2 == "" and n1 !="" :
        textOnDisplay= n1 + operator + n2
        display.setText(textOnDisplay)
    else:
        r = float(n1)
        s = float(n2)
        if operator == "+":
            q = r + s
            n1 = str(q)
            n2 = ""
            operator = ""
            textOnDisplay = n1 + operator + n2
            display.setText(textOnDisplay)
            df = "1"
        elif operator == "-":
            q = r - s
            n1 = str(q)
            n2 = ""
            operator = ""
            textOnDisplay = n1 + operator + n2
            display.setText(textOnDisplay)
            df = "1"
        elif operator == "x":
            q = r * s
            n1 = str(q)
            n2 = ""
            operator = ""
            textOnDisplay = n1 + operator + n2
            display.setText(textOnDisplay)
            df = "1"
        elif operator == "/":
            if s == 0:
                display.setText("ERROR!!!")
                df = "1"
                n1=""
                n2=""
                operator= ""
                QTimer.singleShot(650,clear)
            else:
                q = r / s
                n1 = str(q)
                n2 = ""
                operator = ""
                textOnDisplay = n1 + operator + n2
                df = "1"
                display.setText(textOnDisplay)

#operations
def opr(x):
    global operator
    global df
    global textOnDisplay
    global n2
    if df == "1":
       if n1 != "" and n1 !="-" :
           operator = x
           df = "2"
           textOnDisplay = n1 + operator + n2
           display.setText(textOnDisplay)
    elif df == "2":
        if n2 == "":
            operator = x
            textOnDisplay = n1 + operator + n2
            display.setText(textOnDisplay)
        else:
            equal()
            operator = x
            df = "2"
            textOnDisplay = n1 + operator + n2
            display.setText(textOnDisplay)

def oprs():
    global operator
    global df
    global n2
    global textOnDisplay
    global n1
    if df =="1":
        if n1 == "":
            n1 = "-"
            textOnDisplay = n1 + operator + n2
            display.setText(textOnDisplay)
        elif n1 != "" and n1 != "-":
            operator = "-"
            df = "2"
            textOnDisplay = n1 + operator + n2
            display.setText(textOnDisplay)
    elif df =="2":
       if n2 =="":
           operator = "-"
           textOnDisplay = n1 + operator + n2
           display.setText(textOnDisplay)
       else:
           equal()
           operator = "-"
           df = "2"
           textOnDisplay = n1 + operator + n2
           display.setText(textOnDisplay)






def backspace():
    global df
    global n1
    global n2
    global textOnDisplay
    global operator
    if df =="1":
        n1 = n1[:len(n1)-1]
    elif df =="2":
        if n2 == "":
            df = "1"
            operator = ""
        else:
            n2 = n2[:len(n2) - 1]
    textOnDisplay = n1 + operator + n2
    if textOnDisplay == "":
        display.setText("0")
    else:
        display.setText(textOnDisplay)

def clear():
    global n1
    global n2
    global operator
    global df
    n2 = ""
    n1 = ""
    operator = ""
    df = "1"
    display.setText("0")



b0.clicked.connect(caco)
b1.clicked.connect(lambda:cac("1"))
b2.clicked.connect(lambda:cac("2"))
b3.clicked.connect(lambda:cac("3"))
b4.clicked.connect(lambda:cac("4"))
b5.clicked.connect(lambda:cac("5"))
b6.clicked.connect(lambda:cac("6"))
b7.clicked.connect(lambda:cac("7"))
b8.clicked.connect(lambda:cac("8"))
b9.clicked.connect(lambda:cac("9"))
b_dot.clicked.connect(cacd)

b_p.clicked.connect(lambda:opr("+"))
b_s.clicked.connect(lambda:oprs())
b_m.clicked.connect(lambda:opr("x"))
b_d.clicked.connect(lambda:opr("/"))

b_e.clicked.connect(equal)
b_bs.clicked.connect(backspace)
b_c.clicked.connect(clear)

sys.exit(app.exec())