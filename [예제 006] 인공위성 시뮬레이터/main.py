"""
2022. 12. 01.
Byunghyun Ban
bhban@kakao.com
https://github.com/needleworm/python101
"""
import utils as U

pi = 3.141592 # 원주율
g = 9.8 # 중력가속도
R = U.get_R() # 공전궤도 반지름

# 지표면으로부터 인공위성의 높이를 출력하는 코드를 작성하시오
print("인공위성의 고도는 " + str(R - 6400) + "km 입니다.")

# 인공위성이 지구를 한 바퀴 도는 데 몇 초가 걸리는지 화면에 출력하시오.
S = 2 * pi * (R / g) ** 0.5
print("인공위성이 지구를 한 바퀴도는 데에는 " + str(S) + " 초가 소요됩니다.")

# 인공위성이 하루에 지구를 몇 바퀴 돌 수 있는 지 화면에 출력하시오.
print("인공위성은 하루에 지구를 " + str(int(24*60*60 / S)) + " 바퀴 회전합니다.")
