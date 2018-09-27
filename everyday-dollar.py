#매일 환율 정보 저장하기
from bs4 import BeautifulSoup
import urllib.request as req
import datetime

#HTML가져오기
url="https://finance.naver.com/marketindex/"
res=req.urlopen(url)

#HTML분석하기
soup=BeautifulSoup(res, 'html.parser')

#원하는 데이터 추출
price=soup.select_one('div.head_info > span.value').string
print("usd/krw",price)

#저장할 파일 이름 구하기
t=datetime.date.today() #오늘 날짜
fname=t.strftime("%y-%m-%d")+".txt" #strftime : 날짜 -> 스트링
with open(fname, "w", encoding="utf-8") as f:
    f.write(price)