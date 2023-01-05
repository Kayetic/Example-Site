class Dog():
    def __init__(self, dogName, myColour):
        self.__name = dogName
        self.__colour = myColour

    def bark(self, barkTimes):
        for n in range(barkTimes):
            print("Woof!")

    def setColor(self, myColour):
        self.__colour = myColour

    def getColour(self):
        return self.__colour

    def getName(self):
        return self.__name

    def printDogDetails(self):
        print(self.__name, self.__colour)


class Puppy(Dog):
    def __init__(self, dogName, myColour):
        super().__init__(dogName, myColour)

    __shoesChewed = 0

    def chewShoe(self, myShoesChewed):
        self.__shoesChewed += myShoesChewed

    def getShoesChewed(self):
        return self.__shoesChewed

    # The super() function allows you to call a method from the parent class
    # In this case, the bark() method from the Dog class

    def bark(self, barkTimes):
        return super().bark(barkTimes)


puppy1 = Puppy("Fido", "Brown")
puppy1.bark(3)
