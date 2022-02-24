import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/rabbit.png")
        self.drone = QPixmap("images/drone.jpeg")
        self.logo = QPixmap("images/logo.jpg")
 
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
 
        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
        p.drawPixmap(QRect(50, 50, 100, 150), self.drone)
        p.drawPixmap(QRect(200, 150, 80, 80), self.logo)
 
        p.setPen(QColor(0, 255, 0))
        p.setBrush(QColor(0, 255, 0))
        p.setOpacity(0.2)
        p.drawPie(190, 140, 100, 100, 0, 180 * 32)
        
        p.end()
        
    def Simple_drawing_window1(self):
        pass
 
def main():
    app = QApplication(sys.argv)
 
    w = Simple_drawing_window()
    w.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())

