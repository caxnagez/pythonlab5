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
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __ne__(self, other):
        return not self.__eq__(other)
p1 = Point(1,2)
p2 = Point(5,6)
if p1 == p2:
    print("equal true")
else:
    print("equal false")
    
#Задание 5
class ReversedList:
    def __init__(self, original_list):
        self.original_list = original_list
    def __len__(self):
        return len(self.original_list)
    def __getitem__(self, index):
        if index < 0 or index >= len(self.original_list):
            raise IndexError("Index Error")
        return self.original_list[len(self.original_list) - 1 - index]
r1 = ReversedList([10, 20, 30])
print(len(r1))
for i in range(len(r1)):
    print(r1[i])
r2 = ReversedList([])
print(len(r2))

#Задание 6
class SparseArray:
    def __init__(self): #Хранит только НЕ НУЛЕВЫЕ значения индексов
        self.data = {}
    def __setitem__(self, index, value):
        if value != 0:
            self.data[index] = value
        elif index in self.data:
            del self.data[index]
    def __getitem__(self, index):
        return self.data.get(index, 0) 
if __name__ == "__main__":
    arr = SparseArray()
    arr[1] = 10
    arr[8] = 20
    for i in range(10):
        print('arr[{}] = {}'.format(i, arr[i]))
    arr[10] = 123
    for i in range(8, 13):
        print('arr[{}] = {}'.format(i, arr[i]))
    arr[999999999] = 0
    arr[1000000000] = 123
    print('arr[1000000000] = {}'.format(arr[1000000000]))