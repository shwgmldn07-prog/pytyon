# 사전은 키:값 형태로 되어있다
# 비슷한 자료구조로는 자바스크립트에는 오브젝트, 자바의 맵이 있다
dic = {
    'name':'lee,heewoo',
    'phone':'010-1234-1234',
    'age':26
}

dic2 = {
    'name': 'hong,gil-dong',
    'phone': '010-2222-2222',
    'friends': ['Alice','John','Smith']
}

# 사전에 데이터 넣기 1
a = {'first':'a'}
print(a)

# 사전에 데이터 넣기 2
a['second'] = 'b'
print(a)

# 사전에서 특정 요소 삭제
del a['second']
print(a)

# 사전의 특정 요소를 꺼내보자(사용법은 List와 비슷하다)
print(dic2['name'])
print(dic2['friends'])
# get 메서드를 활용해서도 가져올 수 있다
print(dic2.get('phone'))
# 특정 키가 없는 경우 None이 아닌 대체 내용으로 반환할 수 있음
print(dic2.get('nick','해당내용이 없음'))


