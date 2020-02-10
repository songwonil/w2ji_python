'''
https://hamait.tistory.com/735?category=132470
통계
- 데이트 매칭 회사로 사용자들이 몇 명의 친구를 가지고 있고, 
그것에 관해 어떤 내용들을 담고 있는지 설명해 달라고 데이터 분석팀에게 요청이 날라 왔다. 해결해볼까?
'''

'''
1. 일단 데이터 그 자체를 1차원 리스트로 보여줄수 있습니다.
'''
def func1():    
    num_friends = [100,40,30,54,25,3,100,100,100,3,3]
    print(num_friends)

'''
2. 동일한 친구수를 가진 사람들을 모아서 보여줍니다. 
보통 몇명의 친구들을 가지고 있는지?
100명의 친구를 가진 사람이 4명이고 3명의 친구를 가진 사람이 3명이면 100:4, 3:3 이렇게 보여준다.
'''
def func2():
    import collections
    num_friends = [100,40,30,54,25,3,100,100,100,3,3]
    friends_counts = collections.Counter(num_friends)
    print(friends_counts) 
    print(friends_counts[100])

'''
3. 차트를 이용해서 가시화 해서 보여주면 더 좋을것이다.
matplotlib를 사용한다.
'''
def func3():
    import collections
    import matplotlib.pyplot as plt
    num_friends = [100,40,30,54,25,3,100,100,100,3,3]
    friends_counts = collections.Counter(num_friends)
    print('friends_counts',friends_counts)
    xs = range(101)
    # 파이썬에는 이렇게 List구축을 할 수 있습니다. list comprehension 라고 말합니다.
    ys = [friends_counts[x] for x in xs] 
    plt.bar(xs,ys)
    plt.axis([0,101,0,10])
    plt.xlabel("# of friends")
    plt.ylabel("# of people")    
    plt.show()

'''
4. 가장 많은 친구수는? 가장 적은 친구 수는? 궁금합니다.
당연하게도 이런 통계치가 가장 기본적으로 필요합니다. ( len, max , min 함수를 사용합니다. )
'''
def func4():
    import collections    
    num_friends = [100,40,30,30,30,30,30,30,30,30,54,54,54,54,54,54,54,54,25,3,100,100,100,3,3]
    num_points = len(num_friends)
    print( 'len ', num_points )
    max_value = max(num_friends)
    print('max ', max_value)
    min_value = min(num_friends)
    print('min ',min_value)

'''
5. 조금 변형하여 두번째 혹은 세번째 많은 친구 수도 필요 할때가 있겠지요?
어떤 연속된 데이터에서 가장 크거나 가장 작은 값이 너무 튈경우 문제가 생길 수 있습니다.
따라서 두번째 큰수를 구하고 싶을때가  있는데요 이때는 정렬을 해서 사용할수 있습니다.
'''
def func5():
    #import collections
    num_friends = [100,40,30,30,30,30,30,30,30,30,54,54,54,54,54,54,54,54,25,3,100,100,100,3,3]
    print( '정렬 이전',num_friends )
    sorted_values = sorted(num_friends)
    print( '정렬 이후',sorted_values )
    val1 = sorted_values[1] #두번째로 작은값
    val2 = sorted_values[-2] #두번째로 큰값
    print( '두번째 작은' , val1)
    print( '두번째  큰' , val2)
    
'''
6. 회원들의 친구 수의 평균을 알고 싶습니다. 보통 몇명의 친구를 가지고 있을가요?
'''
def func6():
    #from __future__ import division #이것을 써주어야 값이 더 정확하게 계산된다네요.
    import numpy as np
    num_friends = [100,40,30,30,30,30,30,30,30,30,54,54,54,54,54,54,54,54,25,3,100,100,100,3,3]
    def mean(x):
        return sum(x) / len(x)
    
    avg = mean( num_friends )
    
    print(sum(num_friends) ,' / ' , len(num_friends) ,' = ',  avg )
    print( 1146 / 25 , np.average(num_friends) )

