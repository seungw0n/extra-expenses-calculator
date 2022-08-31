# @description: Collects all functions related to handling files
# @author: seungw0n
# @installed-packages: openpyxl

from openpyxl import load_workbook, Workbook, worksheet
from datetime import datetime

def openExcel(filename: str) -> list:
    """ filename must contain extension """
    wb = load_workbook(filename=filename)
    return wb, wb.sheetnames

def readNeis(wb: Workbook) -> dict:
    sheet = wb.active
    
    result = dict()

    values = list(sheet.values)

    for i in range(2, len(values)):
        date = values[i][3]
        value = [values[i][2], values[i][8], values[i][9], values[i][10]]

        if date in result:
            result[date].append(value)
        else:
            result[date] = [value]
    
    return result

def readLedger(wb: Workbook, sheetnames: list) -> dict:
    result = dict()

    for sheetname in sheetnames:
        sheet = wb[sheetname]
        values = list(sheet.values)
        data = dict()

        for i in range(1, len(values)):
            date = values[i][0]
            price = values[i][1]
            names = values[i][2]
            
            if date == None:
                break

            if date in data:
                data[date].append([names, price])
            else:
                data[date] = [[names, price]]

        result[sheetname] = data

    return result
"""
if __name__ == '__main__':
    # print(openExcel("7월 특근매식비.xlsx"))
    # wb, sheetnames = openExcel("초과근무확인(7월분_나이스원본).xlsx")
    # result = readNeis(wb)
    # print(result)
    # readFromNeis(wb)
    # date = datetime.strptime("2022.07.10", "%Y.%m.%d")
    # print(date.weekday())
    a, b = openExcel("특근매식비장부.xlsx")
    d = readLedger(a, b)

    for key in d:
        print(key)
        print(d[key])
        print()

"""