# if

# weather = "비"
# # if 조건 :
# #     실행 명령문

# if weather == "비":
#     print("우산을 챙기세요")


# weather = "맑아요"
# if weather == "비":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")    

# weather=input("오늘의 날씨는 어떤가요? ")
# weather=weather.replace(" ", "")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")  


# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨예요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")

# for

# for waiting_no in range(1,6):
#     print("대기번호 : " + str(waiting_no))
#     print(f"대기 번호 : {waiting_no}")
#     print("대기 번 호 : {0}" .format(waiting_no))

# starbucks = ["아이언맨", "토르", "그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

# while
customer = "토르"
index = 5
while index >=1:
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피가 폐기처분되었습니다.")