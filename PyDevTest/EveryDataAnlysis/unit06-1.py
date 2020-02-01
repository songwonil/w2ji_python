'''
UNIT 06 기온 데이터를 다양하게 시각화 하기
'''
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
plt.hist( tm , label= header[4] )
#plt.hist( tmin , label= header[3] )
plt.legend()
plt.show()
'''
import random
import matplotlib.pyplot as plt
dice = list()
for i in range(1,10000):
    dice.append( random.randint(1,6) )

plt.hist(dice )
plt.show()

