


# parent class
class Organism:
    name = 'Uknown'
    species = 'Uknown'
    # data type None is nothing
    legs = None
    arms = None
    dna = 'Sequence A'
    origin = 'Uknown'
    carbon_based = True

    # key word self allows access to all the things inside that class
    def information(self):
        msg = '\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}'.format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg

# child class instance
class Human(Organism):
    name = 'MacGuyver'
    species = 'Homosapien'
    legs = 2
    arms = 2
    origin = 'Earth'

    def ingenuity(self):
        msg = '\nCreates a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape!'
        return msg


# another child class instance
class Dog(Organism):
    name = 'Spot'
    species = 'Canine'
    legs = 4
    arms = 0
    dna = 'Sequence B'
    origin = 'Earth'

    def bite(self):
        msg = '\nEmits a loud, menacing growl and bites down ferociously on it\'s target!'
        return msg

# another child class isntance
class Bacterium(Organism):
    name = 'X'
    species = 'Bacteria'
    legs = 0
    arms = 0
    dna = 'Sequence C'
    origin = 'Mars'

    def replication(self):
        msg = '\nThe cells begin to divide and multiply into two seperate organisms!'
        return msg
        





if __name__ == '__main__':
    # instantiate Human() with the name human
    human = Human()
    # do not need to call self since its already defined within its information
    print(human.information())
    print(human.ingenuity())

    # instantiate Dog() with the name dog
    dog = Dog()
    print(dog.information())
    print(dog.bite())

    # instantiate Bacterium() with the name Bacteria
    bacteria = Bacterium()
    print(bacteria.information())
    print(bacteria.replication())












    
