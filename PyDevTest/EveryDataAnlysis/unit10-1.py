'''
unit 10 우리동네 인구 구조를 산점도로 나타내기
1 꺽은선 그래프로 표현하기
'''

def comma(str):
    return int(str.replace(',', ''))

def func1():   
    import csv
    import matplotlib.pyplot as plt
    file_path = 'data\\gen.csv'
    f = open(file_path)
    data = csv.reader(f)
    header = next(data)
    name = '2820065000'
    m = []
    f = []
    result = []
    for row in data:
        if name in row[0]:
            print(row)
            for i in range(0,101):
                m.append( comma( row[ i+3 ] ) )
                f.append( -comma( row[ i+106 ] ) )
    
    plt.plot(m , label='m')
    plt.plot(f , label='f')
    plt.legend()
    plt.show()

'''
2 막대 그래프로 표현하기
'''
def func2():   
    import csv
    import matplotlib.pyplot as plt
    file_path = 'data\\gen.csv'
    f = open(file_path)
    data = csv.reader(f)
    header = next(data)
    name = '2820065000'
    m = []
    f = []
    result = []
    for row in data:
        if name in row[0]:        
            for i in range(0,101):
                result.append( comma( row[ i+3 ] ) - comma( row[ i+106 ] ) )
                
    
    
    plt.bar(range(101),result)
    plt.show()

'''
3 산점도로 표현하기
'''
def func3():   
    import csv
    import matplotlib.pyplot as plt
    import math
    file_path = 'data\\gen.csv'
    f = open(file_path)
    data = csv.reader(f)
    header = next(data)
    name = '2820065000'
    m = []
    f = []
    result = []
    for row in data:
        if name in row[0]:        
            for i in range(0,101):
                result.append( math.sqrt( comma( row[ i+3 ] ) + comma( row[ i+106 ])) )
                m.append( comma( row[ i+3 ] ) )
                f.append( comma( row[ i+106 ] ) )
                
    
    
    plt.scatter(f,m, s=result, c=range(101) , cmap='jet')
    plt.colorbar()
    plt.plot(range(max(m)),range(max(m)), 'g') # 추세선 추가    
    plt.show()

func3()
