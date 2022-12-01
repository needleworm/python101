"""
2022. 12. 01.
Byunghyun Ban
bhban@kakao.com
https://github.com/needleworm/python101
"""
import utils as U

print("성격유형검사를 시작합니다")
E, I = U.E_or_I()
N, S = U.N_or_S()
T, F = U.T_or_F()
P, J = U.P_or_J()
print("성격유형검사가 끝났습니다!")

"""이 아래에 성격유형검사 결과를 출력하는 코드를 작성하시오"""
result = ["E", "N", "T", "P"]
if I > E:
    result[0] = "I"

if S > N:
    result[1] = "S"

if T > F:
    result[2] = "T"

if P > J:
    result[3] = "J"

print("당신의 성격유형은 " + "".join(result) + " 입니다!")
