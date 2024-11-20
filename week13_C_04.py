# week13_C_04.py
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
    inTime = input("대출시간: ")
    inTime = dt.strptime(inTime, parsingFormat)
    outTime = input("반납시간: ")
    outTime = dt.strptime(outTime, parsingFormat)

    books.append({'bookNumber':bookNumber, 'in':inTime, 'out':outTime})

for book in books:
    print(book['bookNumber'], book['in'], book['out'])
