class Rational:

    def __init__(self):
        self.numerator = 1
        self.denominator = 2
        self.second_numerator = 1
        self.second_denominator = 2

    def set_numerator(self, numerator):
        self.numerator = numerator

    def set_denominator(self, denominator):
        self.denominator = denominator

    def set_second_numerator(self, second_numerator):
        self.second_numerator = second_numerator

    def set_second_denominator(self, second_denominator):
        self.second_denominator = second_denominator

    def standard_form(self):
        print(f"{self.numerator}/{self.denominator}")

    def floating_point(self):
        result = self.numerator / self.denominator
        print(int(result))

    def add(self):
        numerator = self.numerator * self.second_denominator + self.second_numerator * self.denominator
        denominator = self.denominator * self.second_denominator
        result = numerator / denominator
        print(int(result))

    def sub(self):
        numerator = self.numerator * self.second_denominator - self.second_numerator * self.denominator
        denominator = self.denominator * self.second_denominator
        result = numerator / denominator
        print(int(result))

    def mul(self):
        numerator = self.numerator * self.second_numerator
        denominator = self.denominator * self.second_denominator
        result = numerator / denominator
        print(int(result))

    def div(self):
        numerator = self.numerator * self.second_denominator
        denominator = self.denominator * self.second_numerator
        result = numerator / denominator
        print(int(result))


pr = Rational()
pr.set_numerator(3)
pr.set_denominator(4)
pr.set_second_numerator(2)
pr.set_second_denominator(4)
pr.add()
pr.sub()
pr.mul()
pr.div()
