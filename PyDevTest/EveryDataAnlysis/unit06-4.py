'''
unit 06-4 기온데이터를 상자 그림으로 표현하기
'''
import matplotlib.pyplot as plt
import random
'''
#랜덤값으로 박스 그림 표현
result = list()

for row in range(1,100):
    result.append(  random.randint(1,100) )


print(result)
plt.boxplot( result  )
plt.show()
'''


'''
# 최고 기온 값으로 표현
import csv

str = 'C:\\git\\w2ji_python\\PyDevTest\\EveryDataAnlysis\\data\\tem_data.csv'
f = open( str ,'r', encoding='euckr')
data = csv.reader( f , delimiter=',' )

# 헤더 저장하기
header = next(data)

#리스트
result = list()

for row in data:
    if row[4] != '':
        result.append(  float(row[4]) )


print(result)
plt.boxplot( result  )
plt.show()
'''
'''
# 8월과 1월 값으로 박스 그림 표현
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


plt.boxplot( [aug,jan] )
#plt.boxplot( jan )
plt.show()
'''
'''
# 월별 기온
import csv
import matplotlib.pyplot as plt
str = 'C:\\git\\w2ji_python\\PyDevTest\\EveryDataAnlysis\\data\\tem_data.csv'
f = open( str ,'r', encoding='euckr')
data = csv.reader( f , delimiter=',' )

# 헤더 저장하기
header = next(data)
#리스트
month = [[],[],[],[],[],[],[],[],[],[],[],[]]

for row in data:
    if row[2] != '' and row[4] !='':
        month[ int(row[2].split('-')[1])-1 ].append( float( row[4]) )


plt.boxplot( month )
#plt.boxplot( jan )
plt.show()
'''
# 8월달 일별 기온 상자 그림
import csv
import matplotlib.pyplot as plt
str = 'C:\\git\\w2ji_python\\PyDevTest\\EveryDataAnlysis\\data\\tem_data.csv'
f = open( str ,'r', encoding='euckr')
data = csv.reader( f , delimiter=',' )

# 헤더 저장하기
header = next(data)
#리스트
day = []
for i in range(31):
    day.append([])

for row in data:
    if row[2] != '' and row[4] !='' and row[2].split('-')[1] == '08' : 
        day[ int(row[2].split('-')[2])-1 ].append( float( row[4]) )


plt.style.use('ggplot') # 그래프 스타일 지정
plt.figure(figsize=(10,5), dpi=100) #그래프 크기 수정
plt.boxplot( day , showfliers=False)    #아웃라이어 값 생략
#plt.boxplot( jan )
plt.show()
