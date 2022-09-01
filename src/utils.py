from src.neis import neisLog
from src.restaurant import restaurantLog


def run(neisFilename: str, restaurantFilename: str):
    validLog, validEmployeeNames, invalidLog = neisLog(filename=neisFilename, targetHour=16, targetMin=50)
    ledgers = restaurantLog(filename=restaurantFilename)

    print(validEmployeeNames)

run("../초과근무확인(7월분_나이스원본).xlsx", "../특근매식비장부.xlsx")