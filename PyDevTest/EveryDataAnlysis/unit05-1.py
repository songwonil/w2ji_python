'''
UNIT 05 내 생일의 기온 변화를 그래프로 그리기
'''
import csv
str = 'C:\\git\\w2ji_python\\PyDevTest\\EveryDataAnlysis\\data\\tem_data.csv'
f = open( str ,'r', encoding='euckr')
data = csv.reader( f , delimiter=',' )
header = next(data)
alist = list()
tm = list()
tmin = list()
for row in data:
    if row[-1]!='' and (row[2])[5:10] == '01-05':
        alist.append(row)

for i in alist:
    tm.append( float(i[4]))
    tmin.append( float(i[3]) )
print(header)

import matplotlib.pyplot as plt
plt.plot( tm , label= header[4] )
plt.plot( tmin , label= header[3] )
plt.legend()
plt.show()


