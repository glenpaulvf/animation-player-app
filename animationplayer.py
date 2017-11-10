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
        self.timer = QTimer()
        self.timer.timeout.connect(self.__progress_slider)
        
        self.play_button.clicked.connect(self.__play_button_on_click)        
    
    def __play_button_on_click(self):
        if self.play_button.text() == "Play":    
            self.play_button.setText("Pause")
            self.update()
            self.timer.start(500)
                        
        elif self.play_button.text() == "Pause":
            self.play_button.setText("Play")
            self.update()
            self.timer.stop()
    
    def __progress_slider(self):
        self.slider.setValue(self.slider.value() + 1)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ap = AnimationPlayer()
    ap.show()
    app.exec_()
