# week09_02.py


data02 = [
    [1,2,3,4],
    [10,20],
    [11,12,13,14]
    ]

data03 = {
    "김인하":[1,2],
    "이인하":[10,20,30,40,50,60,70],
    "송인하":[11,12,13,14,]
    }

def print_info(datas):
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

def analyze_list(datas):
    v = 1
    for i in datas:
        print(f"{v}번째:", end="")
        print_info(datas)

def analyze_dict(datas):
    v = 1
    for k in datas:
        print(f"{k}:",end="")
        print_info(datas)

def analyze_score(datas):
    if isinstance(datas, list):
        analyze_list(datas)
    elif isinstance(datas, dict):
        analyze_dict(datas)
    else:
        print("분석 불가")

analyze_list(data02)
analyze_dict(data03)
analyze_score(data03)
