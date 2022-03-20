# Project: 웹 스크래핑을 이용하여 나만의비서를 만드시오

# [조건]
# 1. 네이버에서 오늘 서울의 날씨정보를 가져온다
# 2. 헤드라인 뉴스 3건을 가져온다
# 3. IT뉴스 3건을 가져온다
# 4. 해커스 어학원 홈페이지에서 오늘의 영어 회하 지문을 가져온다

# [출력 예시]

# [오늘의 날씨]
# 흐림, 어제보다 00도 높아요
# 현재 00도 (최저 00 / 최고 00)
# 오전 강수확률 00% / 오후 강수확률 00%

# 미세먼지 00Ug/m3 좋음
# 초미세먼지 00 ug/m3 좋음

# [헤드라인 뉴스]
# 1. 무슨 무슨 일이...
# (링크 : http://...)
# 2. 어떤 어떤 일이..
# (링크 : http://...)
# 3. 어떤 어떤 일이..
# (링크 : http://...)

# [IT 뉴스]
# 1. 무슨 무슨 일이...
# (링크 : http://...)
# 2. 어떤 어떤 일이..
# (링크 : http://...)
# 3. 어떤 어떤 일이..
# (링크 : http://...)

# [오늘의 영어 회화]
# (영어 지문)
# Jason : What can I say!
# Kim : What do I do..

# (한글 지문)
# Jason : 어쩌겠어요.
# Kim : 어떻게 , 어떻게..

from venv import create
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

def create_soup(url):
    header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
    res = requests.get(url, headers=header)
    # res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_weather():

        # [오늘의 날씨]
# 흐림, 어제보다 00도 높아요
# 현재 00도 (최저 00 / 최고 00)
# 오전 강수확률 00% / 오후 강수확률 00%

# 미세먼지 00Ug/m3 좋음
# 초미세먼지 00 ug/m3 좋음
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
    # 흐림, 어제보다 00도 높아요
    cast = soup.find("p", attrs={"class":"summary"}).get_text()
    # 현재 00도 (최저 00 / 최고 00)
    curr_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text().strip()
    low_temp = soup.find("span", attrs={"class":"temperature_inner"}).get_text()
    # high_temp = soup.find("span", attrs={"class":"highest"}).get_text().replace("기온 ", "")
    # 오전 강수확률 00% / 오후 강수확률 00%
    rain_rate = soup.find("div", attrs={"class":"cell_weather"}).get_text().strip()
    # rain_rate_afternoon = soup.find("span", attrs={"class":"weather_inner"}).get_text()
    print(cast)
    print(curr_temp, "(", low_temp, ")")
    print("강수확률 ","(", rain_rate, ")" )

    url2 = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&pkid=227&qvt=0&query=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%20%EC%98%81%EB%93%B1%ED%8F%AC%EA%B5%AC%20%EC%97%AC%EC%9D%98%EB%8F%99%20%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80'
    soup = create_soup(url2)
    mise = soup.find_all("div", attrs={"class":"grade level1 _level"})[0].get_text()
    ultramise = soup.find_all("div", attrs={"class":"grade level1 _level"})[1].get_text()
    print("미세먼지  ", mise)
    print("초미세먼지 ", ultramise)
    print() # 마지막 줄 뛰우기

    #리스트, 딕셔너리, 텍스트를 사용해서 찾기
    # dust = soup.find("dl", attrs={"class":["indicator","dust"]})
    # dust = soup.find("dl", attrs={"class":"indicator", "id":"dust"})
    # dust = soup.find("dl", attrs={"class":"indicator", "id":"dust"}, text="미세먼지")
    # pm10 = soup.find_all("dd")[0].get_text()
    # pm25 = soup.find_all("dd")[1].get_text()
    # print("미세먼지 {}".format(pm10))
    # print("초미세먼지 {}".format(pm25))


