import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=721433"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")


# 새 기숙사 만화의 첫페이지 title, link출력하기
# cartoons = soup.find_all("td", attrs={"class":"title"})

# title = cartoons[0].a.get_text()
# print(title)
# link = "https://comic.naver.com" + cartoons[0].a["href"]
# print(link)

# for cartoon in cartoons:
#     print(cartoon.a.get_text())
#     link = cartoon.a["href"]
#     print("https://comic.naver.com" + link)

# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

#평점정보 평균구하기
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
# star = cartoons[0].strong.get_text()
# print(star)

total_rates = 0
# count = 0
# for cartoon in cartoons:
#     # rate = cartoon.strong.get_text()
#     rate = cartoon.find("strong").get_text()
#     print("rate : "  + str(rate))
#     total_rates += float(rate)
#     count += 1
#     print("total_rates : " + str(total_rates))
#     average = total_rates/count
#     print("average_star_rating : " + str(average))

for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print("rate : " + str(rate))
    total_rates += float(rate)

print("전체 점수 : " , total_rates)
print("평균 점수 : " , total_rates / len(cartoons) )
