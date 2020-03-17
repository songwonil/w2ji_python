'''
title : 최적화 알고리즘
date : 2020.03.16
content : 재귀함수를 사용한 최적화 시간을 찾는 프로그램.
이런 저런
제발
'''

from numpy.random.mtrand import randint
import random
from numpy import cumsum

'''

'''


# 기초 데이터 데이터 
data = [
        ['A' , 0.2  , 1     , 0.15  , 0.15],
        ['F' , 0.35 , 2     , 0.35  , 0.35],
        ['H' , 0.35 , 2     , 0.583 , 0.583], 
        ['B' , 0.5  , 6     , 0.183 , 0.183], 
        ['C' , 0.4  , 4     , 0.5   , 0.5], 
        ['D' , 0.6  , 8     , 0.267 , 0.267], 
        ['E' , 0.4  , 4     , 0.5   , 0.5],          
        ['G' , 0.6  , 8     , 0.417 , 0.417],         
        ['I' , 0.5  , 6     , 0.35  , 0.35], 
        ['J' , 0.8  , 11    , 0.35  , 0.35], 
        ['K' , 1.2  , 14    ,  0.5  , 0.5], 
        ['L' , 0.95 , 13    , 0.117 , 0.117], 
        ['M' , 0.8  , 11    , 0.333 , 0.333], 
        ['N' , 1.35 , 15    , 0.183 , 0.183], 
        ['O' , 0.7  , 10    , 0.117 , 0.117]
    ]


r_list = []
result = 0


def func_dp():
    '''dp 프로그램은 재귀함수를 사용하여 반복적으로 발생하는 문제를 해결하는 것이다.'''
    num_list = []  #순서키 정렬
       
    
    for x in data:
        num_list.append(x[2] )  #순서치 넣기
    
    num_list = sorted(set(num_list))    # 중복데이터 제거와 순서 정렬
    
    
    def rfunc( num ):
        '''재귀함수'''
        temp = [];
        
        for x in data:
            if( x[2] == num_list[num] and len(temp)==0 ):   # 새로운 행번호일경에 공정과 시간을 계산해서 넣는다.                
                temp.append( x[0] ) # 공정 입력
                temp.append( x[ 1 ] + x[3] + x[4] ) # 시간 산출
            elif( x[2] == num_list[num] and temp[1] > ( x[ 1 ] + x[3] + x[4] ) ): # 같은 공정번호를 가진것이 존재하면 기존 시간과 비교해서 더 작은 값의 공정과 시간을 넣는다.
                temp = [] # 초기화
                temp.append( x[0] ) # 공정 넣기
                temp.append( x[ 1 ] + x[3] + x[4] ) # 시간 넣기
        
        global r_list # 글러벌 변수
        global result # 글러벌 변수
        
        r_list.append(temp) # 글러벌 변수에 넣기
        result = result + temp[1] # 글러벌 변수에 넣기
        
        if( num_list[num] != num_list[-1] ):    # 마지막번호가 아니면 기존번호에 1을 더해서 함수를 다시 호출한다.
            rfunc( num+1 )
        
         
    rfunc( 0 )  #최초의 재귀함수 호출
    
    print( '최적합 경로 출력' )
    for x in r_list:
        print(x)
    print( '결과 시간 : ',result )
    print( '-'*100 )
    

