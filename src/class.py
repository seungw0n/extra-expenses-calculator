# @author: seungw0n

from datetime import datetime

class Person:
    def __init__(self, name: str, hourStart: int, hourEnd: int, dHour: int, dMin: int):
        self.name = name
        self.hourStart = hourStart
        self.hourEnd = hourEnd
        self.dHour = dHour
        self.dMin = dMin
        # first valid check
        self.isValid = True if dHour >= 1 else False
    
class History:
    def __init__(self, names: list, date: str, price: float):
        self.names = names
        self.date = datetime(year=date.split('.')[0], month=date.split('.')[1], day=date.split('.')[2])
        self.price = price
        # first valid check
        self.isValid = True if price / names <= 8000.0 else False


def isWeekday(date: datetime) -> bool:
    return True if date.weekday() <= 4 else False