'''
7. 친구 수의 중앙값(median)을 알고 싶다. 중앙값은 머죠?
중간값은 보통 평균보다 더 내가 원하는 바를 잘 말해주곤 하느네요. 
미국 모 대학교 지리학과의 84년 졸업생의 평균 연봉은 어느 한 졸업생의 의해 크게 상승하였는데 
그 사람은 바로 마이클 조던 입니다.
그런 특이 케이스는 평균이라는 수치를 신뢰하게 어렵게 만듭니다. (회사의 누구 한 사람때문에 회사연봉이 크게 올라가는것 처럼) 
이럴 경우 중간값을 사용합니다.
중간값은 최고의 최소가 얼마나 크게 차이가 나는지는 전혀 중요치 않습니다.
'''
def func7():
    import numpy as np
    num_friends = [1200,15,10,10,9,4,3,3,2,1]
    avg = np.average(num_friends)
    print('평균 : ',avg)
    
    mid = np.median(num_friends)
    print('중앙값 : ',mid)
    
    
'''
8. 친구 수라는 데이터의 분포(산포도)는 어덯게 될까? 분산, 표준편차등을 알아보자
8-1 최대, 최소 사이의 범위
'''
def func8_1():
    import numpy as np
    num_friends = [100,15,10,10,9,4,3,3,2,1]    
    print( num_friends )
    print( max(num_friends) , min(num_friends) , max(num_friends) - min(num_friends)  )

'''
8-2 이상치를 제외하고 평범한 데이터 사이의 범위차이
상, 하위 25% 사이의 차이
'''
def func8_2():
    import numpy as np
    num_friends = [100,15,10,10,9,4,3,3,2,1]
    b= np.arange(0,101,25)
    a = np.percentile( num_friends , b )
    print(a[-2] - a[2])
    
'''
8-3. 분산(variance) : 데이터들 사이에 얼마나 차이가 큰가?
'''
def func8_3():
    import math
    import numpy as np
    num_friends = [100,15,10,10,9,4,3,3,2,1]
    val = np.var(num_friends)
    print('분산  : ',val)

'''
8-4. 표준편차(stand deviation) : 
분산은 데이터의 차이에 제곱을 해주기때문에 그 값을 sqrt를 해줘서 현실적으로 바꿔줌
'''
def func8_4():
    import numpy as np
    num_friends = [100,15,10,10,9,4,3,3,2,1]
    val = np.std(num_friends)
    print('표준편차 : ',val)
    
    
'''
9. 상관 관계 :
두 특성사이의 연관관계를 말해줌(친구의 수와 연봉간에 연관관계가 있을까요?)
9-1. 공분산( covariance )
다른 예를 들어 보면
- 사람들의 okky 싸이트의 접속 시간의 리스트가 있다고 하자
- 사이들의 경력기간 리스트가 있다고 하자.
위의 두가지 요소들 즉 접속시간이 길 수록 경력도 길다라는게 말이 될까?
이것을 알고 싶을때 사용하는게 공분산이다.
'''
def func9_1():
    ''' 
    -서로의 분산이 유사한 증가 혹은 감소 패턴을 보인다면 dot의 크기가 매우 커질것이다.
    -즉 리턴하는 값이 클 수록 상관고나계가 있다고 볼수 있다.
    -(하지만 위의 공분산도 데이터의 속성에 따라 잘못된 정보를  줄수 있음을 유념하자)    
    '''
    import numpy as np
    num_friends = [100,15,10,10,9,4,3,3,2,1]
    val = np.cov( num_friends )
    print('공분산 : ',val)

'''
9-2. 상관관계( correleation )
상관관계는 단위가 없으며 항상 -1 에서 1 사이 값을 갖는다.
예를 들어 상관관계가 0.25 라면 상대적으로 약한 양의 상관관계를 의미한다.
-1 혹은 1 에 가까울때 상관관계가 크다고 말할수 잇다.
'''
def func9_2():
    import numpy as np
    num_friends = [100,15,10,10,9,4,3,3,2,1]
    val = np.corrcoef(num_friends)
    print( val )




    