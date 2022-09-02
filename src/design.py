# @author: seungw0n


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
        return "날짜: " + self.date + " 음식점: " + self.restaurantName + " 교직원: " + str(self.employeeNames) + " 가격: " + str(self.price)
