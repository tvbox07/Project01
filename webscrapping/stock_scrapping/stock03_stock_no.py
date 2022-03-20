import pandas as pd


# 엑셀에서 상장법인(유가증권, 코스닥)자료를 리스트로 불러오기
a1 = pd.read_excel('D:\Coding\PythonWorkspace02\webscrapping\stock_scrapping\stock_list01.xls')

#읽은 엑셀을 리스트로변환
print(a1.columns)
alist = a1.values.tolist()
# print(alist.header)
# print(alist[0][1], alist[0][0])
# print(len(alist))

file="D:\Coding\PythonWorkspace02\webscrapping\stock_scrapping\stock_list01.txt"

# stock_list01.txt에 쓰기
with open(file, "w", encoding="utf-8") as f:
    for line in alist:
        data = line.strip()
        f.wirte(data)

    f.write(alist)

# stock_list01.txt불러오기
with open(file, "rt", encoding="utf-8") as f:
    for line in f:
        # print(line.strip())

        j = 1
        for i in line:
            # for i in range(len(alist)):
            stock_no = "{:06d}".format(i[1])
            com_name = "{}".format(i[0])
            # print(j, " : ", '{:06d}'.format(i[1]))
            # print(i , " : ", list)
            j += 1
            print(j, " : ", stock_no, " : ", com_name)