f2_mark_a = [''] #기계a
f2_val_a = [0] #기계a
f2_mark_b = [''] #기계b
f2_val_b = [0] #기계b 
f2_list = []
f2_result = []
f2_move = []
def func2():
    '''함수2'''
    global data
    
    print('작업리스트')
    for x in data:
        print(x)
        
    num_list = []  #순서키 정렬
    for x in data:
        num_list.append(x[2] )  #순서치 넣기    
    num_list = sorted(set(num_list))    # 중복데이터 제거와 순서 정렬    
    
    

    
    def func2_2(num):
        temp=[]
        global f2_mark_a    #a기계 공정 완료 리스트
        global f2_val_a     #a기계 작업 시간 리스트
        global f2_mark_b    #b기계 공정 완료 리스트
        global f2_val_b     #b기계 작업 시간 리스트
        global f2_list      #전체 작업 리스트
        global f2_result
        global f2_move

        
        for x in data:#순서 선별
            if( x[2] == num_list[num] ):   # 새로운 행번호일경에 공정과 시간을 계산해서 넣는다.                
                temp.append(x)
        
        while True:
            '''선별된 작업이 끝날때까지 반복한다.'''
            ml = []
            for i in temp:
                '''공정 리스트 작성'''
                ml.append(i[0])
            
            #print('반복되는건가?')
            for x in temp:
                #print(x)
                #print(ml)        
                #print('a기계 : ',f2_mark_a)
                #print('b기계 : ',f2_mark_b)        
                #print( (len((set(ml) & set(f2_mark_a))) == 0)  and  (len((set(ml) & set(f2_mark_b))) == 0) )
                if(  len((set(ml) & set(f2_mark_a))) == 0  and  len((set(ml) & set(f2_mark_b))) == 0  ):
                    '''a,b 기계에 작업이 없었다면 처음 이동한것으로 확인 하여 작업시간에 이동시간을 넣는다.'''
                    if( sum(f2_val_a) <= sum(f2_val_b) ):
                        '''a기계의 작업 시간을 산정해서 작으면 여기에 넣는다.  '''
                        if( x[2] != 0 ):
                            f2_mark_a.append( str(x[0]) +'공정 이동')
                            f2_val_a.append( x[1] )
                            f2_list.append( str(x[0]) +'공정 이동' )
                            f2_mark_b.append( '' )
                            f2_val_b.append( 0 )
                        
                        if( (x[0] ==  f2_mark_b[-1] ) and ( sum(f2_val_a) < sum(f2_val_b)  ) ):
                            '''a기계와 b기계에 동시 돌경우를 판단한다. 유휴 시간을 넣는다.'''                            
                            f2_mark_a.append( '유휴시간' )
                            f2_val_a.append( sum(f2_val_b) - sum(f2_val_a)  )
                            f2_mark_b.append( '' )
                            f2_val_b.append( 0 )
                            f2_list.append( '유휴시간' )
                        
                        f2_mark_a.append( str(x[0]) )
                        f2_val_a.append( x[-2] )
                        f2_mark_b.append( '' )
                        f2_val_b.append( 0 )
                        f2_list.append( str(x[0]) +'공정 =a기계' )
                    else:
                        '''a기계의 작업 시간일 길면 이쪽을 수행'''
                        if(x[2] != 0):
                            f2_mark_a.append( '')
                            f2_val_a.append( 0 )
                            f2_mark_b.append( str(x[0]) +'공정 이동' )
                            f2_val_b.append( x[1] )                            
                            f2_list.append( str(x[0]) +'공정 이동' )

                        if( (x[0] ==  f2_mark_a[-1]) and ( sum(f2_val_b) < sum(f2_val_a)  ) ):
                            '''a기계와 b기계에 동시 돌경우를 판단한다. 유휴 시간을 넣는다.'''
                            f2_mark_a.append( '' )
                            f2_val_a.append( 0 )
                            f2_mark_b.append( '유휴시간' )
                            f2_val_b.append( sum(f2_val_a) - sum(f2_val_b)  )
                            f2_list.append( '유휴시간' )
                                
                        f2_mark_a.append( '')
                        f2_val_a.append( 0 )
                        f2_mark_b.append( str(x[0]) )
                        f2_val_b.append( x[-1] )                        
                        f2_list.append( str(x[0]) +'공정 =b기계' )
                        
                        
                else:
                    '''이동 시간을 등록하지 않고 수행하는 부분'''    
                    if( sum(f2_val_a) <= sum(f2_val_b) ):
                        '''a기계가 작업시간이 작다면 수행'''
                        if( not(x[0] in f2_mark_a) ):
                            '''a기계 작업 리스트에 공정이 없다면 등록'''
                            if( (x[0]  == f2_mark_b[-1]) and ( sum(f2_val_a) < sum(f2_val_b)  ) ):
                                '''a기계와 b기계에 동시 돌경우를 판단한다. 유휴 시간을 넣는다.'''                            
                                f2_mark_a.append( '유휴시간' )
                                f2_val_a.append( sum(f2_val_b) - sum(f2_val_a)  )
                                f2_mark_b.append( '' )
                                f2_val_b.append( 0 )
                                f2_list.append( '유휴시간' )
                                                        
                            f2_mark_a.append( x[0])
                            f2_val_a.append( x[-2] )                                                        
                            f2_mark_b.append( '')
                            f2_val_b.append( 0 )
                            f2_list.append( str(x[0]) +'공정 =a기계' )
                            
                        elif( not(x[0] in f2_mark_b) ):
                            if( (x[0] ==  f2_mark_a[-1]) and ( sum(f2_val_b) < sum(f2_val_a)  ) ):
                                '''a기계와 b기계에 동시 돌경우를 판단한다. 유휴 시간을 넣는다.'''
                                f2_mark_a.append( '' )
                                f2_val_a.append( 0 )
                                f2_mark_b.append( '유휴시간' )
                                f2_val_b.append( sum(f2_val_a) - sum(f2_val_b)  )
                                f2_list.append( '유휴시간' )
                            
                            f2_mark_a.append( '')
                            f2_val_a.append( 0 )                            
                            f2_mark_b.append( x[0])
                            f2_val_b.append( x[-1] )                            
                            f2_list.append( str(x[0]) +'공정 =b기계' )                            
                                                
                    elif( sum(f2_val_a) > sum(f2_val_b) ):                    
                        '''b기계가 작업 시간이 작다면 수행'''
                        if( not(x[0] in f2_mark_b) ):
                            '''b기계작업 리스트에 공정이 없다면 등록'''
                            if( (x[0] ==  f2_mark_a[-1] ) and ( sum(f2_val_b) < sum(f2_val_a)  ) ):
                                '''a기계와 b기계에 동시 돌경우를 판단한다. 유휴 시간을 넣는다.'''
                                f2_mark_a.append( '' )
                                f2_val_a.append( 0 )
                                f2_mark_b.append( '유휴시간' )
                                f2_val_b.append( sum(f2_val_a) - sum(f2_val_b)  )
                                f2_list.append( '유휴시간' )
                            
                            f2_mark_a.append( '')
                            f2_val_a.append( 0 )
                            f2_mark_b.append( x[0])
                            f2_val_b.append( x[-1] )
                            f2_list.append( str(x[0]) +'공정 =b기계' )
                        elif( not(x[0] in f2_mark_a) ):
                            if( (x[0]  ==  f2_mark_b[-1]) and ( sum(f2_val_a) < sum(f2_val_b)  ) ):
                                '''a기계와 b기계에 동시 돌경우를 판단한다. 유휴 시간을 넣는다.'''                            
                                f2_mark_a.append( '유휴시간' )
                                f2_val_a.append( sum(f2_val_b) - sum(f2_val_a)  )
                                f2_mark_b.append( '' )
                                f2_val_b.append( 0 )
                                f2_list.append( '유휴시간' )
                            
                            f2_mark_a.append( x[0])
                            f2_val_a.append( x[-2] )
                            f2_mark_b.append( '')
                            f2_val_b.append( 0 )
                            f2_list.append( str(x[0]) +'공정 =a기계' )
            
            if( len(set(ml) & set(f2_mark_a) & set(f2_mark_b)) == len(ml) ):
                break
        
        if( num_list[num] != num_list[-1] ):    # 마지막번호가 아니면 기존번호에 1을 더해서 함수를 다시 호출한다.
            func2_2( num+1 )
             
                
        
    
    func2_2(0)
    
    print('a기계 리스트 : ',f2_mark_a)
    print('b기계 리스트 : ',f2_mark_b) 
    print('전체 리스트 : ',f2_list)    
    print('a', sum(f2_val_a) , f2_val_a)
    print( 'a runningsum', list(cumsum(f2_val_a)) )
    print('b' , sum(f2_val_b) , f2_val_b)
    print('b runningsum', list(cumsum(f2_val_b)) )
    print( '전체 공정 시간 :', max(sum(f2_val_a) , sum( f2_val_b )) )
    
        
                 
