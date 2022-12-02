"""
2022. 12. 01.
Byunghyun Ban
bhban@kakao.com
https://github.com/needleworm/python101
"""

def E_or_I():
    E = 0
    I = 0

    q = ""
    while True:
        q = input("새로운 친구를 사귀는 것이 즐겁다 (y / n)")
        if q in ["y", "n"]:
            break
        print("올바르지 않은 응답입니다.")

    if q == 'y':
        E += 1
    else:
        I += 1

    q = ""
    while True:
        q = input("SNS에 내 취향의 사진보다 좋아요가 많이 눌릴 것 같은 사진을 올리는 편이다 (y / n)")
        if q in ["y", "n"]:
            break
        print("올바르지 않은 응답입니다.")

    if q == 'y':
        E += 1
    else:
        I += 1

    q = ""
    while True:
        q = input("여행지에서 처음 만난 사람과 같이 식사할 수 있다 (y / n)")
        if q in ["y", "n"]:
            break
        print("올바르지 않은 응답입니다.")

    if q == 'y':
        E += 1
    else:
        I += 1

    return E, I


def N_or_S():
    N = 0
    S = 0

    q = ""
    while True:
        q = input("현재의 행복이 미래의 행복보다 중요하다 (y / n)")
        if q in ["y", "n"]:
            break
        print("올바르지 않은 응답입니다.")

    if q == 'y':
        S += 1
    else:
        N += 1

    q = ""
    while True:
        q = input("효용성이 검증된 아이디어가 새로운 아이디어보다 좋다 (y / n)")
        if q in ["y", "n"]:
            break
        print("올바르지 않은 응답입니다.")

    if q == 'y':
        S += 1
    else:
        N += 1

    q = ""
    while True:
        q = input("현실의 일을 고민하기 보다 어젯밤 꾼 꿈이 무엇이었나 떠올리려 노력하는 편이 좋다 (y / n)")
        if q in ["y", "n"]:
            break
        print("올바르지 않은 응답입니다.")

    if q == 'y':
        S += 1
    else:
        N += 1

    return N, S


def T_or_F():
    T = 0
    F = 0

    q = ""
    while True:
        q = input("직장 동료가 회의 중에 울면 짜증보다는 걱정이 든다 (y / n)")
        if q in ["y", "n"]:
            break
        print("올바르지 않은 응답입니다.")

    if q == 'y':
        F += 1
    else:
        T += 1

    q = ""
    while True:
        q = input("논리적 대화에 감정을 개입시키는 것이 싫다 (y / n)")
        if q in ["y", "n"]:
            break
        print("올바르지 않은 응답입니다.")

    if q == 'y':
        T += 1
    else:
        F += 1

    q = ""
    while True:
        q = input("[좋다 / 싫다]보다는 [옳다 / 그르다]가 판단의 기준이 된다 (y / n)")
        if q in ["y", "n"]:
            break
        print("올바르지 않은 응답입니다.")

    if q == 'y':
        T += 1
    else:
        F += 1

    return T, F


def P_or_J():
    P = 0
    J = 0

    q = ""
    while True:
        q = input("패키지여행보다 자유여행이 더 좋다 (y / n)")
        if q in ["y", "n"]:
            break
        print("올바르지 않은 응답입니다.")

    if q == 'y':
        P += 1
    else:
        J += 1

    q = ""
    while True:
        q = input("만일의 사태를 대비해 여러가지 계획을 꼼꼼하게 세운다 (y / n)")
        if q in ["y", "n"]:
            break
        print("올바르지 않은 응답입니다.")

    if q == 'y':
        J += 1
    else:
        P += 1

    q = ""
    while True:
        q = input("계획을 짜면 잘 지키는 편이다 (y / n)")
        if q in ["y", "n"]:
            break
        print("올바르지 않은 응답입니다.")

    if q == 'y':
        J += 1
    else:
        P += 1

    return P, J
