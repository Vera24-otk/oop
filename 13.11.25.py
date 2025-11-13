class Cat:
    def __init__(self, name,color,breed):
        self.name = name
        self.color = color
        self.breed = breed

    def show_info(self):
        print(f"кличка:{self.name}\n"+
              f"цвет:{self.color}\n"+
              f"порода:{self.breed}")

if __name__ == '__main__':
    cat1 = Cat("Myrka", "red", "bengalskaya")
    cat2 = Cat("Myrka", "red", "bengalskaya")
    cat3 = Cat("Myrka", "red","bengalskaya")

    print(cat1)
