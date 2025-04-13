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

#Задание 7
class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients
    def __call__(self, x):
        result = 0
        for power, coeff in enumerate(self.coefficients):
            result += coeff * (x ** power)
        return result
    def __add__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        new_coeffs = []
        for i in range(max_len):
            coeff1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coeff2 = other.coefficients[i] if i < len(other.coefficients) else 0
            new_coeffs.append(coeff1 + coeff2)
        return Polynomial(new_coeffs)
poly = Polynomial([10, -1])
print(poly(0))
print(poly(1))
print(poly(2))

#Задание 8
class Queue:
    def __init__(self, *args):
        self.items = list(args)
    def append(self, *values):
        self.items.extend(values)
    def copy(self):
        return Queue(*self.items)
    def pop(self):
        return self.items.pop(0) if self.items else None
    def extend(self, queue):
        self.items.extend(queue.items)
    def next(self):
        return Queue(*self.items[1:]) if len(self.items) > 1 else Queue()
    def __add__(self, other):
        return Queue(*(self.items + other.items))
    def __iadd__(self, other):
        self.extend(other)
        return self
    def __eq__(self, other):
        return self.items == other.items
    def __rshift__(self, n):
        return Queue(*self.items[n:]) if n < len(self.items) else Queue()
    def __str__(self):
        return "[" + " -> ".join(map(str, self.items)) + "]" if self.items else "[]"
    def __next__(self):
        return self.next()
q1 = Queue(1, 2, 3)
print(q1)
q1.append(4,5)
print(q1)
qx = q1.copy()
print(qx.pop())
print(qx)
q2=q1.copy()
print(q2)
print(q1 == q1, id(q1) == id(q2))
q3 = q2.next()
print(q1, q2, q3, sep = "\n")
print(q1 + q3)
q3.extend(Queue(1,2))
print(q3)
q4 = Queue(1,2)
q4 += q3 >> 4
print(q4)
q5 = next(q4)
print(q4)
print(q5)

#Задание 9 Наследование
class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)
# Примеры использования
triangle = Triangle(3, 4, 5)
print(f"Периметр треугольника: {triangle.perimeter()}") 
equilateral_triangle = EquilateralTriangle(6)
print(f"Периметр равностороннего треугольника: {equilateral_triangle.perimeter()}")

#Задание 10 Задание 11
class Summator:
    def transform(self, n):
        return n
    def sum(self, N):
        return sum(self.transform(i) for i in range(1, N + 1))

class PowerSummator(Summator):
    def __init__(self, b):
        self.b = b
    def transform(self, n):
        return n ** self.b

class SquareSummator(PowerSummator):
    def __init__(self):
        super().__init__(2)

class CubeSummator(PowerSummator):
    def __init__(self):
        super().__init__(3)

#Задание 12
class A:
    def __str__(self):
        return 'A_str_method'
    def hello(self):
        print('Hello')

class B:
    def __str__(self):
        return 'B_str_method'
    def good_evening(self):
        print('Good evening')

class C(A, B):
    pass

class D(B, A):
    pass
c = C()
c.hello()
c.good_evening()
print(c)
d = D()
d.hello()
d.good_evening()
print(c)
print(d)

#Задание 13
import math 
class Weapon:
    def __init__(self, name, damage, range_):
        self.name = name
        self.damage = damage
        self.range = range_
    def hit(self, actor, target):
        if not target.is_alive():
            print("Враг уже повержен")
            return
        actor_x, actor_y = actor.get_coords()
        target_x, target_y = target.get_coords()
        distance = math.sqrt((actor_x - target_x) ** 2 + (actor_y - target_y) ** 2)
        if distance > self.range:
            print(f"Враг слишком далеко для оружия {self.name}")
            return
        print(f"Врагу нанесен урон оружием {self.name} в размере {self.damage}")
        target.get_damage(self.damage)
    def __str__(self):
        return self.name

class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp
    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y
    def is_alive(self):
        return self.hp > 0
    def get_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
    def get_coords(self):
        return (self.pos_x, self.pos_y)

class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon
    def hit(self, target):
        if not isinstance(target, MainHero):
            print("Могу ударить только Главного героя")
            return
        self.weapon.hit(self, target)
    def __str__(self):
        return f"Враг на позиции ({self.pos_x}, {self.pos_y}) с оружием {self.weapon}"

