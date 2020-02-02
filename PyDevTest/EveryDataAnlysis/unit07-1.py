'''
unit 07 우리 동네 인구 구조 시각화하기
'''
file_path = 'C:\\git\\w2ji_python\\PyDevTest\\EveryDataAnlysis\\data\\age.csv'
import csv
import matplotlib.pyplot as plt
f = open(file_path)
data = csv.reader(f)
header = next(data)
result = []
for row in data:
    if '2820000000' in row[0]  :
        for i in row[3:]:
            num = i.replace(',','')
            print(num)             
            result.append( int(num) )                    
            #result.append( row )

print(header)
print(result)
plt.style.use('ggplot')
plt.plot(result)
plt.show()
