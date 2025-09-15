from sys import set_int_max_str_digits

import oper

# dir() 내장함수를 사용하면 모듈에 정의되어 있는 변수,함수 목록을 볼 수 있다
print(dir(oper))

# 모듈의 이름 확인
print(oper.__name__) # 특정 모듈의 이름을 확인
print(__name__) # 현재 나의 이름-> 현재 실행되는 함수

#요약
#1. 모듈은 여러 파일에서 가져다 쓸 수 있는 공통의 기능
#2. frm, import, as 등의 쓰임새에 대해서 익숙해지자

#run,jump,walk,swim
#plus,minus,multiple,devide 수학적 함수
#acceleration,break,drift 드라이브

