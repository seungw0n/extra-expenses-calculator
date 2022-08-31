# @author: seungw0n
from datetime import datetime
from excel import openExcel, readLedger
from design import Restaurant

def splitNames(names: str) -> list:
    names = names.replace(" ", "")
    names = names.split(",")
    names = [x for x in names if x]
    return names 
    
def createObj(excelResult: dict) -> dict:
    result = dict()

    for key, value in excelResult.items():  # {음식점: {날짜: [[이름, 가격], ... ]}}
        for k, v in value.items():  # {날짜: [[이름, 가격], ...]}
            for element in v:
                names = splitNames(element[0])
                price = element[1]

                r = Restaurant(rName=key, employeeNames=names, price=price)
                
                if k in result:
                    result[k].append(r)
                else:
                    result[k] = [r]
    
    return result
            



def ledgerLog(filename: str):
    wb, sheetnames = openExcel(filename=filename)
    excelResult = readLedger(wb, sheetnames)
    
    result = createObj(excelResult)

    for k, v in result.items():
        print(k)
        for e in v:
            print("\t" + str(e))



ledgerLog("특근매식비장부.xlsx")