class Dog():
    def __init__(self, dogName, myColour):
        self.__name = dogName
        self.__colour = myColour

    def bark(self, barkTimes):
        for n in range(barkTimes):
            print("Woof!")


class Puppy(Dog):
    def __init__(self, dogName, myColour):
        super().__init__(dogName, myColour)

    def bark(self, barkTimes):
        for n in range(barkTimes):
            print("Yip!")
