from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit
import cv2
import pyautogui
import time

class Stats():
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(300,200)
        self.window.move(810,340)
        self.window.setWindowTitle("重新部署")

        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.setPlaceholderText("请输入部署次数")
        self.textEdit.move(10,25)
        self.textEdit.resize(150,50)

        self.button = QPushButton("启动！",self.window)
        self.button.move(180,35)

        self.time_begin = 4

        self.button.clicked.connect(self.mainapplication)

    def get_xy(self):
        pyautogui.screenshot().save("./pic/screenshot.png")
        img = cv2.imread("./pic/screenshot.png")
        img_terminal = cv2.imread("./pic/terminal.png")
        if img_terminal is None:
            print("Warning: terminal.png not found, using default coordinates")
            return (960, 540)  # Default center screen coordinates
        height, width, channel = img_terminal.shape
        result = cv2.matchTemplate(img,img_terminal,cv2.TM_SQDIFF_NORMED)
        upper_left = cv2.minMaxLoc(result)[2]
        lower_right = (upper_left[0] + width,upper_left[1] + height)
        avg = (int((upper_left[0]+lower_right[0])/2),int((upper_left[1]+lower_right[1])/2))
        return avg

    def auto_click(self,var_avg):
        pyautogui.click(var_avg[0],var_avg[1],button="left")
        # time.sleep(2)
    
    def mainapplication(self):
        total_count = int(self.textEdit.toPlainText())
        time.sleep(self.time_begin)
        while True:
            pyautogui.press('esc')  
            pyautogui.moveTo(960, 540)  
            time.sleep(2)
            self.get_xy() 
            avg = self.get_xy()
            self.auto_click(avg)
            time.sleep(12)
            pyautogui.press("space")
            time.sleep(4)
            
            total_count =total_count-1
            if total_count ==0:
                break


if __name__ == "__main__":
    app = QApplication([])
    stats = Stats()
    stats.window.show()
    app.exec()