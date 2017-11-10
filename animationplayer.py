import sys
from design import Ui_AnimationPlayerWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

class AnimationPlayer(QMainWindow, Ui_AnimationPlayerWindow):
    
    def __init__(self):
        super(AnimationPlayer, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ap = AnimationPlayer()
    ap.show()
    app.exec_()
