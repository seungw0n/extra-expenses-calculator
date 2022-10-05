# @author: seungw0n

from src.excel import openExcel, readLedger


class Ledger:
    def __init__(self, date: str, restaurantName: str, employeeNames: str, price: float):
        self.date = date
        self.restaurantName = restaurantName

        employeeNames = employeeNames.replace(" ", "")
        employeeNames = employeeNames.split(",")
        employeeNames = [x for x in employeeNames if x]

        self.employeeNames = employeeNames
        self.price = price

        numEmployees = len(employeeNames)
        isValidPrice = self.price / numEmployees <= 8000

        self.overPrice = 0
        if not isValidPrice:
            self.overPrice = self.price - (numEmployees * 8000)

    def __str__(self) -> str:
        return "날짜: " + self.date + " 음식점: " + self.restaurantName + " 교직원: " + str(self.employeeNames) + " 가격: " + str(
            self.price)


def restaurantLog(filename: str) -> list:
    wb, sheetnames = openExcel(filename)
    excelResult = readLedger(wb, sheetnames)

    result = list()
    """
    class Ledger:
        def __init__(self, date: str, restaurantName: str, employeeNames: str, price: float)
    """
    for key, value in excelResult.items():
        for lst in value:
            result.append(Ledger(key, lst[0], lst[1], lst[2]))

    result.sort(key=lambda x: x.date)

    return result

#
# ledgers = restaurantLog("../files/202209/9월 특근매식비장부.xlsx")
# print(len(ledgers))
# for l in ledgers:
#     print(l)
