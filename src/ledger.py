# @author: seungw0n
from datetime import datetime
from neis import neisLog
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


def ledgerLog(filename: str) -> dict:
    wb, sheetnames = openExcel(filename=filename)

    for sheetname in sheetnames:
        sheet = wb[sheetname]

        




    excelResult = readLedger(wb, sheetnames)
    
    result = createObj(excelResult)  # {date: [Restaurant, Restaurant, ....], ....}

    for k, v in result.items():
        print(k)
        for e in v:
            print("\t" + str(e))


    return result

    

# def createFinalLog(neisFilename: str, ledgerFilename: str) -> tuple:
#     neisValidLog, neisInvalidLog = neisLog(filename=neisFilename)
#     restaurantLog = ledgerLog(filename=ledgerFilename)

#     valid = list()
#     invalid = list()

#     # check if employee is able to eat
#     for date, restuarantObjs in restaurantLog:

#         if len(restuarantObjs) == 0:
#             continue

#         overWorks = neisValidLog[date]
        
#         if len(overWorks) == 0:
#             invalid.append([date, restuarantObjs])
#             continue
        
#         for r in restuarantObjs:
#             names = r.employeeNames

#             for name in names:
#                 for overWork in overWorks:
                    

    
c, w = neisLog("./files/초과근무확인8월분.xlsx", 16, 50)
print(c)
ledgerLog("./files/8월 특근매식비장부.xlsx")