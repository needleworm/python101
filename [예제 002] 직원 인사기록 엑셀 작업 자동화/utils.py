"""
2022. 05. 09. 
Byunghyun Ban

bhban@kakao.com
https://github.com/needleworm/python101
"""


try:
    import pyexcel as px
except:
    import pip
    pip.main(['install', "pyexcel"])
    pip.main(['install', "pyexcel-xlsx"])
    import pyexcel as px

import os

def process(name, division, phone, age, filename="예제 002.xlsx"):
    print("엑셀 파일 작업을 시작합니다.")
    print("> 이름 : " + name)
    print("> 부서 : " + division)
    print("> 연락처 : " + phone)
    print("> 나이 : " + age)

    if filename in os.listdir():
        contents = px.load(file_name=filename).array
        contents.append([name, division, phone, age])
    else:
        contents = [["이름", "부서", "연락처", "연령"], [name, division, phone, age]]
    px.save_as(array=contents, dest_file_name=filename)

    print(filename + " 파일에 내용물이 저장되었습니다.")
    print("엑셀 파일 작업을 종료합니다.")
