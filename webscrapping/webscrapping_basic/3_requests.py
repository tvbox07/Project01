import requests

# res = requests.get("http://naver.com")
# res = requests.get("http://anadocoding.tistory.com") # 403서버접근 거브, 404서버요청페이지 못찾음.
# print(res)
# print("응답코드 : ", res.status_code) #200이면 정상

# if res.status_code == requests.codes.ok:
#     print("ok connection")
# else:
#     print("problem happened. [error code ", res.status_code, "]")

# res.raise_for_status()  # 실행에러시 에러 메시지 발생
# print("웹 스크래핑을 진행합니다.")

# res = requests.get("http://naver.com")
# res.raise_for_status
# print(len(res.text))
# with open("mynaver.html", "w",encoding="utf8") as f:
#     f.write(res.text)

# res = requests.get("http://google.com")
# res.raise_for_status
# print(len(res.text))
# with open("mygoogle.html", "w",encoding="utf8") as f:
#     f.write(res.text)

res = requests.get("https://www.daum.net/")
res.raise_for_status()
print(len(res.text))
with open("mydaum.html", "w", encoding="utf8") as f:
    f.write(res.text)