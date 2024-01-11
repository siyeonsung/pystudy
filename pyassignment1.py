import requests

naver = requests.get('https://www.naver.com') # https://www.naver.com 요청
weather = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=37.5582018&lon=126.9979742&appid=4ada87268facd87550e6a5126401fda4&units=metric') #openweathermap api 호출
weather_json = weather.json() #response json를 파이썬 딕셔너리로 변환
print(naver.text) #text로 되어있는 페이지 소스
print(weather_json['current']) #딕셔너리 current 접근

#get
# 1. 직접 입력해서 보내기
# url에 보내고자 하는 데이터를 입력해서 전송한다.
#URL_get = "https://search.naver.com/search.naver?query=%EA%B9%80%EC%9E%A5%ED%9B%88"
#response = requests.get(URL_get)
print(response.status_code)

# 2. dict 이용하기
URL_dict = "https://search.naver.com/search.naver"

param = { "query" : "김장훈"}
response = requests.get(URL_dict, params=param)
print(response.text)

#post
datas = {'key1': 'value1', 'key2': 'value2'}

r = requests.post('https://httpbin.org/post', data=datas)
print(r.text)

#bs4
from bs4 import BeautifulSoup

url = 'https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)