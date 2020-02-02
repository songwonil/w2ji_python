'''
unit 08 인구 구조를 다양한 형태로 시각화 하기
'''
file_path = 'C:\\git\\w2ji_python\\PyDevTest\\EveryDataAnlysis\\data\\age.csv'
import csv
import matplotlib.pyplot as plt
f = open(file_path)
data = csv.reader(f)
header = next(data)
name = '신도림'
result = []
m = []
f = []
for row in data:
    if name in row[0]  :
        for i in range(0,101):
            m.append( int(row[i+3].replace(',','')) )
            f.append( -int(row[-(i+1)].replace(',','')) )

f.reverse()

print(header)

plt.style.use('ggplot')
plt.title(name+'지역의 인구 구조')
plt.barh( range(101), m , label='man')
plt.barh( range(101), f , label='famle')
plt.legend()
plt.show()
