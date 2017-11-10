import sys
from design import Ui_AnimationPlayerWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer

class AnimationPlayer(QMainWindow, Ui_AnimationPlayerWindow):
    
    def __init__(self):
        super(AnimationPlayer, self).__init__()
        self.setupUi(self)
        self.__exec()
    
    def __exec(self):
        self.play_button.clicked.connect(self.__play_button_on_click)        
#        self.slider.valueChanged.connect()
    
    def __play_button_on_click(self):
        if self.play_button.text() == "Play":    
            self.play_button.setText("Pause")
            self.update()
            self.__progress_slider()
                        
        elif self.play_button.text() == "Pause":
            self.play_button.setText("Play")
            self.update()
    
    def __progress_slider(self):
        try:
            self.slider.setValue(self.slider.value() + 1)
        finally:
            QTimer.singleShot(500, self.__progress_slider)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ap = AnimationPlayer()
    ap.show()
    app.exec_()
