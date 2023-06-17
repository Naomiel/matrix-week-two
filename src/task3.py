class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


def bark():
    print("Woof!")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def run(self):
        print(f"{self.name} is running.")


def meow():
    print("Meow!")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def walk(self):
        print(f"{self.name} is walking.")


# Creating instances of the classes
dog = Dog("Bobby", "Bulldog")
cat = Cat("Becky", "Black")

bark()
cat.walk()

