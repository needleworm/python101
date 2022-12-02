"""
2022. 12. 01.
Byunghyun Ban
bhban@kakao.com
https://github.com/needleworm/python101
"""


class Idol:
    def __init__(self, name, age, song, dance, act):
        self.name = name
        self.age = age
        self.song = song
        self.dance = dance
        self.act = act

    def upgrade_all_status(self):
        self.song += 1
        self.dance += 1
        self.act += 1

    def sum_status(self):
        return self.song + self.dance + self.act


"""이 위에 코딩하세요"""


def get_status():
    print("나만의 아이돌 키우기를 시작합니다!")
    print("여러분의 아이돌을 만들어 주세요!")
    name = input("이름: ")

    while True:
        age = input("나이: ")
        if not age.isdigit():
            print("숫자만 입력 가능합니다.")
            continue
        age = int(age)
        break

    while True:
        song = input("노래 능력치 (0 ~ 5): ")
        if not song.isdigit():
            print("숫자만 입력 가능합니다.")
            continue
        song = int(song)
        if song < 0 or song > 5:
            print("0부터 5사이의 값만 입력 가능합니다.")
            continue
        break

    while True:
        dance = input("댄스 능력치 (0 ~ 5): ")
        if not dance.isdigit():
            print("숫자만 입력 가능합니다.")
            continue
        dance = int(dance)
        if dance < 0 or dance > 5:
            print("0부터 5사이의 값만 입력 가능합니다.")
            continue
        break

    while True:
        act = input("연기 능력치 (0 ~ 5): ")
        if not act.isdigit():
            print("숫자만 입력 가능합니다.")
            continue
        act = int(act)
        if act < 0 or act > 5:
            print("0부터 5사이의 값만 입력 가능합니다.")
            continue
        break

    return name, age, song, dance, act


def get_activity():
    while True:
        activity = int(input("활동을 골라주세요!\n\t1. 음반 작업\n\t2. 드라마 출연\n\t3. 댄스 콘서트\n\t4. 헬스장 폐관수련"))
        if activity not in (1, 2, 3, 4):
            print("잘못된 입력입니다.")
            continue
        return activity
