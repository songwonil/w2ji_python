'''
unit 14 numpy를 활용한 나만의 프로젝트 만들기
'''
'''
1. 관심 있는 데이터 찾기
www.data.go.kr
'''
'''
2. 데이터 살펴보며 질문하기
- 전국에서 영유아들이 가장 많이 사는 지역은 어디일까
- 보통 학군이 좋다고 알려진 지역에는 청소년들이 많이 살까?
- 광역시 데이터를 10년 단위로 살펴보면 청년 비율이 줄고 있다는 사실을 알수 있을까?
- 서울에서 지난 5년간 인구가 가장 많이 증가한 구는 어디일까?
- 우리 동네의 인구 구조와 가장 비슷한 동네는 어디일까?
'''

def func1():
    '''
    - 우리 동네와  인구 구조가 가장  비슷한 지역은 어디 일까?
    @ 알고리즘 설계
    1. 데이터를 읽어온다.
    2. 궁금한 지역의 이름을 입력받는다.
    3. 궁금한 지역의 인구 구조를 저장한다.
    4. 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역을 찾는다.
    5. 가장 비슷한 곳의 인구 구조와 궁금한 지역의 인구 구조를 시각화 한다.   
    @ 알고리즘을 코드로 표현한다.
    1. 데이터 읽어오기  
    '''
        
    import csv
    import numpy as np
    import matplotlib.pyplot as plt
    f = open('data\\age.csv')
    data = csv.reader(f)
    head = next(data)
    result = []
    name = '장수서창' #궁금한 지역의 이름이나 코드를 입력한다.
    target = []
    # 데이터 읽기 start
    for row in data:
        for i,v in enumerate(row[1:]):
            row[i+1] = v.replace(',','')
        result.append( row )
    # 데이터 읽기 end
    # 타겟 추출 start
    for i in result:        
        if name in i[0]:
            target = i
            target[1:] = np.array( target[1:] , dtype = int )
    # 타겟 추출 end
    home = np.array( target[3:] )/ target[2]
        
    
    '''
    -차트로 인구 구성을 확인해본다.
    print(target)
    plt.rc('font', family='Malgun Gothic')
    plt.title(target[0]+' 지역의 인구 구조')
    plt.plot( target[3:] )
    plt.show()
    '''
    '''
    - 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역 찾기
    1. 전국의 모든 지역 중 한곳을 선택한다.
    2. 궁금한 지역 의  0세 인구수와 비교 지역의 0세 인구수를 뺀다.
    3. 0~100세까지 2번을 반복하여 차이를 모두 더한다.
    4. 전국의 모든 지역에 대해 반복하며 그 차이가 가장 작은 지역을 찾는다.     
    '''
    #
    for i in result:
        total = 0        
        i[1:] = np.array(i[1:] , dtype=int)
        away = np.array( i[3:] , dtype=int ) / int( i[2] )
        i.append( np.sum( home - away)**2 )
    away = result[0]
    for i in result:
        if name not in i[0]:
            if away[-1] < i[-1]:
                away = i 
        
    
    print(away)
    print( target )
        
    plt.rc('font', family='Malgun Gothic')
    plt.title(target[0]+' 지역의 인구 구조')
    plt.plot( target[3:-1] , label=target[0])
    plt.plot( away[3:-1] , label=away[0] )
    plt.legend()
    plt.show()
            


        
    
    
        
    
            
    
    
    

func1()


    

    


