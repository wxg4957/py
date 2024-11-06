# week11_05.py

# __init__ 설명
class Test:
    def __init__(self):
        self.name = None
        self.age = None
        # init이 있으면 t.func("", 1)로 지정할 필요X
        
    def func(self, name, age):
        self.name = name
        print(age)

t = Test()
print(t.name)
print(t.age)

t = Test()
t.func("김인하", 20)
print(t.name)
print(t.age)

print("="*20)

# self 설명
class In:
    def func(self):
        print("In.func()")

class Out:
    def method(self):
        print("Out.method()")

# method()
# func()

# Out.method()
# In.func()

i = In()
o = Out()

# 정식표현
Out.method(o)
In.func(i)
str.upper("a")

# 약식표현
o.method()
i.func()
"a".upper()

# 정상 작동하지 않을 가능성이 있는 코드
In.func(o)
Out.method(i)

# 실행X
# o.func()
# i.method()
