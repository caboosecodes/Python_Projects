class Protected_and_private:
    # initializes an object
    def __init__(self):
        # protected variable uses only one underscore
        # acts as a warning to other devs to not use outside of this class
        # does not change the behavior
        self._protectedVar = 45

        # private variable uses double underscore
        # it is harder to access
        self.__privateVar = 32

    # function to print self.__privateVar
    def get_private(self):
        print(self.__privateVar)
    
    # function that changes what self.__private is set to
    def set_private(self, private):
        self.__privateVar = private


object = Protected_and_private()
proObject = object._protectedVar
print(proObject)
priObject = object.get_private()
priObject = object.set_private(29)
priObject = object.get_private()