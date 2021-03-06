names = ["아이언맨", "토르코딩","헐크","아이유"]
for name in names:
    with open("{}.txt".format(name), "w", encoding="utf-8") as email_file:
        contents = (
            f"안녕하세요? {name}님.\n\n"

            "(주)시스템 관리자 코난입니다.\n"
            "현재 저희회사는 기획중인 관계로\n"
            f"{name}님의 유튜브를 보고 연락드립게 되었습니다.\n"
            "자세한 사항은 첨부드립니다. \n"
            "제안서에 긍정적인 회신 기다리겠습니다.\n"
            "감사합니다. \n\n"
            " - 코난 드림.\n")       
        email_file.write(contents)


        # email_file.write("""
        #     안녕하세요? {name}님.

        #     (주)시스템 관리자 코난입니다.
        #     현재 저희회사는 기획중인 관계로
        #     {name}님의 유튜브를 보고 연락드립게 되었습니다.
        #     자세한 사항은 첨부드립니다. 
        #     제안서에 긍정적인 회신 기다리겠습니다.
        #     """)

# email_file.write("""
# 안녕하세요? {name}님.

# (주)시스템 관리자 코난입니다.
# 현재 저희회사는 기획중인 관계로
# {name}님의 유튜브를 보고 연락드립게 되었습니다.
# 자세한 사항은 첨부드립니다. 
# 제안서에 긍정적인 회신 기다리겠습니다.
# """)