'''
unit 03 서울이 가장 더웠던 날은 언제였을까/
'''
import csv
str = 'C:\\git\\w2ji_python\\PyDevTest\\EveryDataAnlysis\\data\\tem_data.csv'
f = open( str ,'r', encoding='euckr')
data = csv.reader( f , delimiter=',' )

# 헤더 저장하기
header = next(data)

max_date = ''
t_max_temp0 = 0
t_max_temp1 = 0
for row in data:
    
    
    if row[4] !='':        
        t_max_temp0 = float(row[4])
    else:
        t_max_temp0 = 0
    #print( row , t_max_temp )
    if t_max_temp0 > t_max_temp1:
        t_max_temp1 = t_max_temp0
        max_date = row
    



f.close()
print('서울의 최고 기온은',max_date[4],'도로 ', max_date[2],'입니다' )