def func3():
    '''data를 랜덤으로 섞고 실행한다.'''
    d = [
        ['A' , 0.2  , 1     , 0.15  , 0.15], 
        ['B' , 0.5  , 6     , 0.183 , 0.183], 
        ['C' , 0.4  , 4     , 0.5   , 0.5], 
        ['D' , 0.6  , 8     , 0.267 , 0.267], 
        ['E' , 0.4  , 4     , 0.5   , 0.5], 
        ['F' , 0.35 , 2     , 0.35  , 0.35], 
        ['G' , 0.6  , 8     , 0.417 , 0.417], 
        ['H' , 0.35 , 2     , 0.583 , 0.583], 
        ['I' , 0.5  , 6     , 0.35  , 0.35], 
        ['J' , 0.8  , 11    , 0.35  , 0.35], 
        ['K' , 1.2  , 14    ,  0.5  , 0.5], 
        ['L' , 0.95 , 13    , 0.117 , 0.117], 
        ['M' , 0.8  , 11    , 0.333 , 0.333], 
        ['N' , 1.35 , 15    , 0.183 , 0.183], 
        ['O' , 0.7  , 10    , 0.117 , 0.117]
    ]
    global data
    r = randint(1, 15)    
    
    random.shuffle( d )
    for x in d:
        x[2]=0
    data = d[0:r]
    
    funcfin()


    
        
