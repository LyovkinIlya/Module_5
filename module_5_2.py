class House:
    def __init__(self, name: str, number_of_floors: int):
        self.name = name # имя
        self.number_of_floors = number_of_floors # кол-во этажей
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

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)      # Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)      # Название: ЖК Акация, кол-во этажей: 20
print(len(h1)) # 10
print(len(h2)) # 20