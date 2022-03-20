print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)
print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5>10))
#애완동물을 소개해 주세요.
print("우리집 강아지의이름은 연탄이예요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True")


animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >=3


print("우리집 " + animal + "의 이름은 " + name + "이예요")

print(name + "는 "+ str(age) + "살이며, " + hobby + "을 아주 좋아해요")

print(name,"는 ",age,"살이며, ",hobby,"을 아주 좋아해요")

''' 여러줄을 주석처리 할 경우 작은 따옴표
를 이용해서
여러줄을 주석처리한다.'''

#  콤마를 사용하면 한칸 뛰어지면서 붙혀넣기가 된다.


print(name,  "는 ",  age  ,"살이며, ",  hobby  ,"을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))

station = ["사당", "신도림", "인천공항"]
print( station[0]+ "행 열차가 들어오고 있습니다.")
print( station[1]+ "행 열차가 들어오고 있습니다.")
print( station[2]+ "행 열차가 들어오고 있습니다.")

print(2**3) # 2^3 =8
print(5%3) # 5을 3으로 나눈 나머지 = 2
print(10%3) # 10을 3으로 나눈 나머지 = 1
print(5//3) # 5을 3으로 나눈 몫 = 1
print(10//3) # 10을 3으로 나눈 몫 = 3

print(10>3) # true
print( 4 >= 7) # false
print(10 < 3) # False
print(5 <= 5) # True

print(3 == 3) # True
print(4 == 2) # False
print(3 + 4 == 7) # True

print(1 != 3) # True
print(not(1 != 3)) # False


print((3>0) & (3<5)) # True
print((3 > 0) and (3 < 5)) # True

print((3 > 0) | (3 > 5)) # True
print((3>0) or (3>5)) # True

print(5>4>3) #True
print(5>4>7) #False

print(2+3*4) #24
print((2+3)*4) #20
number = 2 + 3 * 4  #14
print("2+3*4 = "+ str(number))
number += 2 #16
print(number) 

print(abs(-5)) #5
print(pow(4, 2)) # 4^2=4*4=16
print(max(5,12)) #12
print(min(5, 12)) #5
print(round(3.14)) #3
print(round(4.00)) #4

from math import *
print(floor(4.99)) #4
print(ceil(3.14)) #4
print(sqrt(16)) #4

from random import *
print(random()) #0.0~1.0 미만의 임의의 값 생성
print(random()*10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random()*10)) # 0 ~ 10 미만의 의의의 값 생성
print(int(random()*10))
print(int(random()*10))
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성

print(int(random() * 45) + 1) # 1~45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1~45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1~45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1~45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1~45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1~45 이하의 임의의 값 생성

print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성

print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성


s_day = randint(4, 28)
print("오프라인 스타디 모임 날짜는 매월" + str(s_day) +"일로 선정되었습니다.")
print(f"오프라인 스타디 모임 날짜는 매월 {s_day} 일로 선정되었습니다." , s_day)

#문자열
sentence1 = ' I am a man.'
sentence2 = " I am a boy."
sentence3 = """
I am a girl.
I am ambitious.

///


"""

print(sentence1)
print(sentence2)
print(sentence3)

#슬라이싱

jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("년 : " + jumin[0:2]) # 0부터 2 직전까지(0,1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리(뒤에서부터)" + jumin[-7:])

#문자열 처리함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(python[0].islower())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n") #문자 n의 위치
print(index)
index = python.index("n", index+1) #문자 두번째 n의 위치 
print(index)

index2=python.find("n")
# print(python.find("n"))
print(index2)
print(python.find("n", index2+1))
print(python.find("Java")) # 없는 문자일 경우 -1을 반환
# print(python.index("java")) #문자가 없는 경우 에러를 냄

print(python.count("n")) # 위 문장에 n이 몇개인지 숫자를 반환

#문자열 포맷
print("a" + "b ")
print('a' + 'b')

#방법1

print("나는 %d살 입니다." %20) #decimal 정수
print("나는 %d살 입니다." %20.5) #decimal 정수
print("나는 %f살 입니다." %20.5) #float 실수
print("나는 %s살 입니다." %20.5) # string으로 인식
print("나는 %s을 좋아해요." % "파이썬") # string 문장
print("Apple은 %c로 시작해요." % "A") #character 1글자

print("나는 %s색과 %s색을 좋아 합니다." %("파랑", "빨간"))

#방법2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아 합니다." .format("파랑", "빨간"))
print("나는 {0}색과 {1}색을 좋아 합니다." .format("파랑", "빨간"))
print("나는 {1}색과 {0}색을 좋아 합니다." .format("파랑", "빨간"))

#방법 3
print("나는 {age}살이며, {color}색을 좋아해요" .format(age = 20, color ="빨간"))
print("나는 {color}살이며, {age}색을 좋아해요" .format(age = 20, color ="빨간"))

#방법 4 (v3.6이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

#탈출 문자
print("백문이 불여일견 백견이 불여일타")
print("백문이 불여일견 \n 백견이 불여일타") #줄바꿈 \n
# print("저는 "나도코딩" 입니다.")  #에러발생
print('저는 "나도 코딩"입니다')
print("저는 \"나도코딩\"입니다.") #문장내에서 따옴표 \" \'

# \\ :문장 내에서는 \

print("E:\Coding\PythonEducation") #하위 버전에서는 에러 아래와 같이해야 정상
print("E:\\Coding\\PythonEducation")
print("E:\Coding\PythonApplication\PythonApplication1")

# \r : 커서를 맨 앞으로 이동
print("Red  Apple \rPine")
# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")
# \t : tab
print("Red\t\t Apple")

"""
#퀴즈3
사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
예) http://naver.com
규칙1 : http://부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 =>naver 
규칙3 : 남은 글자 중 처음 세자리 +글자 갯수+ 글자내"e"갯수+"!" 로 구성
                    (nav)       (5)             (1)     (!)
예) 생성된 비밀번호 : nav51!
"""

input = "http://naver.com"
rule1 = input[7:]
print(rule1)
rule2_n = rule1.index(".")
print(rule2_n)
rule2 = rule1[:rule2_n]
print(rule2)
# rule3 = rule2[:3] + len(rule2) + rule2.count("e") + !
print(rule2[:3])
print(len(rule2))
print(rule2.count("e"))
rule3_1 = rule2[:3]
rule3_2 = len(rule2)
rule3_3 = rule2.count("e")
rule3 = rule3_1 + str(rule3_2) + str(rule3_3) + "!"
print(rule3)

url = "http://naver.com"
my_str = url.replace("http://", "") #규칙1
print(my_str)
my_str = my_str[:my_str.index(".")] #규칙2
print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다." .format(url, password))
print(f"{url}의 비밀번호는 {password} 입니다.")



#리스트[]

subway = ["유재석", "조세호", "박명수"]
print(subway)

print(subway.index("조세호"))

subway.append("하하")
print(subway)

subway.insert(1, "정형돈",)
print(subway)

print(subway.pop())
print(subway)
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)

subway.append("유재석")
print(subway)
print(subway.count("유재석"))
print(subway.index("유재석"))
# print(subway.sort())
subway.sort()
print(subway)
subway.reverse()
print(subway)

#정렬
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)
print(type(num_list[0]))

