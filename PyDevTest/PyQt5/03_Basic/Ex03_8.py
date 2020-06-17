## Ex 3-8. 창을 화면의 가운데로.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Centering')
        self.resize(500, 350)
        self.center()   # 중앙으로 이동하는 함수
        self.show()

    def center(self):
        qr = self.frameGeometry() #창의 위치와 크기 정보를 가져온다.       
        
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())