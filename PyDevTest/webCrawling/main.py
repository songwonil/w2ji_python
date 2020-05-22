from bs4 import BeautifulSoup
import urllib.request
from urllib.error import URLError, HTTPError
from datetime import datetime , timedelta

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import requests


def diffDate(s_date , t_date):
    ''' 날짜 비교 '''
    a = datetime( int( s_date[0:4] ) , int( s_date[4:6] ) , int( s_date[6:8] ) , 0, 0, 0)
    b = datetime( int( t_date[0:4] ) , int( t_date[4:6] ) , int( t_date[6:8] ) , 0, 0, 0)
    return (a-b).days

def getHtml2(url):
    '''
    - 크름드라이버를 다운 받아야 한다.
    https://sites.google.com/a/chromium.org/chromedriver/downloads
    request 로 처리    
    '''
    browser = webdriver.Chrome('chromedriver')
    browser.implicitly_wait(10)
    browser.get(url)
    
    
    #res = requests.get(url)
    html = browser.page_source
    print( 'getHtml2',url , len(html) )    
    return html
   
    
def getHtml(url):
    ''' 페이지의 오류 점검  '''    
    try:
        print('start getHtml')
        hdr = {'User-Agent': 'Mozilla/5.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3', 'Accept-Encoding': 'none', 'Accept-Language': 'en-US,en;q=0.8', 'Connection': 'keep-alive'}


        req = urllib.request.Request( url , headers=hdr)
        ## url을 통해 해당 url에 들어 있는 내용들을 받는다.
        res = urllib.request.urlopen( req  , timeout=100)
        print('res.stats',res.status,url)
        
        contents = res.read().decode('utf-8')
        return contents
    except HTTPError as e:
        print('getHtml error HTTPError : ',url , e)
    except:
        print('getHtml error ')

        
    
    


def todayhumor( dday , cnt ):
    '''오늘의 유머 사이트 베오베 가져오기'''    
    page_num = str(cnt)
    print('cnt : ',cnt)
    get_url = 'http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page='+page_num
    
    res = getHtml2( get_url )
        
    ## 받은 내용을 html.parser로 우리가 볼 수 있게 파싱한다.
    soup = BeautifulSoup(res, "html.parser")
    
    #클래스만 가져오기
    lists = soup.find_all( attrs={'class':'view list_tr_humordata'} )    
    
    #
    list_chk = 0;   
        
    for list in lists:
        str_div     = 'todayhumor'
        str_url     = 'http://www.todayhumor.co.kr'+list.find( attrs={'class':'subject'}).find('a')['href'] #url값 
        str_subject = list.find( attrs={'class':'subject'}).find('a').get_text()
        str_name    = list.find( attrs={'class':'name'}).get_text()
        str_date    = ('20'+list.find( attrs={'class':'date'}).get_text()[0:8]).replace("/","") #substring과 replace처리
        str_hits    = list.find( attrs={'class':'hits'}).get_text()
        str_ok      = list.find( attrs={'class':'oknok'}).get_text()
        #print(str_url , str_date , list_chk , cnt)
        if list_chk <= 0 :
            list_chk = diffDate( dday , str_date )
    
    # 지정일자의 이전 일자가 아니면 다시 돌린다.
    if list_chk <= 0:
        todayhumor(dday , cnt+1)
    else:
        print('오늘의 유머 끝')
             
    

todayhumor('20200522',1)           

#getHtml2('http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=1')

