# week13_C_08_2.py
# id:202444071
# name:전태현

from datetime import datetime as dt
import os

dtformat = "%Y-%m-%d %H:%M:%S"


def diff_seconds(intime, outtime):
    if not outtime:
        outtime = dt.now()
    return (outtime - intime).total_seconds()


if __name__ == "__main__":
    mydir = "c:\\car1_24000001"
    # myfile = "list.txt"
    myfullfile = os.path.join(mydir, myfile)

    if not os.path.isdir(mydir):
        os.mkdir(mydir)

    books = {}

    # read 작업해야 할 곳!
    # 파일이 있는지 확인
    # 있으면 파싱, 없으면 그대로 밑으로 떨어지면 됨.

    while True:
        number = input("도서번호:").strip()
        if not number:
            break

        if not number in books.keys():
            books[number] = []
        else:
            for time in books[number]:
                if time['out'] == None:
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

        # book = {"num": number, "in": intime, "out": outtime}
        # books.append(book)
        book = {"in": intime, "out": outtime}
        books[number].append(times)

        bookFullName = os.path.join(mypath, number + ".txt")
        with open(bookFullName, 'a', encoding="utf-8") as f:
            intime = dt.strftime(intime, str_fmt)
            if outtime:
                outtime = dt.strftime(outtime, str_fmt)
                f.write(f"{intime}|{outtime}\n")
            else:
                f.write(f"{intime}|")

    for number, times in books.items():
        print(number)
        for time in times:
            print(time["in"], time["out"])
            print(diff_seconds(time["in"], time["out"]))

    

