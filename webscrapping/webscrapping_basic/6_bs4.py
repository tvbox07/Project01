import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)  # soup 객체에서 처음 발견되는 a element를 반환 
# print(soup.a.attrs) #  a element의 속성정보를 출력
# print(soup.a["href"]) #  a element의 href의 속성 정보를 출력

# print(soup.find("a", attrs={"class":"Nbtn_upload"} )) # class값이 Nbtn_upload 인 a element를 찾아줘
# print(soup.find(attrs={"class":"Nbtn_upload"})) # class값이 Nbtn_upload 인 어떤 element를 찾아줘

print(soup.find("li", attrs={"class": "rank01"}))
rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.text)
print("rank1 : " + str(rank1.a.get_text()))
# print(rank1.next_sibling)
# print(rank1.next_sibling.next_sibling.get_text())
# print(rank1.next_sibling.next_sibling.a.get_text())
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank2.a.get_text())
# print(rank3.a.get_text())

# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# print("rank1.parent : " + str(rank3.parent))
# print(rank1.find_next_sibling.a.get_text()) # error발생
rank2 = rank1.find_next_sibling("li")
# print("rank2 : " + str(rank2))
# print("rank2.get_text() : " + str(rank2.a.get_text())) # error발생
print("rank2.a.get_text() : " + str(rank2.a.get_text()))
rank3 = rank2.find_next_sibling("li")
# print("find_next_sibling : " + str(rank2.get_text()))
print("rank3 : " + str(rank3.a.get_text()))
rank4 = rank3.find_next_sibling()
print("rank4 : " + str(rank4.a.get_text()))
rank3 = rank4.find_previous_sibling("li")
print("rank3 : " + str(rank3.a.get_text()))


# <a onclick="nclk_v2(event,'rnk*p.cont','727188','4')"
#  href="/webtoon/detail?titleId=727188&amp;no=143"
#  title="취사병 전설이 되다-143화 : 작별인사">
# 취사병 전설이 되다-143화 : 작별인사</a>

webtoon = soup.find("a" , title="취사병 전설이 되다-143화 : 작별인사")
print(webtoon)
print(webtoon.get_text())