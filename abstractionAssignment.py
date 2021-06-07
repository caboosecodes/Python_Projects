
# to declare an abstract class you first need to import the abc module
from abc import ABC, abstractmethod

# coaster is the abstract class where abstract and any other methods can be defined
class Coaster(ABC):
    # normal method
    def height(self, inches):
        # str() method to turn the integer to string datatype
        print("You are {} inches tall, you can ride the coaster".format(str(inches)))
    # abstractmethod from the abc module
    @abstractmethod
    def tooShort(self, inches):
        # pass keyword used in place of future code
        pass

# child class
class NoCoaster(Coaster):
    # function from the parent class Coaster()
    def tooShort(self, inches):
        print("You are {} inches tall, sorry you are not tall enough to ride the coaster".format(str(inches)))

heightInches = NoCoaster()
heightInches.height(72)
heightInches.tooShort(60)