"""
2022. 12. 01.
Byunghyun Ban
bhban@kakao.com
https://github.com/needleworm/python101
"""


def get_R():
    while True:
        R = input("인공위성의 공전 궤도 반지름을 입력하세요 (7400 km ~ 100000Km) :")
        if not R.isdigit():
            print("숫자만 입력 가능합니다.")
            continue
        R = int(R)
        if R < 7400 or R > 100000:
            print("7400 ~ 100000 사이의 값만 입력 가능합니다.")
            continue
        return R
