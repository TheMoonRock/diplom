class Person:
    #конструктор
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name} Age: {self.age}")

tom = Person("Tom", 22)

print(tom.name)
print(tom.age)

tom.age = 37
print(tom.age)

tom.display_info()
