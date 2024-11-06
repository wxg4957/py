# week11_02.py

import datetime

class Test:
    def __init__(self): # 매개변수
        name = "a"      # local
        self.name = "b" # attr
        self.age = 20   # attr
        print(datetime.datetime.now())

t = Test()
print(t.name)
# 1. Test() 생성자 호출
# 2. __new__() 메소드 자동 호출
#    Test의 인스턴스를 생성
# 3. __init__() 메소드 자동 호출
#    Test의 인스턴스를 초기화
# 4. 생성한 인스턴스의 참조를 반환

t2 = Test()
print(t.name)

t.name = "김인하"
t2.name = "이인하"

print(id(t), id(t2)) # 메모리 주소
print(type(t) == type(t2)) # true
print(t == t2) # false
print(t.name == t2.name) # false
print(t.age == t2.age) #true
