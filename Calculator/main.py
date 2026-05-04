class Calculator:
    def __init__(self, initial_value=0):
        self.value = initial_value

    def add(self, num):
        self.value += num
        return self.value

    def subtract(self, num):
        self.value -= num
        return self.value

    def multiply(self, num):
        self.value *= num
        return self.value

    def divide(self, num):
        if num == 0:
            raise ValueError("Cannot divide by zero")
        self.value /= num
        return self.value

    def reset(self):
        self.value = 0
        return self.value
