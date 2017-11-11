import sys
import csv
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
            self.__animate__viewer()

    def __stop_button_on_click(self):
        self.play_button.setText("Play")
        self.slider.setValue(self.slider.minimum())
        self.timer.stop()
        self.viewer.reset()
    
    def __animate__viewer(self):
        with open(self.ifile, 'r') as f:
            reader = csv.reader(f)      
            
            for i, row in enumerate(reader):
                if i == self.slider.value():
                    new_x = int(row[0])
                    new_y = int(row[1])
                    break
                    
        self.viewer.animate(new_x, new_y)
    
    def __browse(self):
        (self.ifile, _) = QFileDialog.getOpenFileName(self, 'Open csv file',
                        '/', 'CSV (*.csv)')
        
        # Enable pushbuttons and slider
        self.play_button.setEnabled(True)
        self.stop_button.setEnabled(True)
        self.slider.setEnabled(True)
        
        self.__preprocess_data()
                        
    def __preprocess_data(self):
        with open(self.ifile, 'r') as f:
            reader = csv.reader(f)      
        
            max_x = max(int(column[0].replace(',', '')) for column in reader)
            f.seek(0)
            max_y = max(int(column[1].replace(',', '')) for column in reader)

            self.slider.setMaximum(max_x)
            self.slider.setMinimum(1)
            self.slider.setValue(1)
                    
            f.seek(0)
            for i, row in enumerate(reader):
                if i == 1:
                    self.viewer.set_coordinates(int(row[0]), int(row[1]))
                    break
            

class AnimationPlayerViewer(QWidget):
    
    def __init__(self, parent = None):
        super(AnimationPlayerViewer, self).__init__(parent)

        # Circle properties
        self.init_x = 0
        self.init_y = 0
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
        
    def animate(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.update()
    
    def reset(self):
        self.x = self.init_x
        self.y = self.init_y
        self.update()
    
    def set_coordinates(self, x, y):
        self.init_x = x
        self.init_y = y
        self.x = x
        self.y = y
        self.update()
                
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ap = AnimationPlayer()
    ap.show()
    app.exec_()
