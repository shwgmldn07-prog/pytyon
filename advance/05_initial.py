class Puppy:

    name="" # 멤버 변수(필드): class안에서 사용가능한 변수
    goal=""

    def __init__(self,name,goal): # 생성자:객체화시 호출되는 함수
        # 받아온 name과 goal은 생성자로 벗어날 수 없다(생성자의 쓰임이 다하면 함께 없어진다)
        # 그래서 클래스(객체) 맴버에다가 넣어줘야, 객체가 살아있는 동안 사용이 가능하다
        # 그런데 name=name형태로는 어떤것이 객체의 멤버인지 알 수 없다
        # 그래서 멤버인 녀석은 self를 이용하여 표시해준다
     self.name=name
     self.goal=goal

puppy = Puppy("멍멍이","집지키기")
print(f'이름:{puppy.name}/목적:{puppy.goal}')

