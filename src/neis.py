# @author: seungw0n
from datetime import datetime
from excel import openExcel, readNeis


def isWeekday(d: str) -> bool:
    """ 주말인지 아닌지 확인 """
    date = datetime.strptime(d, "%Y.%m.%d")
    return True if date.weekday() <= 4 else False


def getTotalTime(startHour: int, startMin: int, endHour: int, endMin: int) -> tuple:
    """ 초과근무시간 합 구하는 함수 """
    totalHour = endHour - startHour
    totalMin = endMin - endHour

    if totalMin < 0:
        totalHour -= 1
        totalMin = 60 + totalMin
    
    return totalHour, totalMin


def isValidStartTime(targetHour: int, targetMin: int, startHour: int, startMin: int) -> bool:
    """ targetHour:targetMin 일과시간 후 부터만 특근매식비 지원 """
    if startHour > targetHour:
        return True

    if startHour == targetHour and startMin >= targetMin:
        return True

    return False


def isValid(date: str, totalHour: int, targetHour: int, targetMin: int, startHour: int, startMin: int) -> bool:
    """ 특근매식비를 받을 수 있는 조건인지 확인 함
    조건
        평일: 일과시간 이후 초과근무 1시간 이상
        주말: 초과근무 1시간 이상
    """
    if totalHour >= 1:
        if not isWeekday(date) or (isWeekday(date) and isValidStartTime(targetHour, targetMin, startHour, startMin)):
            return True

    return False


def neisLog(filename: str, targetHour: int, targetMin: int) -> tuple:
    """ NEIS 초과근무확인에서 특근매식비 지급여부를 나눔 """
    wb, _ = openExcel(filename)
    total = readNeis(wb)

    validLog = dict()
    validNamesLog = dict()
    invalidLog = dict()

    for key, val in total.items():
        validValues = []
        validNames = []
        invalidValues = []

        for v in val:  # [이름, 시작시간, 끝난시간, 총합]
            name = v[0].split("(")[0]
            startHour = int(v[1].split(":")[0])
            startMin = int(v[1].split(":")[1])
            endHour = int(v[2].split(":")[0])
            endMin = int(v[2].split(":")[1])
            totalHour, totalMin = getTotalTime(startHour=startHour, startMin=startMin, endHour=endHour, endMin=endMin)

            validation = isValid(key, totalHour, targetHour, targetMin, startHour, startMin)
            v[0] = name  # change name 
            if validation:
                validValues.append(v)
                validNames.append(name)
            else:
                invalidValues.append(v)

        validLog[key] = validValues
        validNamesLog[key] = validNames
        invalidLog[key] = invalidValues

    return validLog, validNamesLog, invalidLog


# valid, validNames, invalid = neisLog("./files/초과근무확인8월분.xlsx", 16, 50)
# print(validNames)