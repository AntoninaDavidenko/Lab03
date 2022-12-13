class Rational:

    def __init__(self):
        self.__numerator = 1
        self.__denominator = 2
        self.__second_numerator = 1
        self.__second_denominator = 2

    def set_numerator(self, numerator):
        self.__numerator = numerator

    def set_denominator(self, denominator):
        self.__denominator = denominator

    def set_second_numerator(self, second_numerator):
        self.__second_numerator = second_numerator

    def set_second_denominator(self, second_denominator):
        self.__second_denominator = second_denominator

    def standard_form(self):
        print(f"{self.__numerator}/{self.__denominator}")

    def floating_point(self):
        result = self.__numerator / self.__denominator
        print(int(result))

    def add(self):
        numerator = self.__numerator * self.__second_denominator + self.__second_numerator * self.__denominator
        denominator = self.__denominator * self.__second_denominator
        result = numerator / denominator
        print(int(result))

    def sub(self):
        numerator = self.__numerator * self.__second_denominator - self.__second_numerator * self.__denominator
        denominator = self.__denominator * self.__second_denominator
        result = numerator / denominator
        print(int(result))

    def mul(self):
        numerator = self.__numerator * self.__second_numerator
        denominator = self.__denominator * self.__second_denominator
        result = numerator / denominator
        print(int(result))

    def div(self):
        numerator = self.__numerator * self.__second_denominator
        denominator = self.__denominator * self.__second_numerator
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
