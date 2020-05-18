import openpyxl
import math

def get_data_from_excel(filename):
    '''
    엑셀 파일에서 데이터를 가져옵니다.
    반환값은 key가 학생 이름이고 value가 점수인 딕셔너리 입니다.
    '''
    dic = {}
    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    g = ws.rows
    
    for name , score in g:
        dic[name.value] = score.value
    
    return dic

datas = get_data_from_excel('class2_3.xlsx')


def average(values):
    '''평균'''
    s = 0
    for v in values:
        s += v
    return round( s / len(values) , 1 )

def variance(scores , avrg):
    '''분산 '''
    s = 0
    for score in scores:
        s += (score - avrg)**2
    return round( s/len(scores) , 1)

def std_dev(variance):
    '''편차'''
    return round(math.sqrt(variance),1)

print( average(average) ,  )


