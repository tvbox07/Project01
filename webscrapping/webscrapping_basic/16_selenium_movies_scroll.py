# import requests
# from bs4 import BeautifulSoup

# url = "https://play.google.com/store/movies?utm_source=apac_med&utm_medium=hasem&utm_content=Oct0121&utm_campaign=Evergreen&pcampaignid=MKT-EDR-apac-kr-1003227-med-hasem-mo-Evergreen-Oct0121-Text_Search_BKWS-BKWS%7cONSEM_kwid_43700009359644016_creativeid_416407016592_device_c&gclid=Cj0KCQiA0p2QBhDvARIsAACSOOPXfqdoVyO0lh3e3oIbLAibCjCxPsnRNAs2Mz9oyazkjRjYbBiJK3AaAhq-EALw_wcB&gclsrc=aw.ds"
# header = {
#     "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
#     "Accept-Language":"ko-KR,ko"
# }


# res = requests.get(url, headers=header)
# res.raise_for_status()

# soup = BeautifulSoup(res.text, "lxml")

# movies = soup.find_all("div", attrs={"class":"ULeU3b neq64b"})
# print(len(movies))

# # with open("movie.html", "w", encoding="utf8") as f:
# #     # f.write(res.text)
# #     f.write(soup.prettify()) # html 문서를 예쁘게 출력
# i = 1
# for movie in movies:
#     title = movie.find("div", attrs={"class":"Epkrse"}).get_text()
#     print(str(i) + " : " + title)
#     i +=  1

from selenium import webdriver

#장치사용안함 지우기
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome("D:\Coding\PythonWorkspace02\chromedriver.exe", options=options)

# browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies?utm_source=apac_med&utm_medium=hasem&utm_content=Oct0121&utm_campaign=Evergreen&pcampaignid=MKT-EDR-apac-kr-1003227-med-hasem-mo-Evergreen-Oct0121-Text_Search_BKWS-BKWS%7cONSEM_kwid_43700009359644016_creativeid_416407016592_device_c&gclid=Cj0KCQiA0p2QBhDvARIsAACSOOPXfqdoVyO0lh3e3oIbLAibCjCxPsnRNAs2Mz9oyazkjRjYbBiJK3AaAhq-EALw_wcB&gclsrc=aw.ds"
browser.get(url)

# 지정한 위치로 스크롤 내리기
# 모니터(해상도) 높이 1080 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)")
# browser.execute_script("window.scrollTo(1080, 2160)")
# browser.execute_script("window.scrollTo(2160, 3240)")
# browser.execute_script("window.scrollTo(3240, 4320)")
# browser.execute_script("window.scrollTo(3420, 5400)")

# browser.execute_script("window.scrollTo(0, 5400)")

# 화면 가장 아래로 스코롤 내리기
pre_height = browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time

interval = 2 # 2초에 한번씩 스크롤 내림

#반복수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == pre_height:
        break
    pre_height = curr_height

print("스크롤 완료")   


browser.execute_script("window.scrollTo(0,0)")

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class":"ULeU3b neq64b"})
# movies = soup.find_all("div", attrs={"class":["ULeU3b neq64b","cXFu1"]})  #클래스 이름이 여러게 인경우 or 은 리스트로 만든다

# print(movies)
print(len(movies))

# with open("movie.html", "w", encoding="utf8") as f:
#     # f.write(res.text)
#     f.write(soup.prettify()) # html 문서를 예쁘게 출력
i = 1
for movie in movies:
    try:
        title = movie.find("div", attrs={"class":"Epkrse"}).get_text()  #클래스 이름이 여러게 인경우 or 은 리스트로 만든다
        print(str(i) + " : " + str(title))
        # print(str(i) + " : " + str(title.get_text()))
        i += 1
    except Exception as e:
        continue

movies2 = soup.find_all("div", attrs={"class":"cXFu1"}) # 
# movies = soup.find_all("div", attrs={"class":"Epkrse"})
# print(movies2)
print(len(movies2))
y = 1
for movie in movies2:
    try:
        title = movie.find("span", attrs={"class":"DdYX5"}).get_text()  #클래스 이름이 여러게 인경우 or 은 리스트로 만든다
        print(str(y) + " : " + str(title))
        # print(str(i) + " : " + str(title.get_text()))
        y += 1
    except Exception as e:
        continue

#할인하는 영화 찾기
print("-"*100)
print("할인된 영화 찾기", "-"*50)
z = 1
for movie in movies:
    try:
        title = movie.find("div", attrs={"class":"Epkrse"}).get_text()  #클래스 이름이 여러게 인경우 or 은 리스트로 만든다
        #할인 전 가격
        original_price = movie.find("span", attrs={"class":"SUZt4c P8AFK"})
        if original_price:
            original_price = original_price.get_text()
        else:
            # print(title, " <할인되지 않은 영화 제외>")
            continue
        
        #  할인된 가격
        price = movie.find("span", attrs={"class":"VfPpfd VixbEe"}).get_text()

        # 링크
        link = movie.find("a", attrs={"class": "Si6A0c ZD8Cqc"})["href"]
        # https://play.google.com + link

        print(f"{z} : 제목 :  {title}")
        print(f"할인 전 금액 : {original_price}")
        print(f"할인 후 금액 : {price}")
        print("링크 : ", "https://play.google.com" + link)
        print("-"*120)
        z += 1
     
    except Exception as e:
        continue

browser.quit()
# while(True):
#     pass
