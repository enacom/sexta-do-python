class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtraction(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        # return a ** b
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Can't divide by zero")
        return a / b

    def power(self, a, b):
        result = 1
        for _ in range(b):
            result = self.multiply(result, a)
        return result


if __name__ == '__main__':
    calc = Calculator()
    print(calc.power(2, 10))
