# week11_07.py

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        # 기본: 타입 + 인스턴스 주소를 문자열로 반환
        # 재정의 할 때의 조건, 무조건 문자열로 반환
        return f"x:{self.x} y:{self.y}"

p = Point()
p = Point(1,2)
p = Point(x=1)
p = Point(y=1)
print(p.x, p.y)
print(p)

class Rectangle:
    def __init__(self, x=0.0, y=0.0, w=0.0, h=0.0):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    # 사각형의 둘레를 구해서 반환하는 메소드
    def getRoundLength(self):
        return (self.width * 2) + (self.height * 2)

r = Rectangle(1, 1, 10, 5)
print(r.getRoundLength())

class Subject:
    def __init__(self, num, nm, tc=None):
        self.number = num
        self.name = nm
        self.teacher = tc
        self.grade = None

# Subject()
Subject("071", "파이선")
Subject("071", "파이선", "이인하")
# Subject("071", "파이선", "이인하", 4.0)

class Student:
    def __init__(self, nm, num, d, by):
        self.name = nm
        self.number = num
        self.dept = d
        self.birthyear = by

class Rectangle2:
    def __init__(self, sp=Point(), w=0.0, h=0.0):
        self.spoint = sp
        self_width = w
        self.height = h

class Rectangle3:
    def __init__(self, sp=Point(), ep=Point()):
        self.spoint = sp
        self.epoint = ep

r = Rectangle3()
r.spoint.x = 1
r.epoint.y = 1

r.epoint.x = 10
r.epoint.y = 21
