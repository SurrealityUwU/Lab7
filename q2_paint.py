import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
 
class Paint(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        self.setGeometry(100, 100, 800, 600)
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.last_x, self.last_y = None, None

        self.clearButton = QPushButton("Clear", self)
        self.clearButton.clicked.connect(self.clear)
        self.clearButton.move(250,500)
        self.clearButton.setMinimumWidth(300)
        self.layout.addWidget(self.clearButton)

    def mousePressEvent(self, event):
        self.last_x, self.last_y = event.x(), event.y()
  
    def mouseMoveEvent(self, event):
        painter = QPainter(self.image)
        painter.drawLine(self.last_x, self.last_y, event.x(), event.y())

        self.last_x, self.last_y = event.x(), event.y()
        self.update()
 
    def mouseReleaseEvent(self, event):
        self.last_x, self.last_y = None, None

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())
 
    def clear(self):
        self.image.fill(Qt.white)
        self.update()

def main():
    app = QApplication(sys.argv)
 
    w = Paint()
    w.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())