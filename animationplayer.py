import sys
import csv
from design import Ui_AnimationPlayerWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
                            QStyleOption, QStyle, QFileDialog, QMessageBox
from PyQt5.QtCore import QTimer, Qt, pyqtSignal
from PyQt5.QtGui import QPainter



class AnimationPlayer(QMainWindow, Ui_AnimationPlayerWindow):
    # Create signal
    resized = pyqtSignal()
        
    def __init__(self):
        super(AnimationPlayer, self).__init__()
        self.setupUi(self)
        
        # Setup error dialog
        self.error_dialog = QMessageBox()
        self.error_dialog.setIcon(QMessageBox.Critical)
        self.error_dialog.setText('There was a problem loading the file.')
        self.error_dialog.setWindowTitle("Error")
        
        # Set defaults
        self.scale_factor = 1
        self.max_x = 100
        self.max_y = 100
        self.playback_slow = 1500 / 100
        self.playback_normal = 1000 / 100
        self.playback_fast = 500 / 100
        
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
        
        self.playback_slider.valueChanged.connect(self.__change_playback)
        
        self.resized.connect(self.__scale_data)
        
    def __play_button_on_click(self):
        if self.play_button.text() == "Play":    
            self.play_button.setText("Pause")
            self.update()
            self.timer.start(self.playback_normal)
                        
        elif self.play_button.text() == "Pause":
            self.play_button.setText("Play")
            self.update()
            self.timer.stop()
    
    def __progress_slider(self):
        if self.slider.value() == self.slider.maximum():
            self.play_button.setText("Play")
            self.timer.stop()
        else:
            if self.slider.value() < self.slider.maximum():     
                self.slider.setValue(self.slider.value() + 1)
                self.__animate__viewer()

    def __stop_button_on_click(self):
        self.play_button.setText("Play")
        self.slider.setValue(self.slider.minimum())
        self.timer.stop()
        self.viewer.reset()
    
    def __animate__viewer(self): 
        if self.slider.value() < self.slider.maximum():
            try:
                with open(self.ifile, 'r') as f:
                    reader = csv.reader(f)      
                    
                    for i, row in enumerate(reader):
                        if i == self.slider.value():
                            new_x = int(row[0]) * self.scale_factor + 2
                            new_y = int(row[1]) * self.scale_factor + 2
                            break
                
                self.viewer.animate(new_x, new_y)
            except:
                self.error_dialog.show()
    
    def __browse(self):
        (self.ifile, _) = QFileDialog.getOpenFileName(self, 'Open csv file',
                        '/', 'CSV (*.csv)')

        # Enable pushbuttons and slider
        self.play_button.setEnabled(True)
        self.stop_button.setEnabled(True)
        self.slider.setEnabled(True)
        self.playback_slider.setEnabled(True)
        
        self.__preprocess_data()
                        
    def __preprocess_data(self):
        try:
            with open(self.ifile, 'r') as f:
                reader = csv.reader(f)      
            
                # Set scale factor for data
                self.max_x = max(int(column[0].replace(',', '')) for column in reader)
                f.seek(0)
                self.max_y = max(int(column[1].replace(',', '')) for column in reader)
                
                self.__scale_data()
                
                f.seek(0)
                count = sum(1 for row in reader)
                
                # Set slider
                self.slider.setMaximum(count)
                self.slider.setMinimum(1)
                self.slider.setValue(1)
                        
                # Set initial coordinators
                f.seek(0)
                for i, row in enumerate(reader):
                    if i == 1:
                        self.viewer.directive = True
                        x_init = int(row[0]) * self.scale_factor - 3
                        y_init = int(row[1]) * self.scale_factor - 3
                        self.viewer.set_coordinates(x_init, y_init)
                        break
        except:
            # Disable pushbuttons and slider
            self.play_button.setEnabled(False)
            self.stop_button.setEnabled(False)
            self.slider.setEnabled(False)
            self.playback_slider.setEnabled(False)
            
            self.error_dialog.show()
            
    def __scale_data(self):
        width = self.viewer.width() - 15 # -12 for padding, -3 for circle
        height = self.viewer.height() - 15 # -12 for padding, -3 for circle

        max_x = self.max_x
        max_y = self.max_y

        if max_x > width and max_y > height:
            self.scale_factor =  min((width / float(max_x - 3)), (height / float(max_y - 3)))
        elif max_x > width: # and max_y < height
            self.scale_factor =  width / float(max_x - 3)
        elif max_y > height: # and max_x < width
            self.scale_factor =  height / float(max_y - 3)
        else: # max_x <= width and max_y <= height:
            self.scale_factor =  self.scale_factor
        
        self.update()
        
    def resizeEvent(self, event):
        self.resized.emit()
        
    def __change_playback(self):
        if self.playback_slider.value() == 0:
            self.timer.start(self.playback_slow)
        elif self.playback_slider.value() == 1:
            self.timer.start(self.playback_slow)
        else: # self.playback_slider.value() == 2:
            self.timer.start(self.playback_fast)
        

class AnimationPlayerViewer(QWidget):
    
    def __init__(self, parent = None):
        super(AnimationPlayerViewer, self).__init__(parent)

        self.directive = False
        
        # Circle properties
        self.init_x = -3 # +2 for padding, -5 for radius
        self.init_y = -3 # +2 for padding, -5 for radius
        self.radius = 5
        self.diameter = self.radius * 2 # diameter
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
        
        
        if self.directive:
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
