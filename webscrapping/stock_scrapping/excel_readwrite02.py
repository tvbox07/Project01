# import pandas as pd

# # 한글 엑셀 불러올경우 pip install xlrd  필요
# xlxs = pd.read_excel('D:\Coding\PythonWorkspace02\webscrapping\stock_scrapping\유가증권.xls')

import pandas as pd
import os
import csv

#코스닥 리스트 불러오기
# 엑셀 읽기
a1 = pd.read_excel('D:\Coding\PythonWorkspace02\webscrapping\stock_scrapping\stock_list02.xls', header=0)

#읽은 엑셀을 리스트로변환
alist = a1.values.tolist()
print("xls to list length : ", len(alist))

# directory = os.path.dirname(os.path.abspath(__file__))
# file_name = "stock_list01.csv"
# dir_file = directory + "\\" + file_name

# 현재 작업 디렉토리를 작업디레토리로 변경
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())

f = open("./stock_list02.csv", "w", encoding="utf-8-sig", newline="") #한글이 깨지지 않게 저장하기 utf-8-sig
writer = csv.writer(f)


i = 0
for line in alist:
    writer.writerow(line)
    i += 1
    # print(i, " : ", line)
        
f.close()


# csv 파일열어 데이터 불러오기
g = open("./stock_list02.csv", "r", encoding="utf-8-sig")
reader = csv.reader(g)
# print(reader)
data = list(reader)
# print(data[0][0])
# print(data)
print("csv length : ", len(data))

j = 0
stock_no_list = []
com_name_list = []
for line in data:
    # for i in line:
    #     print(line[1])

    # for i in line:
        # for i in range(len(alist)):
    stock_no = "{:06d}".format(int(line[1]))
    com_name = "{}".format(line[0])
    # print(data[j])
    j += 1
    # print(j, " : ", stock_no, " : ", com_name)  
    stock_no_list.append(stock_no)   
    com_name_list.append(com_name)  

g.close()

print("stock_no_list = ", stock_no_list)
print("com_name_list = ", com_name_list)



# #리스트에서 한 행씩 읽어서 str변수에 원하는 형태로 삽입
# dictionarytext = "sign = {"
# for i in range(len(alist)):
#     stock_no = "{:06d}".format(alist[i][1])
#     com_name = str(alist[i][0])
#     dictionarytext += "\""+stock_no+"\" : " + com_name+ ","
#     if i%5 == 0 :dictionarytext += "\n"

# dictionarytext += "}"

# #text 파일 만들기
# f= open("D:\Coding\PythonWorkspace02\webscrapping\stock_scrapping\stock_list01.txt","w",-1,encoding="utf-8")
# #만든 str을 text에 넣기
# f.write(dictionarytext)
# #파일 닫기
# f.close()
# # print(dictionarytext)
# f= open("D:\Coding\PythonWorkspace02\webscrapping\stock_scrapping\stock_list01.txt","w",-1,encoding="utf-8")


# with open("D:\Coding\PythonWorkspace02\webscrapping\stock_scrapping\stock_list01.txt","rt", encoding="utf-8") as f:
#     for line in f:
#         data = line.strip()
#         print(data)

# f = open('D:\Coding\PythonWorkspace02\webscrapping\stock_scrapping\stock_list01.csv','rt', encoding='utf-8-sig')
# data = f.read()
# # f.close()
# print(data)

