import sys
from PyQt5.QtWidgets import QApplication , QWidget

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        '''    '''
        self.setWindowTitle('My First Application') #제목 
        self.move(300,300)# x, y 의 좌표 로이동
        self.resize(400,200) # 크기
        self.show() # 출력


if __name__ == '__main__':
    print(__name__)
    app = QApplication(sys.argv)
    print(app)
    ex = MyApp()
    sys.exit( app.exec_() )      