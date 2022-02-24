import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/rabbit.png")
        self.glass = QPixmap("images/glass.png")
        self.smoke = QPixmap("images/smoke.png")
 
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
 
        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
        p.drawPixmap(QRect(180, 120, 150, 150), self.glass)
        p.drawPixmap(QRect(50, 220, 150, 150), self.smoke)
        
        p.setPen(QColor(255, 255, 0))
        p.setBrush(QColor(255, 255, 0))
        p.drawPie(50, 50, 150, 150, 0, 180 * 32)
        
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

