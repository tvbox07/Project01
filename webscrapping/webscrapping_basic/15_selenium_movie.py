import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies?utm_source=apac_med&utm_medium=hasem&utm_content=Oct0121&utm_campaign=Evergreen&pcampaignid=MKT-EDR-apac-kr-1003227-med-hasem-mo-Evergreen-Oct0121-Text_Search_BKWS-BKWS%7cONSEM_kwid_43700009359644016_creativeid_416407016592_device_c&gclid=Cj0KCQiA0p2QBhDvARIsAACSOOPXfqdoVyO0lh3e3oIbLAibCjCxPsnRNAs2Mz9oyazkjRjYbBiJK3AaAhq-EALw_wcB&gclsrc=aw.ds"
header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
}


res = requests.get(url, headers=header)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ULeU3b neq64b"})
print(len(movies))

# with open("movie.html", "w", encoding="utf8") as f:
#     # f.write(res.text)
#     f.write(soup.prettify()) # html 문서를 예쁘게 출력
i = 1
for movie in movies:
    title = movie.find("div", attrs={"class":"Epkrse"}).get_text()
    print(str(i) + " : " + title)
    i +=  1