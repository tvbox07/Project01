from sre_constants import REPEAT_ONE
import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=5&backgroundColor="
# res = requests.get(url)
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
res = requests.get(url, headers=header)

res.raise_for_status()
soup = BeautifulSoup(res.text , "lxml")
# print(res.text)

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# print(items[0])
# name01 = items[0].find("div" , attrs={"class":"name"})
# print(name01.get_text())
count = 0
for item in items:

    # 사전 예약 상품 제외
    pre_order = item.find("span", attrs={"class":"pre-order-badge-text"}) # pre-order-badge-text
    if pre_order:
        print(" <사전 예약 상품은 제외합니다.>")
        continue

    name = item.find("div", attrs={"class":"name"}).get_text() # 제품명
    
    # #삼성전자 제외
    # if "삼성전자" in name:
    #     print("삼성전자 상품 제외합니다")
    #     continue
    #     #LG전자 제외
    # if "LG전자" in name:
    #     print("LG전자 상품 제외합니다")
    #     continue
        #애플 제외
    if "애플" in name:
        print("애플 상품 제외합니다")
        continue

    price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격
   
    # 리뷰 100개 이상, 평점 4.5이상 되는 것만 조회
    rate = item.find("em", attrs={"class":"rating"})  # 평점
    if rate:
        rate = rate.get_text()
    else:
        rate = "평점 없음"
        continue
   
    rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) #평점수
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
        rate_cnt = rate_cnt[1:-1]
    else:
        rate_cnt = "평점 수 없음"
        continue
    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
        count += 1
        print(count , " : " ,name , price, rate, rate_cnt)

 