# week13_C_05.py
# 202444071
# 전태현

import datetime
from datetime import datetime as dt

books = list()
parsingFormat = "%Y-%m-%d %H:%M:%S"

while True:
    bookNumber = input("도서번호: ").strip()
    if not bookNumber:
        break

    while True:
        try:
            inTime = input("대출시간: ").strip()
            if inTime:
                inTime = dt.strptime(inTime, parsingFormat)
                break
        except:
            pass
        
    while True:
        try:
            outTime = input("반납시간: ").strip()
            if not outTime:
                outTime = None
            else:
                outTime = dt.strptime(outTime, parsingFormat)
            break
        except:
            pass

    books.append({'bookNumber':bookNumber, 'in':inTime, 'out':outTime})

for book in books:
    print(book['bookNumber'], book['in'], book['out'])
