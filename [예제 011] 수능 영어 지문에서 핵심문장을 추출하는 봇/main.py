"""
2022. 12. 01.
Byunghyun Ban
bhban@kakao.com
https://github.com/needleworm/python101
"""
import utils as U
import os

# 2023수능 31번지문
sample_text = "There is something deeply paradoxical about the professional status of sports journalism, especially in the " \
    "medium of print. In  discharging  their  usual  responsibilities  of  description  and commentary,  " \
    "reporters’  accounts  of  sports  events  are  eagerly consulted  by  sports  fans,  while  in  their  " \
    "broader  journalistic role of covering sport in its many forms, sports journalists are among  the  most  " \
    "visible  of  all  contemporary  writers.  The ruminations  of  the  elite  class  of  ‘celebrity’  sports  " \
    "journalists are much sought after by the major newspapers, their lucrative contracts being the envy of " \
    "colleagues in other ‘disciplines’ of journalism.  Yet  sports  journalists  do  not  have  a  standing  in " \
    "their profession that corresponds to the size of their readerships or of their pay packets, with the old " \
    "saying (now reaching the status of cliché) that sport is the ‘toy department of the news media’ still " \
    "readily to hand as a dismissal of the worth of what sports journalists do. This reluctance to take sports " \
    "journalism seriously  produces  the  paradoxical  outcome  that  sports newspaper writers are much read but " \
    "little."

print(U.extract(sample_text))

""" 이 아래에 코딩하세요 """
txt_files = os.listdir("sources")
for filename in txt_files:
    if not filename.endswith(".txt"):
        continue

    file = open("sources/" + filename)
    contents = file.read()
    file.close()
    file = open("sources/" + filename, "a")

    contents = contents.replace("\n", "")
    key_sentence = U.extract(contents)

    file.write("\n\n[핵심 문장 분석 결과]\n")
    file.write(key_sentence)
    file.close()
