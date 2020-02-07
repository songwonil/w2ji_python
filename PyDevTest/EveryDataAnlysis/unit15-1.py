'''
unit 15 테이블 형태의 데이터를 쉽게 다루도록 도와주는 pandas 라이브러리
'''

def func1():
    '''1. pandas 간단한 예제'''
    import pandas as pd
    df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table')
    print(df[1])
    for i in df[1]:
        print(i)

func1()