def funcfin():
    '''함수2'''
    global data
    
    print('작업리스트')
    for x in data:
        print(x)
        
    num_list = []  #순서키 정렬
    for x in data:
        num_list.append(x[2] )  #순서치 넣기    
    num_list = sorted(set(num_list))    # 중복데이터 제거와 순서 정렬    
    
    
    

    
    def funcfin_2(num):
        temp=[]
        global f2_mark_a    #a기계 공정 완료 리스트
        global f2_val_a     #a기계 작업 시간 리스트
        global f2_mark_b    #b기계 공정 완료 리스트
        global f2_val_b     #b기계 작업 시간 리스트
        global f2_list      #전체 작업 리스트
        global f2_result
        global f2_move

        
        for x in data:#순서 선별
            if( x[2] == num_list[num] ):   # 새로운 행번호일경에 공정과 시간을 계산해서 넣는다.                
                temp.append(x)
        temp = sorted(temp, key = lambda x : ( x[-1]) , reverse=True)
        while True:
            '''선별된 작업이 끝날때까지 반복한다.'''
            ml = []
            for i in temp:
                '''공정 리스트 작성'''
                ml.append(i[0])
            
            #print('반복되는건가?')
            for x in temp:
                #print(x)
                #print(ml)        
                #print('a기계 : ',f2_mark_a)
                #print('b기계 : ',f2_mark_b)        
                #print(x[0],max(sum(f2_val_a) , sum(f2_val_b)) , max(sum(f2_val_a) , sum(f2_val_b)) < x[1] , x[1])
                if(  max(sum(f2_val_a) , sum(f2_val_b)) < x[1]  and  not(x[0] in (set(f2_mark_a) & set(f2_mark_b))) and sum(f2_val_a) <= sum(f2_val_b) ):
                    '''a,b 기계에 작업이 없었다면 처음 이동한것으로 확인 하여 작업시간에 이동시간을 넣는다.'''
                    if( sum(f2_val_a) <= sum(f2_val_b) ):
                        '''a기계의 작업 시간을 산정해서 작으면 여기에 넣는다.  '''
                        if( x[2] != 0 ):
                            f2_mark_a.append( str(x[0]) +'공정이동')
                            f2_val_a.append( x[1] )
                            f2_list.append( str(x[0]) +'공정이동' )
                        
                        if( len(f2_mark_b) ==0 or ( (x[0] ==  f2_mark_b[-1] ) and ( sum(f2_val_a) < sum(f2_val_b)  ) ) ):
                            '''a기계와 b기계에 동시 돌경우를 판단한다. 유휴 시간을 넣는다.'''                            
                            f2_mark_a.append( '유휴시간' )
                            f2_val_a.append( sum(f2_val_b) - sum(f2_val_a)  )
                            f2_list.append( '유휴시간' )
                        
                        f2_mark_a.append( str(x[0]) )
                        f2_val_a.append( x[-2] )
                        f2_list.append( str(x[0]) +'공정 =a기계' )
                    elif( max(sum(f2_val_a) , sum(f2_val_b)) < x[1]  and  not(x[0] in (set(f2_mark_a) & set(f2_mark_b))) and sum(f2_val_a) > sum(f2_val_b) ):
                        '''a기계의 작업 시간일 길면 이쪽을 수행'''
                        if(x[2] != 0):
                            f2_mark_b.append( str(x[0]) +'공정이동' )
                            f2_val_b.append( x[1] )                            
                            f2_list.append( str(x[0]) +'공정이동' )

                        if( (x[0] ==  f2_mark_a[-1]) and ( sum(f2_val_b) < sum(f2_val_a)  ) ):
                            '''a기계와 b기계에 동시 돌경우를 판단한다. 유휴 시간을 넣는다.'''
                            f2_mark_b.append( '유휴시간' )
                            f2_val_b.append( sum(f2_val_a) - sum(f2_val_b)  )
                            f2_list.append( '유휴시간' )
                                
                        f2_mark_b.append( str(x[0]) )
                        f2_val_b.append( x[-1] )                        
                        f2_list.append( str(x[0]) +'공정 =b기계' )
                        
                        
                else:
                    '''이동 시간을 등록하지 않고 수행하는 부분'''    
                    if( sum(f2_val_a) <= sum(f2_val_b) ):
                        '''a기계가 작업시간이 작다면 수행'''
                        if( not(x[0] in f2_mark_a) ):
                            '''a기계 작업 리스트에 공정이 없다면 등록'''
                            if(  (x[0]  == f2_mark_b[-1]) and ( sum(f2_val_a) < sum(f2_val_b)  ) ):
                                '''a기계와 b기계에 동시 돌경우를 판단한다. 유휴 시간을 넣는다.'''                            
                                f2_mark_a.append( '유휴시간' )
                                f2_val_a.append( sum(f2_val_b) - sum(f2_val_a)  )
                                f2_list.append( '유휴시간' )
                                                        
                            f2_mark_a.append( x[0])
                            f2_val_a.append( x[-1] )                                                        
                            f2_list.append( str(x[0]) +'공정 =a기계' )
                            
                        elif( not(x[0] in f2_mark_b) ):
                            if( (x[0] ==  f2_mark_a[-1]) and ( sum(f2_val_b) < sum(f2_val_a)  ) ):
                                '''a기계와 b기계에 동시 돌경우를 판단한다. 유휴 시간을 넣는다.'''
                                f2_mark_b.append( '유휴시간' )
                                f2_val_b.append( sum(f2_val_a) - sum(f2_val_b)  )
                                f2_list.append( '유휴시간' )
                           
                            f2_mark_b.append( x[0])
                            f2_val_b.append( x[-1] )                            
                            f2_list.append( str(x[0]) +'공정 =b기계' )                            
                                                
                    elif( sum(f2_val_a) > sum(f2_val_b) ):                    
                        '''b기계가 작업 시간이 작다면 수행'''
                        if( not(x[0] in f2_mark_b) ):
                            '''b기계작업 리스트에 공정이 없다면 등록'''
                            if( (x[0] ==  f2_mark_a[-1] ) and ( sum(f2_val_b) < sum(f2_val_a)  ) ):
                                '''a기계와 b기계에 동시 돌경우를 판단한다. 유휴 시간을 넣는다.'''
                                f2_mark_b.append( '유휴시간' )
                                f2_val_b.append( sum(f2_val_a) - sum(f2_val_b)  )
                                f2_list.append( '유휴시간' )
                            
                            f2_mark_b.append( x[0])
                            f2_val_b.append( x[-1] )
                            f2_list.append( str(x[0]) +'공정 =b기계' )
                        elif( not(x[0] in f2_mark_a) ):
                            if( (x[0]  ==  f2_mark_b[-1]) and ( sum(f2_val_a) < sum(f2_val_b)  ) ):
                                '''a기계와 b기계에 동시 돌경우를 판단한다. 유휴 시간을 넣는다.'''                            
                                f2_mark_a.append( '유휴시간' )
                                f2_val_a.append( sum(f2_val_b) - sum(f2_val_a)  )
                                f2_list.append( '유휴시간' )
                            
                            f2_mark_a.append( x[0])
                            f2_val_a.append( x[-1] )
                            f2_list.append( str(x[0]) +'공정 =a기계' )
            
            if( len(set(ml) & set(f2_mark_a) & set(f2_mark_b)) == len(ml) ):
                break
        
        if( num_list[num] != num_list[-1] ):    # 마지막번호가 아니면 기존번호에 1을 더해서 함수를 다시 호출한다.
            funcfin_2( num+1 )
             
                
        
    
    funcfin_2(0)
    
    print('a기계 리스트 : ',f2_mark_a)
    print('b기계 리스트 : ',f2_mark_b) 
    print('전체 리스트 : ',f2_list)    
    print('a', sum(f2_val_a) , f2_val_a)
    print( 'a runningsum', list(cumsum(f2_val_a)) )
    print('b' , sum(f2_val_b) , f2_val_b)
    print('b runningsum', list(cumsum(f2_val_b)) )
    print( '전체 공정 시간 :', max(sum(f2_val_a) , sum( f2_val_b )) )    
    



 


#문제 1번
print(('*'*50)+'1번 문제 시작'+('*'*50))
funcfin()  
print(('*'*50)+'1번 문제 끝'+('*'*50))
'''

#번제 2번
print(('*'*50)+'2번 문제 시작'+('*'*50))         
func3()
print(('*'*50)+'2번 문제 끝'+('*'*50))
'''    