import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/rabbit.png")
        self.frabbit = QPixmap("images/fliped_rabbit.png")
        self.noot = QPixmap("images/Nootfly.gif")
 
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.drawPixmap(QRect(250, -20, 160, 160), self.rabbit)
        p.drawPixmap(QRect(250, 100, 160, 160), self.frabbit)
        p.drawPixmap(QRect(250, 220, 160, 160), self.rabbit)
        p.drawPixmap(QRect(250, 340, 160, 160), self.frabbit)
        p.drawPixmap(QRect(50, 40, 80, 80), self.noot)
        
 
        p.setPen(QColor(0, 255, 0))
        p.setBrush(QColor(0, 255, 0))
        p.setOpacity(0.2)
        
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