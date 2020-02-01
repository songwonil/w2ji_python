'''
unit 06-3 기온데이터를 히스토그램으로 표현하기
'''
import csv
import matplotlib.pyplot as plt
str = 'C:\\git\\w2ji_python\\PyDevTest\\EveryDataAnlysis\\data\\tem_data.csv'
f = open( str ,'r', encoding='euckr')
data = csv.reader( f , delimiter=',' )

# 헤더 저장하기
header = next(data)
#리스트
aug = list()
jan = list()
for row in data:
    if row[4] != '':
        if row[2].split('-')[1] == '08':        
            aug.append( float( row[4]) )
        if row[2].split('-')[1] == '01':        
            jan.append( float( row[4]) )


plt.hist( aug ,bins=100 )
plt.hist( jan ,bins=100 )
plt.show()
