# week12_01.py

class Subject:
    def setGrade(self, grade):
        if grade != None and (grade < 0 or grade > 4.5):
            grade = None
        self.grade = grade
        
    def __init__(self, number, name, teacher=None, grade=None):
        self.number = number
        self.name = name
        self.teacher = teacher
        self.setGrade(grade)

    def __str__(self):
        return f"[{self.number}] {self.name}"

sub = Subject("CS0001", "컴퓨터개론", grade=100.9)
print(sub.grade)

sub = Subject("CS0001", "컴퓨터개론", grade=100.9)
sub.setGrade = 100.9
print(sub.grade)

sub = Subject("CS0001", "컴퓨터개론")
print(sub.grade)

class Student:
    def totalGrade(self):
        if self.subjects:
            grades = [sub.grade for sub in self.subjects if sub.grade != None]
            if grades:
                return sum(grades) / len(grades)
        else:
            return None
    
    def __init__(self, number, name, dept, birthyear, *subjects):
        self.number = number
        self.name = name
        self.dept = dept
        self.birthyear = birthyear
        if subjects:
            self.subjects = list(subjects)
        else:
            self.subjects = list()

    def __str__(self):
        return f"[{self.number}] {self.name}"

stu = Student("1", "전태현", "컴퓨터", 2024)
print(stu)
print(stu.totalGrade())

stu = Student("2", "김", "컴퓨터", 2024
              , Subject("001", "파이썬", "김인하")
              , Subject("002", "자바스크립트", "전혜경")
              )
print(stu)
print(stu.totalGrade())

stu = Student("3", "이", "컴퓨터", 2024
              , Subject("001", "파이썬", "김인하")
              , Subject("002", "자바스크립트", "전혜경", grade=3.5)
              , Subject("003", "오픈소스", "김태간", grade=4.5)
              )
print(stu)
print(stu.totalGrade())
