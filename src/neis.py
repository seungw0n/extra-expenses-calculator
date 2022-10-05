# @author: seungw0n
from datetime import datetime
from src.excel import openExcel, readNeis

"""
Overview: NEIS 에서 발급받은 초과근무확인 엑셀을 이용하여 특근매식비 지급 대상인지 아닌지 확인

시작시간과 종료시간이 00:00 일 경우는 초과근무를 하지 않은 경우

    근무일
        1. 초과근무는 일과시간 이후 부터 계산됨
        2. 실제초과근무시간의 종료시간 - 시작시간이 1시간 이상 일 경우 지급 대상

    휴일
        1. 주말 (토,일)일 경우만 계산됨, 그 이후 다른 휴일은 적용 안 됨
        2. 실제초과근무시간의 종료시간 - 시작시간이 1시간 이상 일 경우 지급 대상
"""


def isWeekday(d: str) -> bool:
    """ 주말인지 아닌지 확인 """
    date = datetime.strptime(d, "%Y.%m.%d")
    return True if date.weekday() <= 4 else False


def isValidStartTime(officeHour: int, officeMin: int, startHour: int, startMin: int) -> bool:
    """ officeHour:officeMin 일과시간 후 부터만 특근매식비 지원 """
    if startHour > officeHour:
        return True

    if startHour == officeHour and startMin >= officeMin:
        return True

    return False


def getOvertime(startHour: int, startMin: int, endHour: int, endMin: int) -> tuple:
    """ 초과근무시간 합 구하는 함수 """
    totalHour = endHour - startHour
    totalMin = endMin - startMin

    if totalMin < 0:
        totalHour -= 1
        totalMin = 60 + totalMin
    
    return totalHour, totalMin


def getValidList(filename: str, officeHour: int, officeMin: int):
    wb, _ = openExcel(filename)
    data = readNeis(wb)
    """
        data = { "날짜" : [ [이름, 시작시간, 종료시간], ....], "날짜" :.. }
    """

    validLog = dict()
    validNames = dict()
    invalidLog = dict()

    for date, lst in data.items():
        validLog[date] = []
        validNames[date] = []
        invalidLog[date] = []

        for datum in lst:
            name, start, end = datum[0], datum[1], datum[2]
            name = name.split("(")[0]
            startHour = int(start.split(":")[0])
            startMin = int(start.split(":")[1])
            endHour = int(end.split(":")[0])
            endMin = int(end.split(":")[1])

            flag = False  # 지급여부대상

            if isWeekday(date):  # 평일
                if isValidStartTime(officeHour, officeMin, startHour, startMin) and getOvertime(startHour, startMin, endHour, endMin)[0] >= 1:
                    flag = True
            else:  # 주말
                if getOvertime(startHour, startMin, endHour, endMin)[0] >= 1:
                    flag = True

            if flag:
                validLog[date].append([name, startHour, startMin, endHour, endMin])
                validNames[date].append(name)
            else:
                invalidLog[date].append([name, startHour, startMin, endHour, endMin])

    return validLog, validNames, invalidLog


# valid, validNames, invalid = getValidList("../files/202209/초과근무확인 9월.xlsx", 16, 50)
# for k, v in valid.items():
#     print("날짜: " + k)
#     print("\t", v)
