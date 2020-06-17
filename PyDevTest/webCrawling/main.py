from bs4 import BeautifulSoup
import urllib.request
from urllib.error import URLError, HTTPError
from datetime import datetime , timedelta

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import requests

import pymysql
from openpyxl import Workbook
from openpyxl import load_workbook

import re

def getDbCon():
    '''db 연결체'''
    con = pymysql.connect(host='127.0.0.1', user='com', password='com01', db='com', charset='utf8')
    return con

def dbInsert(site , url , subject , nick_nm , w_date , hits , recommend):
    '''
    -DB 입력 처리
    '''
    conn = getDbCon()
    try:
        with conn.cursor() as curs:
            sql = 'INSERT INTO web_crawling( site, url, subject, nick_nm, w_date, hits, recommend, cdate) VALUES( %s , %s , %s , %s , %s , %s , %s , now())'
            curs.execute(sql, ( site , url , subject , nick_nm , w_date , hits , recommend ) )
        conn.commit()        
    finally:
        conn.close()
    

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

        
    
    


def todayhumor( dday , page ):
    '''오늘의 유머 사이트 베오베 가져오기'''    
    str_div     = 'todayhumor'
    page_num = str(page)
    get_url = 'http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page='+page_num
    
    res = getHtml2( get_url )
        
    ## 받은 내용을 html.parser로 우리가 볼 수 있게 파싱한다.
    soup = BeautifulSoup(res, "html.parser")
    
    #클래스만 가져오기
    lists = soup.find_all( attrs={'class':'view list_tr_humordata'} )    
    
    #
    list_chk = 0;   
        
    for list in lists:        
        str_url     = 'http://www.todayhumor.co.kr'+list.find( attrs={'class':'subject'}).find('a')['href'] #url값 
        str_subject = list.find( attrs={'class':'subject'}).find('a').get_text()
        str_name    = list.find( attrs={'class':'name'}).get_text()
        str_date    = ('20'+list.find( attrs={'class':'date'}).get_text()[0:8]).replace("/","") #substring과 replace처리
        str_hits    = list.find( attrs={'class':'hits'}).get_text().replace(",","")
        str_ok      = list.find( attrs={'class':'oknok'}).get_text().replace(",","")
        #print(str_url , str_date , list_chk , cnt)
        if dday == str_date:
            dbInsert( str_div , str_url , str_subject , str_name , str_date , str_hits , str_ok )
        
        if list_chk <= 0 :
            list_chk = diffDate( dday , str_date )
    
    # 지정일자의 이전 일자가 아니면 다시 돌린다.
    if list_chk <= 0:
        todayhumor(dday , page+1)
    else:
        print('오늘의 유머 끝')
             

def humoruniv(dday , page):   
    '''
    - 웃대 사이트 크롤링 
    '''
    str_div     = 'humoruniv'
    page_num = str(page)
    get_url = 'http://web.humoruniv.com/board/humor/list.html?table=pds&pg='+page_num
    res = getHtml2( get_url )        
    ## 받은 내용을 html.parser로 우리가 볼 수 있게 파싱한다.
    soup = BeautifulSoup(res, "html.parser")
    #print(soup)
    #
    #lists = soup.find_all( 'tr' , attrs={'id':'li_chk_pds'} )
    lists = soup.find_all( 'tr' , id=re.compile("^(li_chk_pds-)((?!:).)*$") ) # li_chk_pds- 로 시작하는 전부
    
    list_chk = 0;   
        
    for list in lists:
        #print(list)
        str_url     = 'http://web.humoruniv.com/board/humor/'+list.find( 'td',attrs={'class':'li_sbj'}).find('a')['href'] #url값
        str_subject = list.find( 'td' , class_='li_sbj').find('a').get_text().strip()
        str_subject1 = list.find( 'span' , class_='list_comment_num' ).get_text().strip()
        str_subject = str_subject[0: str_subject.find(str_subject1) ].replace(str_subject1,'').strip()
        str_name    = list.find( 'span' , class_='hu_nick_txt').get_text().strip()
        str_date    = list.find( 'span' , class_='w_date' ).get_text()[0:10].replace("-","") #substring과 replace처리
        str_hits    = list.find( 'td' , class_='li_und' ).get_text().strip().replace(",","")
        str_ok      = list.find( 'span' , class_='o' ).get_text().strip().replace(",","")
        str_no      = list.find( 'font' ).get_text().strip().replace(",","")
        str_ok      = int(str_ok) - int(str_no)
        
        
        if dday == str_date:
            dbInsert( str_div , str_url , str_subject , str_name , str_date , str_hits , str_ok )
        
        if list_chk <= 0 :
            list_chk = diffDate( dday , str_date )
        
           
    # 지정일자의 이전 일자가 아니면 다시 돌린다.
    if list_chk <= 0:
        humoruniv(dday , page+1)
    else:
        print('웃대 끝')


def battlepage(dday , page):   
    '''
    - 페틀페이비 크롤링 
    '''
    str_div     = 'battlepage'
    page_num = str(page)
    get_url = 'http://v12.battlepage.com/??=Board.Humor.Table&page='+page_num
    res = getHtml2( get_url )        
    ## 받은 내용을 html.parser로 우리가 볼 수 있게 파싱한다.
    soup = BeautifulSoup(res, "html.parser")
    #print(soup)
    #
    lists = soup.find_all( 'table' , class_='bp_board' )
    #lists = soup.find_all( 'tr' , id=re.compile("^(li_chk_pds-)((?!:).)*$") ) # li_chk_pds- 로 시작하는 전부
    
    
    list_chk = 0;   
        
    for list in lists:
        #str_notice = list.find( 'td' , class_='li_sbj').find('a').get_text().strip()
        
        
        print('-'*50)        
        print(list)
        print('-'*50)
        
        '''
        str_url     = 'http://web.humoruniv.com/board/humor/'+list.find( 'td',attrs={'class':'li_sbj'}).find('a')['href'] #url값
        str_subject = list.find( 'td' , class_='li_sbj').find('a').get_text().strip()
        str_subject1 = list.find( 'span' , class_='list_comment_num' ).get_text().strip()
        str_subject = str_subject[0: str_subject.find(str_subject1) ].replace(str_subject1,'').strip()
        str_name    = list.find( 'span' , class_='hu_nick_txt').get_text().strip()
        str_date    = list.find( 'span' , class_='w_date' ).get_text()[0:10].replace("-","") #substring과 replace처리
        str_hits    = list.find( 'td' , class_='li_und' ).get_text().strip().replace(",","")
        str_ok      = list.find( 'span' , class_='o' ).get_text().strip().replace(",","")
        str_no      = list.find( 'font' ).get_text().strip().replace(",","")
        str_ok      = int(str_ok) - int(str_no)
        '''
        '''
        if dday == str_date:
            dbInsert( str_div , str_url , str_subject , str_name , str_date , str_hits , str_ok )
        
        if list_chk <= 0 :
            list_chk = diffDate( dday , str_date )
        '''
        
        
    '''    
    # 지정일자의 이전 일자가 아니면 다시 돌린다.
    if list_chk <= 0:
        battlepage(dday , page+1)
    else:
        print('배틀페이지 끝')
    '''    

# 오늘의 유머 
#todayhumor('20200525',1) # 1페이지부터 시작

# 웃대
#humoruniv('20200525',0) #0페이지부터 시작

#배틀페이지
battlepage('20200525',1) # 1페이지부터시작
