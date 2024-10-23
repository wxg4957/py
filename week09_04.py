# week09_04.py

s1 = {1,2,3,3,4}
s2 = {'a','b','1',1,'1'}

print(s1)
print(s2)

print(s1 & s2)
print(s1 | s2)
print(s1 - s2)

s1.add('6')
print(s1)
s1.update([1,2,3,7])
print(s1)
s1.remove(3)
print(s1)
