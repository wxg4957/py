# week12_10.py

def test():
    raise NotImplementedError("test함수 미작성")

while True:
    try:
        dvd = int(input("피제수: "))
        dvs = int(input("제수: "))
        result = dvd / dvs
        print(result)
        test()
    except ValueError:
        print("정수로 입력")
    except ZeroDivisionError:
        print("제수에 0 이외의 수 입력")
    except Exception as e:
        print(e)
    else:
        print("try문이 완벽히 실행되면 실행")
    finally:
        print("반드시 실행됨")
    # except Exception:
    #     print("!")
    # except:
    #     print("!")
