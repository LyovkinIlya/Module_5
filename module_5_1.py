class House:
    def __init__(self, name: str, number_of_floors: int):
        self.name = name # имя
        self.number_of_floors = number_of_floors # кол-во этажей

    def go_to(self, new_floor: int):
        n = 1
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этаже не существует")
        else:
            while n <= new_floor:
                print(n)
                n += 1


h1 = House('ЖК Горский', 18)
h1.go_to(int(input(f"Укажите номер этажа, на который нужно приехать от 1 до {h1.number_of_floors}: ")))