from datetime import timedelta, datetime


class Calendar:
    def __init__(self, date):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = value

    def __iadd__(self, other):
        if isinstance(other, Calendar):
            self.__date += other.__date
            return self.__date
        else:
            raise TypeError(u'unsupported operand type(s) for ''''{}'''' and ''''{}'''''.format(type(self).__name__, type(other).__name__))

    def __isub__(self, other):
        if isinstance(other, Calendar):
            self.__date -= other.__date
            return self.__date
        else:
            raise TypeError(u'unsupported operand type(s) for ''''{}'''' and ''''{}'''''.format(type(self).__name__, type(other).__name__))

    def __le__(self, other):
        if isinstance(other, Calendar):
            return self.__date <= other.__date
        else:
            raise TypeError(u'unsupported operand type(s) for ''''{}'''' and ''''{}'''''.format(type(self).__name__, type(other).__name__))

    def __ge__(self, other):
        if isinstance(other, Calendar):
            return self.__date >= other.__date
        else:
            raise TypeError(u'unsupported operand type(s) for ''''{}'''' and ''''{}'''''.format(type(self).__name__, type(other).__name__))

    def __lt__(self, other):
        if isinstance(other, Calendar):
            return self.__date < other.__date
        else:
            raise TypeError(u'unsupported operand type(s) for ''''{}'''' and ''''{}'''''.format(type(self).__name__, type(other).__name__))

    def __gt__(self, other):
        if isinstance(other, Calendar):
            return self.__date > other.__date
        else:
            raise TypeError(u'unsupported operand type(s) for ''''{}'''' and ''''{}'''''.format(type(self).__name__, type(other).__name__))

    def __eq__(self, other):
        if isinstance(other, Calendar):
            return self.__date == other.__date
        else:
            raise TypeError(u'unsupported operand type(s) for ''''{}'''' and ''''{}'''''.format(type(self).__name__, type(other).__name__))

    def __ne__(self, other):
        if isinstance(other, Calendar):
            return self.__date != other.__date
        else:
            raise TypeError(u'unsupported operand type(s) for ''''{}'''' and ''''{}'''''.format(type(self).__name__, type(other).__name__))


day_one = datetime(2022, 7, 3)
day_two1 = datetime(2022, 7, 4)
day_two = timedelta(4)
print(day_two1 > day_one)
print(day_one + day_two)
