class House:
    def __init__(self, name: str, number_of_floors: int):
        self.name = name  # имя
        self.number_of_floors = number_of_floors  # кол-во этажей
        self.__str__()

    def go_to(self, new_floor: int):
        n = 1
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этаже не существует")
        else:
            while n <= new_floor:
                print(n)
                n += 1

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return str(f"Название: {self.name}, кол-во этажей: {self.number_of_floors}")

    def __eq__(self, other):  # ==
        if isinstance(other, int):
            return self.number_of_floors == other
        elif isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            return "Ошибка! Не правильный тип данных"

    def __lt__(self, other):  # <
        if isinstance(other, int):
            return self.number_of_floors < other
        elif isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            return "Ошибка! Не правильный тип данных"

    def __le__(self, other):  # <=
        if isinstance(other, int):
            return self.number_of_floors <= other
        elif isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            return "Ошибка! Не правильный тип данных"

    def __gt__(self, other):  # >
        if isinstance(other, int):
            return self.number_of_floors > other
        elif isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            return "Ошибка! Не правильный тип данных"

    def __ge__(self, other):  # >=
        if isinstance(other, int):
            return self.number_of_floors >= other
        elif isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            return "Ошибка! Не правильный тип данных"

    def __ne__(self, other):  # !=
        if isinstance(other, int):
            return self.number_of_floors != other
        elif isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            return "Ошибка! Не правильный тип данных"

    def __add__(self, value):  # увеличивает кол-во этажей на переданное значение value
        if isinstance(value, int):
            return self.number_of_floors + value
        else:
            return "Ошибка! Не правильный тип данных"

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__