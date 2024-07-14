class Calc:
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        return self.num1 + self.num2
    
    def substract(self):
        if self.num1 >= self.num2:
            return self.num1 - self.num2
        else:
            return self.num2 - self.num1
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        return self.num1 / self.num2