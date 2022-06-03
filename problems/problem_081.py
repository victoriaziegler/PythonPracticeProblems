# Write four classes that meet these requirements.
#
# Name:       Animal
#
# Required state:
#    * number_of_legs, the number of legs the animal has
#    * primary_color, the primary color of the animal
#
# Behavior:
#    * describe()       # Returns a string that describes that animal
#                         in the format
#                                self.__class__.__name__
#                                + " has "
#                                + str(self.number_of_legs)
#                                + " legs and is primarily "
#                                + self.primary_color
#
#
# Name:       Dog, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Bark!"
#
#
#
# Name:       Cat, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Miao!"
#
#
#
# Name:       Snake, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Sssssss!"


class Animal:
    def __init__(self, number_of_legs, primary_color):
        self.number_of_legs = number_of_legs
        self.primary_color = primary_color

    def describe(self):
        return f"{self.__class__.__name__} has {str(self.number_of_legs)} legs and is primarily {self.primary_color}."


class Dog(Animal):
    def speak(self):
        return "Bark!"


class Cat(Animal):
    def speak(self):
        return "Miao!"


class Snake(Animal):
    def speak(self):
        return "Sssss!"


dog1 = Dog(4, "black")
print(dog1.describe() + " Dog should say " + Dog.speak(dog1))

cat1 = Cat(4, "gray")
print(cat1.describe() + " Cat should say " + Cat.speak(cat1))

snake1 = Snake(0, "brown")
print(snake1.describe() + " Snake should say " + Snake.speak(snake1))
