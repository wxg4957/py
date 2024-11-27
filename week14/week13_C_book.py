# week13_C_book.py

from datetime import datetime as dt

class Book1:
    pass

class TimeStamp:
    def __init__(self, rentTime, returnTime):
        self.rentTime = rentTime
        self.returnTime = returnTime

    def diffSeconds(self):
        if self.returnTime:
            diff = self.returnTime - self.rentTime
        else:
            diff = dt.now() - self.rentTime

        return diff.total_seconds()

    def isRent(self):
        return not self.returnTime

class Book2:
    def __init__(self, number):
        self.number = number
        self.history = []

    def addTimeStamp(self, rentTime, returnTime):
        self.history.append(TimeStamp(rentTime, returnTime))
        
