"""
2022. 05. 10. 
Byunghyun Ban

bhban@kakao.com
https://github.com/needleworm/python101
"""

import random


class Sphinx:
    def __init__(self):
        self.quiz_dict = {
            "int" : [1, 3, 12, 42, -34, 0],
            "float" : [1.0, 0.0, 4.2, -3.5, 231.0],
            "bool" : [True, False],
            "str" : ["'A'", "'apple'", "'I want some milks'", "'I am Ironman'"],
            "list" : [[1, 2, 3], ["A", "B", "C"], [(1, 2, 3), (4, 5, 6)]],
            "tuple" : [(1, 2, 3), ("A", "B", "C"), ([1, 2, 3], [4, 5, 6])],
            "dict" : [{}, {"A": 3}, {"A": 3, "B": 4}],
            "set" : [{1, 2, 3}, {4, 5, 6, 7}],
            "nonetype" : [None]
        }

        print("*** 데이터 타입 스핑크스를 무찔러라! ***\n\n")
        print("[주의] 데이터타입 스핑크스가 나타났습니다!")
        print("[스핑크스] 내가 내는 문제를 맞추지 못하면 살려주지 않겠다!\n\n")

    def quiz(self):
        count = 0
        for i in range(10):
            count += int(self.single_quiz())
        
        print("[스핑크스] 총 10문제 중에서 " + str(count) + " 문제를 맞췄군!")
        if count < 7:
            print("[스핑크스] 더 강해져서 돌아와라, 인간! 크하하하!\n\n")
            print("*** 데이터 타입 스핑크스에게 패배했습니다. ***")
        else:
            print("[스핑크스] 크윽, 분하다. 너무 똑똑한 인간이야!\n\n")
            print("*** 데이터 타입 스핑크스를 무찔렀습니다! ***")

    def single_quiz(self):
        answer = random.choice(list(self.quiz_dict.keys()))
        question = random.choice(self.quiz_dict[answer])

        print("[문제] 다음 데이터의 타입은 무엇인가?")
        print("    > " + str(question))
        response = input("[답을 입력하시오] : ")

        if response.lower() == answer:
            print("[스핑크스] 정답이다! 대단하군!\n\n")
            return True
        else:
            print("[스핑크스] 오답이다, 인간! 답은 " + answer + " 이다!\n\n")
            return False
