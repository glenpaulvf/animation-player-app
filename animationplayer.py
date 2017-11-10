import sys
from design import Ui_AnimationPlayerWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPainter


class AnimationPlayer(QMainWindow, Ui_AnimationPlayerWindow):
    
    def __init__(self):
        super(AnimationPlayer, self).__init__()
        self.setupUi(self)
        self.__exec()
    
    def __exec(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.__progress_slider)
        
        self.play_button.clicked.connect(self.__play_button_on_click)        
        self.stop_button.clicked.connect(self.__stop_button_on_click)
    
    def __play_button_on_click(self):
        if self.play_button.text() == "Play":    
            self.play_button.setText("Pause")
            self.update()
            self.timer.start(0)
                        
        elif self.play_button.text() == "Pause":
            self.play_button.setText("Play")
            self.update()
            self.timer.stop()
    
    def __progress_slider(self):
        if self.slider.value() == self.slider.maximum():
            self.play_button.setText("Play")
            self.timer.stop()
        else:
            self.slider.setValue(self.slider.value() + 1)

    def __stop_button_on_click(self):
        self.play_button.setText("Play")
        self.slider.setValue(self.slider.minimum())
        self.timer.stop()
    

class AnimationPlayerViewer(QWidget):
    
    def __init__(self, parent = None):
        super(AnimationPlayerViewer, self).__init__()
        
        # Circle properties
        self.diameter = 10 # diameter
        self.x = 0 # x-coordinate
        self.y = 0 # y-coordinate
    
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        
        painter.setPen(Qt.black)
        painter.setBrush(Qt.black)
        painter.drawEllipse(self.x, self.y, self.diameter, self.diameter)
        
        painter.end()
        
        
                
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ap = AnimationPlayer()
    ap.show()
    app.exec_()
