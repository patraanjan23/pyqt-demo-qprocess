from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import QProcess
import sys

class MyWidgetApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(64, 64, 400, 200)
        self.setWindowTitle("Hello World")

        self.btn = QPushButton("Press Me!")
        self.labelOut = QLabel()
        self.labelError = QLabel()
        self.outString = "Out:"
        self.errString = "Err:"
        self.vbox = QVBoxLayout()
        self.process = QProcess()

        self.setup_ui()
    
    def setup_ui(self):
        self.vbox.addWidget(self.labelOut)
        self.vbox.addWidget(self.labelError)
        self.vbox.addWidget(self.btn)
        self.setLayout(self.vbox)

        self.btn.clicked.connect(self.start_process)
        self.process.readyReadStandardOutput.connect(self.update_stdout)
        self.process.readyReadStandardError.connect(self.update_stderr)

    def start_process(self):
        self.process.start("python", "program.py".split())
    
    def update_stdout(self):
        data = self.process.readAllStandardOutput().data()
        self.outString += " " + data.decode("utf-8").rstrip()
        self.labelOut.setText(self.outString)
    
    def update_stderr(self):
        data = self.process.readAllStandardError().data()
        self.errString += " " + data.decode("utf-8").rstrip()
        self.labelError.setText(self.errString)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywidget = MyWidgetApp()
    mywidget.show()
    sys.exit(app.exec_())