# parent class
class Animal:
    def speak(self):
        print("Animal is speaking")


# Child class
class dog(Animal):
    def bark(self):
        print("Dog is barking")


class cat(Animal):
    def meow(self):
        print("cat is meowing")


d = dog()
d.speak()

c = cat()
c.speak()
