class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def drive(self):
        print("Driving")

    def set_age(self, age):
        self.age = age

    def get_age(self):
        print(f"I am now {self.age} years old")

    def get_older(self, amount):
        self.age += amount
        print(f"I am now {self.age} years old")


person1 = Person("John", 36)
person1.drive()
person1.set_age(40)
person1.get_age()
person1.get_older(5)
