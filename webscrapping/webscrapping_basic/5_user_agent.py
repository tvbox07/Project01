import requests
# url = "https://www.daum.net/"
# header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
# res = requests.get(url, headers=header)

url = "http://nadocoding.tistory.com"
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
res = requests.get(url, headers=header)

res.raise_for_status()
print(res.text)
# with open("daum1.html", "w", encoding="utf8") as f:
#     f.write(res.text)
with open("mynadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)