num_list = [5,2,4,3,1]
num_list =[str(x) for x in num_list]
num_list.sort()
print(num_list)
print(type(num_list[0]))

num_list = ["5","2","4","3","1"]
num_list.sort()
print(num_list)
print(type(num_list[0]))

num_list = ["5","2","4","3","1"]
num_list = [int(x) for x in num_list]
num_list.sort()
print(num_list)
print(type(num_list[0]))

num_list = ["5","2","4","3","1"]
num_list = list(map(int, num_list))
print(num_list)
print(type(num_list[0]))

num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

num_list.clear()
print(num_list)

#다양한 자료형 사용
num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]

mix_list.extend(num_list)
print(mix_list)


#사전 Dictionary key/value
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

# print(cabinet[5])  #오류발생 후 에러발생면서 정지
# print("hi")

print(cabinet.get(5)) #값이 없으면 none을 반환
print("hi2 get의 값이 없어도 실행")

value = cabinet.get(5)
print(value)

print(cabinet.get(5))
print(cabinet.get(5, "사용가능")) #디폴트값 반환
# print(cabinet[5]) #값이 없으므로 에러발생

print(3 in cabinet)  #true 키가 있는지를 물음 
print(5 in cabinet)  #False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

cabinet["A-3"] = "김종국"
cabinet["c-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())


#튜플

menu = ("돈까스", "치즈까스")
print(menu[0])

print(menu[1])

# menu.add("생선까스") #에러발생 튜플은 추가할 수 없음.
menu2 = ("생선까스") 
# menu.__add__(menu2)

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")

print(name, age, hobby)

#셋트(집합)
# 중복 안됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호","양세형"}
python = set(["유재석", "박명수"])

csharp = {"고고"}

#교집합, intersection(java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# print(java & csharp) # 반환이 없기에 에러 발생
print(java.intersection(csharp)) #반환이 없어도 반환
print(type(java.intersection(csharp))) #반환이 없어도 반환

# 합집합 (java할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

#차집합 (Java 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 잊었어요
java.remove("김태호")
print(java)

# 자료 구조의 변경
# 커피숖
menu02 = {"커피", "우유", "주소"}
print(menu02, type(menu02))

menu02 = list(menu02)
print(menu02, type(menu02))

menu02 = tuple(menu02)
print(menu02, type(menu02))

menu02 = set(menu02)
print(menu02, type(menu02))

# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle과 sample을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 키피 당첨자 : [2, 3, 4]
# -- 축하합니다 --


from random import *
import numpy

def createList(n):
    lst = []
    for i in range(1, n+1):
        lst.append(i)
    return(lst)
lst = createList(20)
print(lst)

lst02 = [i for i in range(1, 20+1)]
print(lst02)

import numpy as np
lst03 = list(np.arange(1, 20+1))
print(lst03)

# list = []
# print(list)
# i = list(range(1, 20))
# # list.append(i)
# print(i)


from random import *

print(lst)
# lst = str(lst)
print(type(lst))
shuffle(lst)
print(lst)
chicken_winner = sample(lst, 1)
print(chicken_winner)
print("치킨 당첨자 : " + str(chicken_winner[0]))
lst.remove(chicken_winner[0])

print(lst)

coffee_winner = sample(lst, 3)
print("커피 당첨자 : " + str(coffee_winner))

# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 키피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

print("-- 당첨자 발표--")
print("치킨 당첨자 : " + str(chicken_winner[0]))
print("커피 당첨자 : " + str(coffee_winner))
print("-- 축하합니다. --")


from random import *
users = range(1, 21)
print(type(users))
users = list(users)
print(type(users))
print(users)
shuffle(users)
print(users)
winners = sample(users, 4) # 4명 중 1명은 치킨, 3명은 커피

print(" -- 당첨자 발표 --")
print("치킨 당첨자 : {0}" .format(winners[0]))
print("커피 당첨자 : {0}" .format(winners[1:]))
print(f"치킨 당첨자 : {winners[0]}")
print(f"커피 당첨자 : {winners[1:]}")
print(" -- 축하합니다. --")

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

# weather = input("오늘의 날씨는 어때요?")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")  