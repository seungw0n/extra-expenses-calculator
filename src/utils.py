from src.neis import getValidList
from src.restaurant import restaurantLog


def run(neisFilename: str, restaurantFilename: str):
    validLog, validEmployeeNames, invalidLog = getValidList(filename=neisFilename, officeHour=16, officeMin=50)
    ledgers = restaurantLog(filename=restaurantFilename)

    invalidEmployees = list()

    for ledger in ledgers:
        date = ledger.date
        employeeNames = ledger.employeeNames
        overPrice = ledger.overPrice

        if overPrice != 0:
            invalidEmployees.append([date, str(employeeNames), ledger.restaurantName, "이유: 특근매식비 초과 사용"])

        validNames = validEmployeeNames[date]

        for name in employeeNames:  # 특근매식비 지급 대상 아닌 사람이 먹었을 경우
            if name in validNames:
                validEmployeeNames[date].remove(name)
            else:
                invalidEmployees.append([date, name, ledger.restaurantName, "이유: 특근매식비 지급 대상이 아님"])

    for n in invalidEmployees:
        print(n)
        for invalid in invalidLog[n[0]]:
            if invalid[0] == n[1]:
                print("\t", "시작시간", invalid[1], ":", invalid[2], "종료시간", invalid[3], ":", invalid[4])

    # print(validEmployeeNames)

run("../files/202209/초과근무확인 9월.xlsx", "../files/202209/9월 특근매식비장부.xlsx")


