# week11_04.py

class Student:
    def __init__(self):
        self.name = ""
        self.number = ""
        self.dept = ""
        self.birthyear = 0

students = []
for i in range(3):
    s1 = Student()
    s1.name = input("이름:")
    s1.number = input("학번:")
    s1.dept = input("학과:")
    s1.birthyear = int(input("생년:"))
    students.append(s1)

for i in students:
    print(i.name)

'''
s2 = Student()
s2.name = input("이름:")
s2.number = input("학번:")
s2.dept = input("학과:")
s2.birthyear = int(input("생년:"))

s3 = Student()
s3.name = input("이름:")
s3.number = input("학번:")
s3.dept = input("학과:")
s3.birthyear = int(input("생년:"))

print(s1.name, s1.number, s1.dept, s1.birthyear)
print(s2.name, s2.number, s2.dept, s2.birthyear)
print(s3.name, s3.number, s3.dept, s3.birthyear)
'''
