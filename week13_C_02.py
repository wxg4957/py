# week13_C_02.py
# 202444071
# 전태현

while True:
    bookNumber = input("도서번호: ").strip()
    if not bookNumber:
        break
    inTime = input("대출시간: ")
    outTime = input("반납시간: ")
