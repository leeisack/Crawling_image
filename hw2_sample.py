# import cv2
# import os

# # ## TODO1: 아래 두 변수명을 사용 환경에 맞게 수정
# # root_path = None /Users/isacklee/Documents/ROOT
# # result_file = None /Users/isacklee/Documents/RESULT

# # def make_abspath_list(_root_path_, _result_file_):
# #     img_list = []
# #     ## TODO2: 입력받은 경로 내 모든 파일 중 이미지인 파일의 절대경로를 img_list에 추가
# #     ## TODO3: result_file에 img_list작성하여 저장
# #     return len(img_list)

# # print(make_abspath_list(root_path, result_file))


import re

def solution(new_id):
    # print(new_id)
    #소문자로 바꾸기
    Id_lower = new_id.lower()
    print(Id_lower)
    
    #-_.특수문자지우기
    Id_sub = re.sub(r"[^a-z0-9-_.$]",'',Id_lower)
    print(Id_sub)

    #.. 2개이상 . 
    Id_double_sub = re.sub(r"\.\.+",'.',Id_sub)
    print(Id_double_sub)
    
    Id_start_end = re.sub(r"^[\.]",'',Id_double_sub)
    print("시작 . 제거")
    print(Id_start_end)

    try:
        if Id_start_end[-1] == '.':
            Id_start_end2 = Id_start_end[:-1]
            print("마지막 . 제거")
            print(Id_start_end2)
        else:
            Id_start_end2 = Id_start_end
            print("마지막 . 제거")
            print(Id_start_end2)
    except IndexError:
        Id_start_end2 = Id_start_end
        print("마지막 . 제거")
        print(Id_start_end2)

    if len(Id_start_end2) == 0:
        Id_double_sub3= 'a'
        print('add a')
        print (Id_double_sub3)
    else:
        Id_double_sub3 = Id_start_end2
        # print(len(Id_double_sub3))
        print(Id_double_sub3)



    if len(Id_double_sub3) >= 16:
        reformed = Id_double_sub3[0:15]
        if reformed[-1] =='.':
            reformed = reformed[0:-1]
        print(reformed)
    else:
        reformed = Id_double_sub3
        print(reformed)

    
    
    if len(reformed) == 2:
        Id_2_under = reformed + reformed[-1]
        print(Id_2_under)
    elif len(reformed) == 1: 
        Id_1_under = reformed + reformed[-1] + reformed[-1]
        print(Id_1_under)
    else:
        # print(reformed)
        print(reformed)
    print("done")


solution("abcdefghijklmn.p")
solution("abcdefghijklmn.p")
solution("abcdefghijklmn.p")
solution("abcdefghijklmn.p")
solution("abcdefghijklmn.p")



import re

def solution(new_id):
    answer = ''
    # 1단계 & 2단계 : 소문자 치환
    answer = re.sub('[^a-z\d\-\_\.]', '', new_id.lower())
    # 3단계 : 마침표 2번 이상 > 하나로
    answer = re.sub('\.\.+', '.', answer)
    # 4단계 : 양 끝 마침표 제거
    answer = re.sub('^\.|\.$', '', answer)
    # 5단계 : 빈 문자열이면 a 대입
    if answer == '':
        answer = 'a'
    # 6단계 : 길이가 16자 이상이면 1~15자만 남기기 & 맨 끝 마침표 제거
    answer = re.sub('\.$', '', answer[0:15])
    # 7단계 : 길이가 3이 될 때까지 반복해서 끝에 붙이기
    while len(answer) < 3:
        answer += answer[-1:]
    return answer

