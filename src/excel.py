# @description: Collects all functions related to handling files
# @author: seungw0n
# @installed-packages: openpyxl

from openpyxl import load_workbook, Workbook, worksheet

def restaurantSheets(filename: str) -> list:
    """ filename must contain extension """
    wb = load_workbook(filename=filename)
    sheetnames = wb.sheetnames

    sheets = list()

    for name in sheetnames:
        sheets.append(wb[name])
    
    return sheets

def overtimeSheet(filename: str) -> worksheet:
    """ 1번째 sheet을 이용 """
    wb = load_workbook(filename=filename)
    ws = wb.active
    print(ws['B3'].value)
    return ws

if __name__ == '__main__':
    restaurantSheets("./", "7월 특근매식비.xlsx")
    overtimeSheet("./", "초과근무확인(7월분).xlsx")
