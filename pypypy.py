#Задание 1 базовый синтаксис
class BigBell:
    def __init__(self):
        self.toggle = True
    def sound(self):
        if self.toggle:
            print("ding")
        else:
            print("dong")
        self.toggle = not self.toggle
bell = BigBell()
bell.sound()
bell.sound()
bell.sound()
#Задание 2
class Balance:
    def __init__(self):
        self.left_weight = 0
        self.right_weight = 0
    def add_left(self, weight):
        if weight > 0:
            self.left_weight += weight
    def add_right(self, weight):
        if weight > 0:
            self.right_weight += weight
    def result(self):
        if self.left_weight == self.right_weight:
            return '='
        elif self.left_weight > self.right_weight:
            return 'L'
        else:
            return 'R'
balance = Balance()
balance.add_right(10)
balance.add_left(5)
balance.add_left(5)
print(balance.result())
balance.add_left(1)
print(balance.result())
#Задание 3
class Selector:
    def __init__(self, numbers):
        self.numbers = numbers
    def get_odds(self):
        return [num for num in self.numbers if num % 2 != 0]
    def get_evens(self):
        return [num for num in self.numbers if num % 2 == 0]
values = [11, 12, 14, 15, 16, 22, 44, 66]
selector = Selector(values)
odds = selector.get_odds()
evens = selector.get_evens()
print(' '.join(map(str, odds)))
print(' '.join(map(str, evens)))
#Задание 4 специальные методы


