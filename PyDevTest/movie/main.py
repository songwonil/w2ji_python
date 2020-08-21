import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QSpacerItem
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGroupBox

from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QFormLayout


from PyQt5.QtCore import QSize


from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem


import pymysql
from PyQt5.Qt import QVBoxLayout


__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QWidget):
    
    
    
    def getDbCon(self):
        '''db 연결체'''
        con = pymysql.connect(host='127.0.0.1', user='com', password='com01', db='com_mall', charset='utf8')
        return con    

    def dbSelect(self , v1d , v2d , v31 , v32 , v4d):
        ''' -DB 조회        '''
        print( v1d , v2d , v31 , v32 , v4d )
        
        rr = []
        conn = self.getDbCon()
        
        curs = conn.cursor()
        sql = ' select ' 
        sql += ' a.movietitle  , a.releasedate , a.videoreleasedate , a.IMDBURL , b.genre_nm , cast(c.rating as char(2)) rating , d.age , d.gender , d.occupation '
        sql += ' from movie_item a '
        sql += ' join movie_genre b on ( a.genre = b.genre) '
        sql += ' join movie_rate c on ( a.movieid  = c.movieid) '
        sql += ' join movie_users d on ( c.user_id = d.user_id ) '
        sql += ' and b.genre like \''+v1d+'\' '
        sql += ' and d.occupation like \''+v2d+'\' '
        sql += ' and c.rating between '+v31+' and '+v32
        sql += ' order by '+v4d
        print(sql)
        
        
        curs.execute(sql)
        rows = curs.fetchall()        
        for row in rows:
            aa = []
            aa.append( row[0] )
            aa.append( row[1] )
            aa.append( row[2] )
            aa.append( row[3] )
            aa.append( row[4] )
            aa.append( row[5] )
            aa.append( row[6] )
            aa.append( row[7] )
            aa.append( row[8] )
            rr.append(aa)       
        
        conn.close()
        return rr  
        
        

    def getCombo(self , str):
        ''' -DB 콤보  : genre(장르) , job(직업)     '''        
        rr = []
        sql = ''
        conn = self.getDbCon()
        
        curs = conn.cursor()
        if(str == 'genre'):
            sql = 'select  genre_nm as nm , genre as id from movie_genre order by 2'
        elif( str == 'job' ):
            sql = 'select distinct  occupation as nm , occupation as id  from movie_users order by 2'

            
        curs.execute(sql)
         
        # 데이타 Fetch
        rows = curs.fetchall()        
        for row in rows:
            aa = []
            aa.append( row[0] )
            aa.append( row[1] )
            rr.append(aa)       
        
        conn.close()
        return rr  
    
    def btn5Click(self):
        print('fffff')
        
    
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.init_widget()

    def init_widget(self):
        """        현재 위젯의 모양등을 초기화        """
        

            
        
        tableWidget = QTableWidget()
        
        
            
        
        
        self.setWindowTitle("QComboBox Widget")
        self.resize(1024,768) # 크기
        
        
        layout_base = QBoxLayout(QBoxLayout.TopToBottom, self)
        self.setLayout(layout_base)

        # 첫 번째 그룹 QBoxLayout
        search = QGroupBox("검색")        
        search.setFixedHeight(250)
        layout_base.addWidget(search)
        
        vlayout = QVBoxLayout() #버티컬 레이아웃
        
        layout1 = QHBoxLayout()        
        lb1 = QLabel('장르 : ')       
        lb1.setFixedSize( QSize(80,30) )  
        layout1.addWidget(lb1)        
        qb1 = QComboBox()
        
        qb1.addItem( '전체' , '%' )
        gg = self.getCombo('genre')
        for g in gg:
            qb1.addItem( g[0] , g[1] )

        
        
        
        qb1.setFixedSize( QSize(150,30) )
        layout1.addWidget(qb1)        
        layout1.addStretch(1)
        vlayout.addLayout( layout1 )
        
        layout2 = QHBoxLayout()        
        lb2 = QLabel('직업 : ')       
        lb2.setFixedSize( QSize(80,30) )  
        layout2.addWidget(lb2)        
        qb2 = QComboBox()
        
        jj = self.getCombo('job')
        qb2.addItem( '전체' , '%' )
        for j in jj:
            qb2.addItem( j[0] , j[1] )        
        
        qb2.setFixedSize( QSize(150,30) )
        layout2.addWidget(qb2)        
        layout2.addStretch(1)
        vlayout.addLayout( layout2 )        


        layout3 = QHBoxLayout()        
        lb3 = QLabel('평점 : ')       
        lb3.setFixedSize( QSize(80,30) )  
        layout3.addWidget(lb3)        
        
        lb3_1 = QLabel('Min')
        lb3_1.setFixedSize( QSize(80,30) )
        layout3.addWidget(lb3_1)
        
        ql3_1 = QLineEdit()
        ql3_1.setText('0')
        ql3_1.setFixedSize( QSize(150,30) )
        layout3.addWidget(ql3_1)
        
        
        lb3_2 = QLabel('Max')
        lb3_2.setFixedSize( QSize(80,30) )
        layout3.addWidget(lb3_2)
        
        ql3_2 = QLineEdit()
        ql3_2.setFixedSize( QSize(150,30) )
        ql3_2.setText('10')
        layout3.addWidget(ql3_2)        
        
                
        layout3.addStretch(1)
        vlayout.addLayout( layout3 )
        
        
        layout4 = QHBoxLayout()        
        lb4 = QLabel('Sort by ')       
        lb4.setFixedSize( QSize(80,30) )  
        layout4.addWidget(lb4)        
        qb4 = QComboBox()
        l4 = [['제목','a.movietitle'],['개봉일','a.releasedate'],['vod출시일','a.videoreleasedate'],['Url','a.IMDBURL'],['장르','b.genre_nm'],['평점','c.rating'],['성별','d.gender'],['직업','d.occupation']]
        for l in l4:
            qb4.addItem( l[0] , l[1] )
        
        
        qb4.setFixedSize( QSize(150,30) )
        layout4.addWidget(qb4)        
        layout4.addStretch(1)
        vlayout.addLayout( layout4 )        
        
        def abc():
            print('aaa')
            tableWidget.clear()
            tableWidget.setRowCount( 1 )
            tableWidget.setHorizontalHeaderLabels(["제목","개봉일","vod출시일","Url","장르","평점","나이","성별","직업"])
            v1i = qb1.currentIndex()
            v1t = qb1.itemText(v1i)
            v1d = qb1.itemData(v1i)
            
            v2i = qb2.currentIndex()
            v2t = qb2.itemText(v2i)
            v2d = qb2.itemData(v2i)
            
            v31 = ql3_1.text()
            v32 = ql3_2.text()
            
            v4i = qb4.currentIndex()
            v4t = qb4.itemText(v4i)
            v4d = qb4.itemData(v4i)
            
            result = self.dbSelect( v1d , v2d , v31 , v32 , v4d )
            tableWidget.setRowCount( result.__len__() )
            tableWidget.setColumnCount(9)
            tableWidget.setHorizontalHeaderLabels(["제목","개봉일","vod출시일","Url","장르","평점","나이","성별","직업"])
            row_cnt = 0
            for r in result:  
                tableWidget.setItem( row_cnt ,0, QTableWidgetItem( r[0] ))
                tableWidget.setItem( row_cnt ,1, QTableWidgetItem( r[1] ))
                tableWidget.setItem( row_cnt ,2, QTableWidgetItem( r[2] ))
                tableWidget.setItem( row_cnt ,3, QTableWidgetItem( r[3] ))
                tableWidget.setItem( row_cnt ,4, QTableWidgetItem( r[4] ))
                tableWidget.setItem( row_cnt ,5, QTableWidgetItem( r[5] ))
                tableWidget.setItem( row_cnt ,6, QTableWidgetItem( r[6] ))
                tableWidget.setItem( row_cnt ,7, QTableWidgetItem( r[7] ))
                tableWidget.setItem( row_cnt ,8, QTableWidgetItem( r[8] ))
                row_cnt= row_cnt+1
            
            

            
        
        layout5 = QHBoxLayout()
        btn5 = QPushButton("검색", self)
        btn5.clicked.connect( abc )
        
        
        btn5.setFixedSize( QSize(565,30) )
        layout5.addWidget(btn5)
        layout5.addStretch(1)
        vlayout.addLayout( layout5 )        
        
        search.setLayout(vlayout)       
        
        list = QGroupBox("Search Movie")
        layout_base.addWidget(list)
        layout = QHBoxLayout()
        
        
        result = self.dbSelect( '%' , '%' , '0' , '10' , 'a.movietitle' )
        
        # Create table
        
        
        
        #a.movietitle  , a.releasedate , a.videoreleasedate , a.IMDBURL , b.genre_nm , c.rating , d.age , d.gender , d.occupation
        tableWidget.setRowCount( result.__len__() )
        tableWidget.setColumnCount(9)
        tableWidget.setHorizontalHeaderLabels(["제목","개봉일","vod출시일","Url","장르","평점","나이","성별","직업"])
        row_cnt = 0
        for r in result:  
            tableWidget.setItem( row_cnt ,0, QTableWidgetItem( r[0] ))
            tableWidget.setItem( row_cnt ,1, QTableWidgetItem( r[1] ))
            tableWidget.setItem( row_cnt ,2, QTableWidgetItem( r[2] ))
            tableWidget.setItem( row_cnt ,3, QTableWidgetItem( r[3] ))
            tableWidget.setItem( row_cnt ,4, QTableWidgetItem( r[4] ))
            tableWidget.setItem( row_cnt ,5, QTableWidgetItem( r[5] ))
            tableWidget.setItem( row_cnt ,6, QTableWidgetItem( r[6] ))
            tableWidget.setItem( row_cnt ,7, QTableWidgetItem( r[7] ))
            tableWidget.setItem( row_cnt ,8, QTableWidgetItem( r[8] ))
            row_cnt= row_cnt+1
        
       
       
        layout.addWidget(tableWidget)
        
        
        
        list.setLayout(layout)
        

        
        
                
       




if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())