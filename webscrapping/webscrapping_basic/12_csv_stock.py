import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.naver?&page="
header ={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}

filename = "시가총액1_200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") #한글이 깨지지 않게 저장하기 utf-8-sig
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
#["N", "종목명", "현재가",....] 리스트 형태로들어감
print(type(title))
writer.writerow(title)

for page in range(1, 5):
    print(page)
   
    # url = url + str(page)
    # print(url)
    res = requests.get(url+str(page), headers=header)
    # res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: #의미 없는 데이터는 제외
            continue
        data = [column.get_text().strip() for column in columns]
        print(data)
        writer.writerow(data)