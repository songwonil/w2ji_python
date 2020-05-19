from bs4 import BeautifulSoup
import urllib.request


str = 'http://www.todayhumor.co.kr/board/list.php?table=bestofbest'
req1 = urllib.request.Request( str , headers={'User-Agent': 'Mozilla/5.0'})
url = req1
## url을 통해 해당 url에 들어 있는 내용들을 받는다.
res = urllib.request.urlopen(url).read()

## 받은 내용을 html.parser로 우리가 볼 수 있게 파싱한다.
soup = BeautifulSoup(res, "html.parser")

list = soup.find_all( attrs={'class':'view list_tr_humordata'} )#클래스만 가져오기

a=0
for ss in list:
    #print(a ,'' ,ss.select( '.subject'  ))
    #print(a ,'' ,ss.find( attrs={'class':'subject'}).find('a').get_text() )
    print(a ,'' ,ss.find( attrs={'class':'subject'}).find('a').get_text() )
    print(a ,'' ,ss.find( attrs={'class':'name'}).get_text() )
    print(a ,'' ,ss.find( attrs={'class':'date'}).get_text() )
    print(a ,'' ,ss.find( attrs={'class':'hits'}).get_text() )
    print(a ,'' ,ss.find( attrs={'class':'oknok'}).get_text() )
    a+=1   

#
#url : href
#제목 subject
#작성자 name
#조회수 hits
#좋아요 oknok
#날짜 date