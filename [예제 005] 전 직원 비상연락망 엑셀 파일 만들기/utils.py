"""
2022. 06. 03.
Byunghyun Ban

bhban@kakao.com
https://github.com/needleworm/python101
"""


import time

try:
    import pyexcel as px
except ModuleNotFoundError:
    import pip
    pip.main(['install', "pyexcel"])
    pip.main(['install', "pyexcel-xlsx"])
    try:
        import pyexcel as px
    except ModuleNotFoundError:
        time.sleep(2)
        import pyexcel as px

import os
import random

alphabet_samples = "abcdefghizklmnopqrstuvwxyz1234567890"


def random_string(length):
    result = ""
    for i in range(length):
        result += random.choice(alphabet_samples)
    return result


first_name_samples = "김이박최정강조윤장임황윤"
middle_name_samples = "민서예지도하주윤채현지"
last_name_samples = "준윤우원호후서연아은진"


def random_name():
    result = ""
    result += random.choice(first_name_samples)
    result += random.choice(middle_name_samples)
    result += random.choice(last_name_samples)
    return result


def generate_xlsx():
    if "직원 정보" not in os.listdir():
        print("> 직원 정보/ 폴더 생성")
        os.mkdir("직원 정보")

    HEADER = ["이름", "나이", "이메일", "부서명", "전화번호", "성별"]

    print("> 엑셀 파일 생성 시작")
    names = []

    itr = 100
    for el in os.listdir("직원 정보"):
        if el.endswith(".xlsx"):
            itr -= 1

    for i in range(itr):
        name = random_name()
        if name not in names:
            names.append(name)
        else:
            while name in names:
                name = random_name()
            names.append(name)

        filename = "직원 정보/" + name + ".xlsx"

        contents = [
            name,
            str(time.time())[-2:],
            random_string(8) + "@bhban.com",
            random.choice(["연구부", "개발부", "인사과", "마케팅팀", "영업부", "경영지원팀", "관리부"]),
            "010-" + str(time.time() / 1000)[-4:] + "-" + str(time.time() / 1000)[-6:-2],
            random.choice(["male", "female"])
        ]

        RESULT = [HEADER, contents]

        px.save_as(array=RESULT, dest_file_name=filename)

    print("> 엑셀 파일 생성 종료")

    ret = []
    for el in os.listdir("직원 정보"):
        if el.endswith(".xlsx"):
            ret.append("직원 정보/" + el)

    return ret


def process(file_list):
    print("> " + str(len(file_list)) + " 명의 직원 정보를 병합합니다.")
    contents = []

    for file in file_list:
        if ".xlsx" not in file:
            continue
        data_array = px.get_array(file_name=file)

        header = data_array[0]
        data_array = data_array[1:]

        if not contents:
            contents.append(header)

        contents += data_array

    px.save_as(array=contents, dest_file_name="전 직원 비상연락망.xlsx")

    print("> 전 직원 비상연락망 작성이 완료되었습니다.")
