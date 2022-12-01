import utils as U
file_list = U.generate_xlsx()

""" 이 아래에 코딩하세요! """
# [Task 1] file_list의 내용물을 정렬하세요.
#     (Hint 1) sort()를 사용합니다.
file_list.sort()

# [Task 2] file_list의 맨 뒤 원소 30개를 삭제하세요.
#     (Hint 2) del()을 사용합니다.
del(file_list[-30:])

# [Task 3] file_list의 맨 앞 원소 10개를 화면에 출력하세요.
#     (Hint 3) print()를 사용합니다.
print(file_list[:10])

""" 코딩 종료! """
U.process(file_list)
