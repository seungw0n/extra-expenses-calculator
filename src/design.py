# @author: seungw0n

from datetime import datetime

class Restaurant:
    def __init__(self, rName: str, employeeNames: list, price: float):
        self.rName = rName
        self.employeeNames = employeeNames
        self.price = price
    
    def __str__(self) -> str:
        return "음식점: " + self.rName + " 교직원: " + str(self.employeeNames) + " 가격: " + str(self.price)
