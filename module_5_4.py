class House:
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

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
            self.number_of_floors = self.number_of_floors + value
            return self
        else:
            return "Ошибка! Не правильный тип данных"

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

# Консоль:
# ['ЖК Эльбрус']
# ['ЖК Эльбрус', 'ЖК Акация']
# ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# ЖК Акация снесён, но он останется в истории
# ЖК Матрёшки снесён, но он останется в истории
# ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# ЖК Эльбрус снесён, но он останется в истории