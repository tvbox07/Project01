import re
import requests
from bs4 import BeautifulSoup

header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

for year in range(2011, 2022):

    # 2021년 영화순위
    # https://search.daum.net/search?w=tot&q=2021%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)

    res = requests.get(url, headers=header)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})
    print(images)

    for idx, image in enumerate(images):
        print(image["src"])

        # image_url =image["src"]
        # if image_url.startswith("//"):
        #     image_url = "https:" + image_url

        image_res = requests.get(image["src"])
        image_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:  #write binary
            f.write(image_res.content)

        # if idx >= 4: #상위 5개 이미지까지만 다운로드
        #     break
        if idx == 0: #상위 1개 이미지까지만 다운로드
            break

