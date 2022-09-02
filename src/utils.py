from neis import neisLog
from restaurant import restaurantLog


def run(neisFilename: str, restaurantFilename: str):
    validLog, validEmployeeNames, invalidLog = neisLog(filename=neisFilename, targetHour=16, targetMin=50)
    ledgers = restaurantLog(filename=restaurantFilename)

    # sort by date
    ledgers.sort(key=lambda x: x.date)

    invalidEmployees = list()

    for ledger in ledgers:
        date = ledger.date
        employeeNames = ledger.employeeNames
        overPrice = ledger.overPrice

        if overPrice != 0:
            invalidEmployees.append([date, str(employeeNames), ledger.restaurantName, "이유: 특근매식비 초과 사용"])

        validNames = validEmployeeNames[date]

        for name in employeeNames:  # 특근매식비 지급 대상 아닌 사람이 먹었을 경우
            if name == "노종미":
                print(ledger)
            if name in validNames:
                validEmployeeNames[date].remove(name)
            else:
                invalidEmployees.append([date, name, ledger.restaurantName, "이유: 특근매식비 지급 대상이 아님"])
    # 방학 : 7월 20일
    # 개학 : 8월 17일
    for n in invalidEmployees:
        print(n)
    # print(validEmployeeNames)

run("./files/초과근무확인8월분.xlsx", "./files/8월 특근매식비장부(수정).xlsx")


