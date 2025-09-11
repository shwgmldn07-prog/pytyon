# 파스칼표기법 = 맨 앞글자만 대문자(java의 class 생성 시 활용)
# 카멜표기법 = 단어의 의미가 있는 첫글자를 대문자로 한다(shopList)
# 스네이크표기법 = 단어간의 구분을 _로 한다(shop_list)


# 리스트 생성 방법 1 - 비어있는 리스트로 생성
a = []

# 리스트 생성 방법 2 - 값이 있는 리스트로 생성
shop_list = ['apple','banana','carrot','mango']
print(f'shop_list : {shop_list}')

# 리스트에 값을 넣는 방법
# 가장 뒤로부터 넣는 방법
a.append(1)
a.append(2)
a.append(3)
# 특정한 번호를 지정해서 넣는 방법
a.insert(1,'X')

print(f'a의 길이:{len(a)}')
print(f'a:{a}')

# a의 2번방에 있는 값
print(f'a[2]={a[2]}')
# a의 가장 마지막 방에 있는 값
print(f'a의 마지막 방의 값 = {a[3]}')

# 길이에서 1을 뺀 값을 이용-> 인덱스는 0번부터 시작한다는 점을 이용)
print(f'a의 마지막 방의 값 = {a[len(a)-1]}')
# 파이썬에서 사용되는 방식, 0보다 뒤로가면 맨 뒤로 이동한다는 개념
print(f'a의 마지막 방의 값 = {a[-1]}')













