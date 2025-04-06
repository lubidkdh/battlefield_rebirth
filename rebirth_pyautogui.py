from PySide2.QtWidgets import QApplication,QMainWindow,QPushButton,QPlainTextEdit


import time
import pydirectinput

class Stats():
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(300,200)
        self.window.move(810,340)
        self.window.setWindowTitle("重新部署")

        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.setPlaceholderText("请输入部署数")
        self.textEdit.move(10,25)
        self.textEdit.resize(150,50)

        self.button = QPushButton("启动！",self.window)
        self.button.move(180,35)
        self.time_begin = 10
        self.button.clicked.connect(self.mainapplication)

        self.init_count = 3
        self.exit_count = 6
    def initialize_step(self):
        pydirectinput.press('esc')
        for i in range(0,4):
             pydirectinput.press('down')
        pydirectinput.press('enter')    
        time.sleep(12)
        pydirectinput.press("space")
    def exit(self):
        pydirectinput.press('esc')
        for m in range(0,7):
            pydirectinput.press('down')
        
        pydirectinput.press('enter')
        time.sleep(4)
        pydirectinput.press('enter')
        exit(1)
        
    def mainapplication(self):
        total_count = int(self.textEdit.toPlainText())-1
        time.sleep(self.time_begin)
        self.initialize_step()
        while True:
            time.sleep(self.time_begin)            
            pydirectinput.press('esc')  
            pydirectinput.press('down')
            pydirectinput.press('down')
            pydirectinput.press('down')
            pydirectinput.press('enter') 
            time.sleep(14)
            pydirectinput.press("space")
            
            total_count =total_count-1
            if total_count ==0:
                break
        self.exit()


app = QApplication([])
stats = Stats()
stats.window.show()
app.exec_()

