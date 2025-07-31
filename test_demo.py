#!/usr/bin/env python3
"""
Demo script for the game automation project
Shows the functionality without actually running automation
"""

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QLabel
import sys

class DemoWindow:
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(400, 300)
        self.window.setWindowTitle("重新部署 - Demo Mode")
        
        # Input field
        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.setPlaceholderText("请输入部署次数 (Enter number of deployments)")
        self.textEdit.move(10, 25)
        self.textEdit.resize(200, 50)
        
        # Buttons
        self.keyboard_button = QPushButton("键盘模式 (Keyboard Mode)", self.window)
        self.keyboard_button.move(10, 90)
        self.keyboard_button.resize(180, 30)
        self.keyboard_button.clicked.connect(self.demo_keyboard_mode)
        
        self.cv_button = QPushButton("视觉模式 (CV Mode)", self.window)
        self.cv_button.move(200, 90)
        self.cv_button.resize(180, 30)
        self.cv_button.clicked.connect(self.demo_cv_mode)
        
        # Status label
        self.status_label = QLabel("准备就绪 (Ready)", self.window)
        self.status_label.move(10, 140)
        self.status_label.resize(370, 150)
        self.status_label.setWordWrap(True)
        self.status_label.setStyleSheet("background-color: #f0f0f0; padding: 10px; border: 1px solid #ccc;")
        
    def demo_keyboard_mode(self):
        try:
            count = int(self.textEdit.toPlainText() or "1")
            status_text = f"""
🖥️ 键盘自动化模式演示 (Keyboard Automation Demo)

将执行 {count} 次部署循环 (Will perform {count} deployment cycles)

步骤 (Steps):
1. 按ESC打开菜单 (Press ESC to open menu)
2. 使用方向键导航 (Navigate with arrow keys)  
3. 按ENTER选择选项 (Press ENTER to select)
4. 等待游戏响应 (Wait for game response)
5. 按SPACE确认 (Press SPACE to confirm)
6. 重复过程 (Repeat process)

⚠️ 演示模式 - 不会执行实际操作
(Demo mode - no actual automation will run)
            """
            self.status_label.setText(status_text)
        except ValueError:
            self.status_label.setText("请输入有效数字 (Please enter a valid number)")
    
    def demo_cv_mode(self):
        try:
            count = int(self.textEdit.toPlainText() or "1")
            status_text = f"""
👁️ 计算机视觉模式演示 (Computer Vision Demo)

将执行 {count} 次部署循环 (Will perform {count} deployment cycles)

步骤 (Steps):
1. 截取屏幕截图 (Take screenshot)
2. 使用OpenCV匹配终端按钮 (Use OpenCV to match terminal button)
3. 计算按钮中心坐标 (Calculate button center coordinates)
4. 自动点击按钮 (Auto-click button)
5. 等待加载完成 (Wait for loading)
6. 重复过程 (Repeat process)

📁 需要 pic/terminal.png 作为模板图像
(Requires pic/terminal.png as template image)

⚠️ 演示模式 - 不会执行实际操作  
(Demo mode - no actual automation will run)
            """
            self.status_label.setText(status_text)
        except ValueError:
            self.status_label.setText("请输入有效数字 (Please enter a valid number)")

def main():
    app = QApplication(sys.argv)
    demo = DemoWindow()
    demo.window.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())