"""
2022. 12. 01.
Byunghyun Ban
bhban@kakao.com
https://github.com/needleworm/python101
"""
import utils as U

val = ""
while True:
    val = input("모드를 선택하세요.\n\t1. 한국어 -> 영어\n\t2. 영어 -> 한국어\n")
    if val in ['1', '2']:
        break

    print("\n입력값이 잘못되었습니다. (1 또는 2 입력)")

if val == '1':
    while True:
        text = input("\n한국어를 입력해주세요 (q to quit): \n")
        if text == "q":
            break
        print(U.kr_to_en(text))
else:
    while True:
        text = input("\n영어를 입력해주세요 (q to quit): \n")
        if text == "q":
            break
        print(U.en_to_kr(text))
