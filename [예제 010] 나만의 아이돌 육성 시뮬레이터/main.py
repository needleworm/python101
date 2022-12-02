"""
2022. 12. 01.
Byunghyun Ban
bhban@kakao.com
https://github.com/needleworm/python101
"""
import utils as U

name, age, song, dance, act = U.get_status()
your_idol = U.Idol(name, age, song, dance, act)

for i in range(5):
    activity = U.get_activity()

    if activity == 1: # 음반활동
        print("노래실력이 향상되었습니다!")
        your_idol.song += 1
    elif activity == 2: # 드라마 배우 활동
        print("연기실력이 향상되었습니다!")
        your_idol.act += 1
    elif activity == 3: # 콘서트 활동
        print("댄스 실력이 향상되었습니다!")
        your_idol.dance += 1
    elif activity == 4: # 헬스장 폐관수련
        print("근성장과 혈행개선을 통해 모든 능력치가 1씩 증가합니다.")
        your_idol.upgrade_all_status()

    your_idol.age += 1
    print("\n아이돌 " + your_idol.name + "의 데뷔 후 " + str(i + 1) + "년이 흘렀습니다.\n\n")

if your_idol.sum_status() < 15:
    print("아이돌의 능력치가 부족하여 은퇴합니다.")
else:
    print("아직 활동의 여력이 남아 소속사와 재계약합니다.")
