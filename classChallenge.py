

# parent class with built in __init__() function
class Comic_characters:
    def __init__(self, characterName, comicName, author):
        self.characterName = characterName
        self.comicName = comicName
        self.author = author

    def string(self):
        msg = 'The character {} from the comic {} written by {}\n'.format(self.characterName, self.comicName, self.author)
        return msg


class Superhero(Comic_characters):
    # keyword pass is when you don't want to add anoy other properties or methods to the class
    '''pass'''
    def __init__(self, characterName, comicName, author, artist, publisher):
        # you can use super() method instead of calling the parent class which will let the child class automatically inherit all the methods and properties from the parent
        Comic_characters.__init__(self, characterName, comicName, author)
        # new properties added to the child class
        self.artist = artist
        self.publisher = publisher

    # polymorphism of the parent class method string()
    def string(self):
        msg = 'The comic {0} is published by {1} and its currently being written by {2}, and drawn by {3}\n'.format(self.comicName, self.publisher, self.author, self.artist)
        return msg


class Foreign_comics(Comic_characters):
    def __init__(self, characterName, comicName, author, artist, origin_country, translated_to):
        Comic_characters.__init__(self, characterName, comicName, author)
        self.artist = artist
        self.origin_country = origin_country
        self.translated = translated_to

    def string(self):
        msg = 'The manga {} published in {} featuring {} as the main character, was written and drawn by {}\n'.format(self.comicName, self.origin_country, self.characterName, self.author)
        return msg





if __name__ == '__main__':
    # creates the object peanut
    peanut = Comic_characters('Charlie Brown', 'Peanuts', 'Charles M. Schulz')
    print(peanut.string())

    #creates the object spiderman
    spiderman = Superhero('Spiderman', 'The Amazing Spiderman', 'Nick Spencer', 'Ryan Ottley', 'Marvel')
    print(spiderman.string())

    #creates the object Berserk
    Berserk = Foreign_comics('Guts', 'Berserk', 'Kentaro Miura', 'Kentaro Miura', 'Japan', 'English')
    print(Berserk.string())






    
