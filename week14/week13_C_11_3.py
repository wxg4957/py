# week13_C_11_3.py
# id:202444071
# name:전태현

from week13_C_book import Book2 as Book
from week13_C_book import TimeStamp
from datetime import datetime as dt
import os

dtformat = "%Y-%m-%d %H:%M:%S"

if __name__ == "__main__":
    myPath = "c:\\book1_2444071"
    # myfile = "list.txt"
    # myfullfile = os.path.join(mydir)

    if not os.path.isdir(myPath):
        os.mkdir(myPath)

    books = []

    members = os.listdir(myPath)
    for member in members:
        memberFullName = os.path.join(myPath, member)
        if os.path.isfile(memberFullName):
            # 111.txt => 111 => 111, .txt
            fileExt = os.path.splitext(member)
            if fileExt and len(fileExt) == 2 and fileExt[-1] == ".txt":
                number = fileExt[0].strip()
                book = Book(number)
                with open(memberFullName, 'r', encoding="utf-8") as f:
                    for line in f:
                        splitDatas = line.strip().split('|')
                        if splitDatas and len(splitDatas) == 2:
                            intime = dt.strptime(splitDatas[0], dtformat)
                            if splitDatas[1].strip():
                                outtime = dt.strptime(splitDatas[1].strip(), dtformat)
                            else:
                                outtime = None

                            book.addTimeStamp(intime, outtime)
                if book.history:
                    books.append(book)

    # read 작업해야 할 곳!
    # 파일이 있는지 확인
    # 있으면 파싱, 없으면 그대로 밑으로 떨어지면 됨.

    while True:
        number = input("도서번호:").strip()
        if not number:
            break

        searchBook = [book for book in books if book.number == number]

        if not searchBook:
            book = Book(number)
            books.append(book)
        else:
            book = searchBook[0]
            for timeStamp in book.history:
                if timeStamp.isRent():
                    print("반납되지 않음")
                    continue

        while True:
            try:
                intime = input("대출시간:").strip()
                if intime:
                    intime = dt.strptime(intime, dtformat)
                    break
            except:
                pass

        while True:
            try:
                outtime = input("반납시간:").strip()
                if not outtime:
                    outtime = None
                    break
                outtime = dt.strptime(outtime, dtformat)
                break
            except:
                pass

        # book = {"in": intime, "out": outtime}
        # books[number].append(book)
        book.addTimeStamp(intime, outtime)

        bookFullName = os.path.join(myPath, number + ".txt")
        with open(bookFullName, 'a', encoding="utf-8") as f:
            intime = dt.strftime(intime, dtformat)
            if outtime:
                outtime = dt.strftime(outtime, dtformat)
                f.write(f"{intime}|{outtime}\n")
            else:
                f.write(f"{intime}|")

    for book in books:
        print(book.number)
        
        for timeStamp in book.history:
            print(timeStamp.rentTime, timeStamp.rentTime)
            print(timeStamp.diffSeconds())
