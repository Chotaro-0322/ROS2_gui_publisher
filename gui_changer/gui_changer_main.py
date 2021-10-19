import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from .submodule.gui_changer_fun import Ui_MainWindow
import rclpy
from rclpy.node import Node

class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def main(args=None):
    # ros setting
    rclpy.init(args=None) 
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()