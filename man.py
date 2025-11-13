class Man:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        def set_age(self, age):
            if age < 14:
                self.__age = age
                print("ребенок")

    def show_info(self):
        print(f"имя: {self.name}\n"+
              f"возраст: {self.age}")

if __name__ == '__main__':
    man1 = Man("Вера", 27)
    man2 = Man("Оля", 25)
    man3 = Man("Петя", 12)

    man1.show_info()