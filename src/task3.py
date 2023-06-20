class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print("Woof!")

    def run(self):
        print(f"{self.name} is running.")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def meow(self):
        print("Meow!")

    def walk(self):
        print(f"{self.name} is walking.")


# Creating instances of the classes
dog = Dog("Bobby", "Bulldog")
cat = Cat("Becky", "Black")

dog.bark()
cat.walk()
