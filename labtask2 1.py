name= "ZAHRA TUL HUSSAN SYED"
rollno= "23108195"
result = name + " " + rollno
print(result)
class basic_calc:
    def __init__(self, num1, num2):
        self.x = num1
        self.y = num2
    def add(self):
        return self.x + self.y
    def subtract(self):
        return self.x - self.y
    def multiply(self):
        return self.x * self.y
    def divide(self):
        if self.y == 0:
            return "division is not possible"
        return self.x / self.y
calculator = basic_calc(67,56)
print("Addition of two number is:", calculator.add())       
print("Subtraction of two number is:", calculator.subtract())  
print("Multiplication of two number is:", calculator.multiply())  
print("Division of two number is:", calculator.divide())      