# [헤드라인 뉴스]
# 1. 무슨 무슨 일이...
# (링크 : http://...)
# 2. 어떤 어떤 일이..
# (링크 : http://...)
# 3. 어떤 어떤 일이..
# (링크 : http://...)
def scrape_headline_news():
    #ex: 
    # print("[헤드라인 뉴스]")
    # url = "https://news.naver.com"
    # soup = create_soup(url)
    # news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3) 
    # # ***** 여러 리스트 중 limit 옵션을 설정해서 갯수를 제한 할 수 있다.
    # for index, news in enumerate(news_list):
    #     title = news.div.a.get_text() # 개별 태그를 나열해서 택스트를 얻을 수 있음
    #     title = news.find("a").get_text().strip()
    #     link = url + news.find("a")["href"]
    #     print("{}, {}".format(index+1, title))
    #     print("  (링크 : {}".format(link))
    # print()




    print("[헤드라인 뉴스]")
    # url = "https://news.naver.com/"
    # soup = create_soup(url)
    # journal = soup.find_all("div", attrs={"class":"cjs_ctitle _item_title"})
    # # print(journal)
    # news = soup.find_all("div", attrs={"class":"cjs_news_tw"})
    # # print(news)
    # # link = soup.find_all("a", attrs={"class":"cjs_news_a _cds_link"})["href"]
    # # print(link)
    # for i in range(5):
    #     print(i, " ", journal[i].get_text().strip())
    #     print(news[i].get_text().strip())
    #     # print( "(링크 : ", link[i] , ")")
 
    # url = "https://news.kbs.co.kr/common/main.html"
    # soup = create_soup(url)
    # headline = soup.find("li", attrs={"class":"top"})
    # title = headline.find("em", attrs={"class":"tit"}).get_text()
    # time = headline.find("span", attrs={"class":"time"}).get_text()
    # link = headline.find("a")["href"].strip()
    # link = "http://news.kbs.co.kr"+link
    # print("[KBS] : ", title)
    # print("(", time, ")")
    # print("(링크 : ", link, ")")
    
    url = "https://imnews.imbc.com/pc_main.html"
    soup = create_soup(url)
    # print(soup)
    headline = soup.find("div", attrs={"class":"news_header"})
    # title = soup.find("div", attrs={"class":"top_title ellipsis"})
    # time = headline.find("span", attrs={"class":"time"}).get_text()
    # link = soup.find("a")["href"].strip()
    # link = "http://news.kbs.co.kr"+link
    # print("[MBC] : ", title)
    # print("(", time, ")")
    # print("(링크 : ", link, ")")
    print(headline)


def print_news(index, title, link): #출력을 함수로 따로 만듬
    print("{}. {}".format(index+1, title))
    print("   (링크 : {}".format(link))

def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"cluster_list"}).find_all("li", limit=3)
    for index, news in enumerate(news_list):
        #뉴스에서 이미지가 있으면 인덱스를 0이 아닌 1을 반환해서
        #이미지 다음의 텍스트를 헤드라인으로 반환
        a_idx = 0
        img = news.find("img")
        if img: 
            a_idx = 1
        # title = news.find_all("a")[a_idx].get_text().strip()
        # link = news.find("a")[a_idx]["href"]
        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        print_news(index, title, link)
    print()

def scrape_english():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    # contents = soup.find_all("div", attrs={"class":"conv_txt"})
    # print(content)
    # for word in enumerate(content):
    #     content = word.text()
    #     print(content)
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]: #8문장이 있다고 가정할 경우 5~8까지 가져옴
        #2로 나눠 몫만 취하고 그 숫자 부터끝까지
        print(sentence.get_text().strip())
    
    print()
    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]: #8문장이 있다고 가정할 경우 5~8까지 가져옴
        #2로 나눠 몫만 취하고 그 숫자 전까지
        print(sentence.get_text().strip())

    
    print()

if __name__ == "__main__": # main 일때 실행
    scrape_weather() # 오늘의 날씨 정보 가져오기
    scrape_headline_news() # 헤드라인 뉴스 가져오기
    scrape_it_news() # IT 뉴스 정보 가져오기
    scrape_english()