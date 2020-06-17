## Ex 3-6. 메뉴바 만들기.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+q')    #단축키임과 동시에 표시됨
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)
        
        self.statusBar().showMessage('Ready') #상태바에 넣는다.
        self.setWindowTitle('Menubar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())