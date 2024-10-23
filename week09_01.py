# week09_01.py

data01 = [1,2,3,4]

summary = sum(data01)
maximum = max(data01)
minimum = min(data01)
average = sum(data01) / len(data01)

print(summary)
print(maximum)
print(minimum)
print(average)


print("-" * 30)
for i in data01:
    print(f"{i}")


print("-" * 30)
for i in range(len(data01)):
    print(f"{i}")


print("-" * 30)
for i in range(len(data01)):
    print(f"data01[{i}]:{data01[i]}")


print("-" * 30)
for i in enumerate(data01):
    print(f"data01[{i[0]}]:{i[1]}")


print("-" * 30)
for i, v in enumerate(data01):
    print(f"data01[{i}]:{v}")


data02 = [
    [1,2,3,4],
    [10,20],
    [11,12,13,14]
    ]


print("-" * 30)
for i in data02:
    print(i)


print("-" * 30)
v = 1
for i in data02:
    print(f"{v}번째:{i}")
    summary = sum(i)
    maximum = max(i)
    minimum = min(i)
    average = sum(i) / len(i)
    
    print(f"sum {summary}")
    print(f"max {maximum}")
    print(f"min {minimum}")
    print(f"avg {average}")
    v += 1
    

print("-" * 30)
v = 1
for i in data02:
    print(f"{v}번째:", end="")
    
    for i2, v2 in enumerate(i):
        print(f"[{i2}]{v2} ", end="")
    print()
    
    summary = sum(i)
    maximum = max(i)
    minimum = min(i)
    average = sum(i) / len(i)
    
    print(f"sum {summary}")
    print(f"max {maximum}")
    print(f"min {minimum}")
    print(f"avg {average}")
    v += 1
    

data03 = {
    "김인하":[1,2],
    "이인하":[10,20,30,40,50,60,70],
    "송인하":[11,12,13,14,]
    }


print("-" * 30)
for k in data03:
    print(k)


print("-" * 30)
for k in data03:
    print(data03[k])


print("-" * 30)
for k in data03:
    print(f"{k}:{data03[k]}")

    
print("-" * 30)
for k in data03:
    print(f"{k}",end="")
    for i in range(len(data03[k])):
        print(f"[{i+1}]{data03[k][i]} ",end="")
    print()
    
    summary = sum(data03[k])
    maximum = max(data03[k])
    minimum = min(data03[k])
    average = sum(data03[k]) / len(data03[k])
    
    print(f"sum {summary}")
    print(f"max {maximum}")
    print(f"min {minimum}")
    print(f"avg {average}")
        





