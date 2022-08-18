# @author: seungw0n

from datetime import datetime

class Overtime:
    def __init__(self, name: str, start: str, end: str, sum: str):
        self.name = name
        self.startHour = start.split(":")[0]
        self.startMin = start.split(":")[1]
        self.endHour = end.split(":")[0]
        self.endMin = end.split(":")[1]
        self.sumHour = sum.split(":")[0]
        self.sumMin = sum.split(":")[1]
    
    def isValid(self):
        return True if int(self.sum) >= 1 else False
    
    def __str__(self):
        return self.name + " " + self.startHour + ":" + self.startMin + " " + self.endHour + ":" + self.endMin + " " + self.sumHour + ":" + self.sumMin
    
class Restaurant:
    def __init__(self, names: list, date: str, price: float):
        self.names = names
        self.date = datetime(year=date.split('.')[0], month=date.split('.')[1], day=date.split('.')[2])
        self.price = price
        # first valid check
        self.isValid = True if price / names <= 8000.0 else False
