import requests
from bs4 import BeautifulSoup
value=input("검색어 입력")
URL_get = "https://search.naver.com/search.naver?query="+value
response = requests.get(URL_get)
soup = BeautifulSoup(response.text,'html.parser') #string 집어넣기

for i in soup.select('.news_contents > a'): #css selector 사용-뉴스 class만 가져오기
    print(i.text) #글 출력
    print(i['href']) #a 태그 내 href 속성(링크) 출력

#멜론 top100

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"} 
html = requests.get("http://www.melon.com/chart/index.htm", headers=header)
soup=BeautifulSoup(html.text,'html.parser')
rank_list=[]
name_list=[]
for i in range(0,50):
    rank_list.append(soup.select('#lst50 > td:nth-child(2) > div > span.rank')[i].text)
    name_list.append(soup.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')[i].text)
for j in range(0, 50):
    rank_list.append(soup.select('#lst100 > td:nth-child(2) > div > span.rank')[j].text)
    name_list.append(soup.select('#lst100 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')[j].text)
for k in range(0,100):
    print(rank_list[k], end=' - ')
    print(name_list[k])

#css를 이용한 특정 순위 노래 불러오기
inputnumber=int(input("원하는 순위 입력 : "))
names=[]
for name in soup.select("#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a"):
    names.append(name.text)
for name in soup.select("#lst100 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a"):
    names.append(name.text)
print(names[inputnumber-1])

#아이로 시작하는 모든 가수의 모든 곡 불러오기(정규식 이용)
import re
research=re.compile('아이.') #re.compile: 문자열을 파이썬이 이해할 수 있는 언어로 컴파일해주는 함수
soup=BeautifulSoup(html.text,'html.parser')
songs=[]; singers=[]
for song in soup.select("#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a"):
    songs.append(song.text)
for song in soup.select("#lst100 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a"):
    songs.append(song.text)
for singer in soup.select("#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a"):
    singers.append(singer.text)
for singer in soup.select("#lst100 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a"):
    singers.append(singer.text)

for i in range(0,100):
    if research.search(singers[i]): #.search : 아이로 시작하는 가수명 찾기
        print(songs[i], singers[i])