class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, name, hp):
        super().__init__(pos_x, pos_y, hp)
        self.name = name
        self.weapons = []
        self.current_weapon_index = -1
    def hit(self, target):
        if not self.weapons:
            print("Я безоружен")
            return
        if not isinstance(target, BaseEnemy):
            print("Могу ударить только Врага")
            return
        self.weapons[self.current_weapon_index].hit(self, target)
    def add_weapon(self, weapon):
        if not isinstance(weapon, Weapon):
            print("Это не оружие")
            return
        self.weapons.append(weapon)
        print(f"Подобрал {weapon}")
        if len(self.weapons) == 1:
            self.current_weapon_index = 0
    def next_weapon(self):
        if not self.weapons:
            print("Я безоружен")
            return
        if len(self.weapons) == 1:
            print("У меня только одно оружие")
            return
        self.current_weapon_index = (self.current_weapon_index + 1) % len(self.weapons)
        print(f"Сменил оружие на {self.weapons[self.current_weapon_index]}")
    def heal(self, amount):
        self.hp += amount
        if self.hp > 200:
            self.hp = 200
        print(f"Использовал флягу с Эстусом, теперь здоровья {self.hp}")
weapon1 = Weapon("Иритилльский меч", 5, 1)
weapon2 = Weapon("Цвайхандер", 7, 2)
weapon3 = Weapon("Меч Фаррона", 3, 10)
weapon4 = Weapon("Черпак", 1000, 1000)
princess = BaseCharacter(100, 100, 100)
archer = BaseEnemy(50, 50, weapon3, 100)
armored_swordsman = BaseEnemy(10, 10, weapon2, 500)
archer. hit(armored_swordsman)
armored_swordsman.move(10, 10)
print(armored_swordsman.get_coords())

main_hero = MainHero(0, 0, "Ashen One", 200)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.add_weapon(weapon1)
main_hero.hit(armored_swordsman)
main_hero.add_weapon(weapon4)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.hit(princess)
main_hero.hit(armored_swordsman)
main_hero.hit(armored_swordsman)

#Задание 14 Проектирование и разработка классов
class MailServer:
    def __init__(self, name):
        self.name = name
        self.mailbox = {}
    def receive_mail(self, user):
        return self.mailbox.pop(user, [])
    def send_mail(self, user, message):
        if user not in self.mailbox:
            self.mailbox[user] = []
        self.mailbox[user].append(message)
    def __str__(self):
        return self.name

class MailClient:
    def __init__(self, server, user):
        self.server = server
        self.user = user
    def receive_mail(self):
        mails = self.server.receive_mail(self.user)
        if mails:
            print(f"Письма для {self.user} на сервере {self.server}:")
            for mail in mails:
                print(f"- {mail}")
        else:
            print(f"Нет новых писем для {self.user}.")
    def send_mail(self, server, user, message):
        if server not in MailSystem.servers:
            print(f"Ошибка: Невозможно отправить письмо на сервер {server}. Он не зарегистрирован.")
            return
        server.send_mail(user, message)
        print(f"Письмо отправлено пользователю {user} на сервере {server}.")

class MailSystem:
    servers = []
    @classmethod
    def register_server(cls, server):
        cls.servers.append(server)
    @classmethod
    def list_servers(cls):
        return [str(server) for server in cls.servers]

if __name__ == "__main__":
    server1 = MailServer("MailServer1")
    server2 = MailServer("MailServer2")
    MailSystem.register_server(server1)
    MailSystem.register_server(server2)
    client1 = MailClient(server1, "user1@example.com")
    client2 = MailClient(server2, "user2@example.com")
    client1.send_mail(server1, "user2@example.com", "Привет от 1")
    client2.send_mail(server1, "user1@example.com", "Привет от 2")
    client1.receive_mail()
    client2.receive_mail()
#Задание 15
def make_negative(x):
    return -x if x > 0 else x
def square(x):
    return x ** 2
def strange_command(x):
    return x + 1 if x % 5 == 0 else x
commands = {
    'make_negative': (lambda x: x > 0, make_negative),
    'square': (lambda x: True, square),
    'strange_command': (lambda x: x % 5 == 0, strange_command)
}
numbers = list(map(int, input().split()))
command = input().strip()
while command in commands:
    condition, transform = commands[command]
    numbers = [transform(x) if condition(x) else x for x in numbers]
    print(' '.join(map(str, numbers)))
    command = input().strip()

#Все хватит я устал
#Задание 16 -------------------------------------------------------------------------

#Задание 17 -------------------------------------------------------------------------

#Задание 18  -------------------------------------------------------------------------