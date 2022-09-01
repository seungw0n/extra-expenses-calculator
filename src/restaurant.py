# @author: seungw0n

from excel import openExcel, readLedger
from design import Ledger


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

    return result

#
# wb, sheetnames = openExcel("../특근매식비장부.xlsx")
# excelResult = readLedger(wb, sheetnames)
# ledgers = restaurantLog(excelResult)
#
# for l in ledgers:
#     print(l)
