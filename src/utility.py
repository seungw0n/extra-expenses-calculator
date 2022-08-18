# @author: seungw0n
from datetime import datetime
from excel import restaurantSheets, overtimeSheet
from design import Overtime, Restaurant

def isWeekday(date: datetime) -> bool:
    """ 주말인지 아닌지 확인 """
    return True if date.weekday() <= 4 else False

def isValidStartTime(startHour: int, startMin: int) -> bool:
    """ 16:50 분 일과시간 후 부터만 특근매식비 지원 """
    if startHour > 16:
        return True
    
    if startHour == 16 and startMin >= 50:
        return True
    
    return False

def validCheck(date: datetime, startHour: int, startMin: int, totalHour: int) -> bool:
    if totalHour < 1:
        return False
    
    if isWeekday(date=date):
        return isValidStartTime(startHour, startMin)
    else:
        return True

def overtimes(filename):
    ws = overtimeSheet(filename)

    objs = dict()

    for row in ws.iter_rows(min_row=3):
        lst = list() # [name, date, start, end, sum]
        cnt = 0
        for c in row:
            cnt += 1
            if (cnt == 3 or cnt == 4 or cnt == 9 or cnt == 10 or cnt == 11):
                lst.append(c.value)
        
        obj = Overtime(lst[0], lst[2], lst[3], lst[4])

        if lst[1] in objs:
            objs[lst[1]].append(obj)
        else:
            objs[lst[1]] = [obj]

    for key in objs.keys():
        print(key)
        for o in objs[key]:
            print("\t" + str(o))

    
    return objs
"""
def restaurants(filename):
    sheets = restaurantSheets(filename)

    result = dict()

    for sheet in sheets:
"""

# overtimes("./초과근무확인(7월분).xlsx")
overtimes("./초과근무확인(7월분_나이스원본).xlsx")