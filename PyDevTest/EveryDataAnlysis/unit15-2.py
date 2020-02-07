'''
unit 15 
3. 데이터 프레임 기초
'''

def func1():
    '''pandas 데이터 프레임 기초'''
    import pandas as pd
    index = pd.date_range('1/1/2000', periods=8)
    print(index)


def func2():
    ''' numpy 라이브러리 와 pandas '''
    import numpy as np
    import pandas as pd
    index = pd.date_range('1/1/2000', periods=8)
    df = pd.DataFrame( data=np.random.rand(8,3) , index=index , columns=list('abc') )
    
    #print( np.sum(df , axis=0)) # 합계
    #print(df['a']  , df['c'] ,df['a'] / df['c'] )
    print(df.head()) 
    df.to_csv( 'data\\aaa.csv' )


def func3():
    ''' --- pandas로 인구 구조 분석하기 ---
    1. 데이터를 읽어온다.
    -- 전체 데이터를 총 인구수로 나누어 비율로 변환한다.
    -- 총인구수와 연령구간인구수를 삭제한다.
    2. 궁금한 지역의 이름을 입력받는다.
    3. 궁금한 지역의 인구 구조를 저장한다.
    4. 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역을 찾는다.
    -- 전국의 모든 지역 중 한곳을 선택한다.
    -- 궁금한 지역 A의 0세 인구 비율에서 B의 0세 인구 비율을 뺀다.
    -- 100세 이상 인구수에 해당하는 값까지 반복한 후 차이의 제곱을 모두 더한다.
    -- 전국의 모든 지역에 대해 반복하며 그 차이가 가장 작은 지역을 찾느다.
    5. 가장 비슷한 곳의 인구 구조와 궁금한 지역의 인구 구조를 시각화 한다.   
    '''
    '''1. 데이터 읽어오기 '''
    import pandas as pd
    file_path = 'data\\age.csv'
    df = pd.read_csv(file_path , encoding='cp949' , index_col = 0)
    
    print( df.columns )
    del df['2019년12월_계_연령구간인구수']
    df.rename( columns= lambda x: x.replace('2019년12월_계_','') , inplace=True )
    print( df.columns )
    print( df.index )
    
    a =  df.index.str.contains('장수')
    print( a)
    

func3()
    
    


    












    
