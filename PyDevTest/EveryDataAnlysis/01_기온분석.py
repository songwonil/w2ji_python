import csv
str = 'C:\\git\\w2ji_python\\PyDevTest\\EveryDataAnlysis\\data\\tem_data.csv'
f = open( str ,'r', encoding='euckr')
data = csv.reader( f , delimiter=',' )

# 헤더 저장하기
header = next(data)

i=0
for row in data:
    i+=1
    print(i,row)

print(header)

f.close()