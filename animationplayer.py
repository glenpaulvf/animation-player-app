import sys
from design import Ui_AnimationPlayerWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
                            QStyleOption, QStyle, QFileDialog
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
        
        self.slider.sliderMoved.connect(self.__animate__viewer)
        self.slider.sliderPressed.connect(self.__animate__viewer)
        self.slider.sliderReleased.connect(self.__animate__viewer)
        
        self.action_open.triggered.connect(self.__browse)
        
    def __play_button_on_click(self):
        if self.play_button.text() == "Play":    
            self.play_button.setText("Pause")
            self.update()
            self.timer.start(1000)
                        
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
            self.__animate__viewer()

    def __stop_button_on_click(self):
        self.play_button.setText("Play")
        self.slider.setValue(self.slider.minimum())
        self.timer.stop()
        self.viewer.reset()
    
    def __animate__viewer(self):
        self.viewer.animate(self.slider.value())
    
    def __browse(self):
        (filename, _) = QFileDialog.getOpenFileName(self, 'Open csv file',
                        '/home', 'CSV (*.csv)')
        

class AnimationPlayerViewer(QWidget):
    
    def __init__(self, parent = None):
        super(AnimationPlayerViewer, self).__init__(parent)

        # Circle properties
        self.diameter = 10 # diameter
        self.reset() # Sets x, y coordinates
    
    def paintEvent(self, event):
        style = QStyleOption()
        style.initFrom(self)
        style_paint = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, style, style_paint, self)
        
        painter = QPainter()
        painter.begin(self)
        
        painter.setPen(Qt.black)
        painter.setBrush(Qt.black)
        painter.drawEllipse(self.x, self.y, self.diameter, self.diameter)
        
        painter.end()
        
    def animate(self, value):
        self.x = 2 + value
        self.y = 2 + value
        self.update()
    
    def reset(self):
        self.x = 2 # x-coordinate, buffer 2px
        self.y = 2 # y-coordinate, buffer 2px
        self.update()
                
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ap = AnimationPlayer()
    ap.show()
    app.exec_()
