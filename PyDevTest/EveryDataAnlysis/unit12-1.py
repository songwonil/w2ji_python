'''
unit 12 지하철 시간대별 데이터 시각화하기
- 출근 시간대 사람들이 가장 많이 타고내리는 역은 어디일까
- 지하철 시간대별로 가장 많은 사람이 승하차 하는 역은 어디일까

'''
def func1():
    '''데이터 확인'''
    import csv
    file_path = 'data\\time.csv'
    f = open(file_path)
    data = csv.reader(f)
    head = next(data)
    print(head)
    print(next(data))
    
    for row in data:
        row[4:] = map(float , row[4:])
        print(row)

def func2():
    '''2.출근 시간대 사람들이 가장 많이 타고 내리는 역은 어디일까.'''
    import csv
    import matplotlib.pyplot as plt
    file_path = 'data\\time.csv'
    f = open(file_path)
    data = csv.reader(f)
    head1 = next(data)
    head2 = next(data)
    result = []
    for row in data:
        row[4:] = map(float , row[4:])
        result.append(row[10])
    print(result)
    print(len(result))
    result.sort()
    plt.bar(range( len(result) ) , result)
    plt.show()