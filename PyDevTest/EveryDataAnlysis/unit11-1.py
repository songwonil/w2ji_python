'''
unit 11 대중교통 데이터 시각화 하기
'''
def comma(str):
    '''콤마를 제거한다.'''    
    return float(str.replace(',',''))


def func1():    
    '''대중교통 데이터 가져오기'''
    import csv
    file_path = 'data\\subway.csv'
    f = open(file_path,'r')
    data = csv.reader(f)
    header = next(data)
    for row in data:
        print(row)
    print(header)

def func2():
    '''3. 유임승차 비율이 가장 높은 역은 어디 일까.'''
    import csv
    file_path = 'data\\subway.csv'
    f = open(file_path,'r')
    data = csv.reader(f)
    header = next(data)
    result = []
    for row in data:
        fee = comma(row[4])
        free = comma(row[6])
        total = fee + free
        if row[6] != '0' and total > 100000:
            a =  fee / total
            if len(result) ==0:
                result = row
            else:
                t = comma( result[4]) / ( comma(result[6]) + comma(result[4]) )
                if a > t :
                    result = row
                
                
    print(result)

def func3():
    '''4. 유무임 승하차 인원이 가장 많은 역은 어디일까.'''
    import csv
    file_path = 'data\\subway.csv'
    f = open(file_path,'r')
    data = csv.reader(f)
    header = next(data)
    result = []
    for row in data:
        fee = comma(row[4])
        free = comma(row[6])
        total = fee + free
        if row[6] != '0' and total > 100000:
            a =  fee / total
            if len(result) ==0:
                result = row
            else:
                t = comma( result[4]) / ( comma(result[6]) + comma(result[4]) )
                if a > t :
                    result = row
                
                
    print(result)

'''5. 모든역의 유무임 승하차 비율은 어떻게 될까.'''
import csv
file_path = 'data\\subway.csv'
f = open(file_path,'r')
data = csv.reader(f)
header = next(data)[4:-1]
result = []
for row in data:
    print( row[4:-1])
    #for i in range(4,8):
        
print(header)
