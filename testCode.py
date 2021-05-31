

mySentence = 'loves the color'

color_list = ['red','blue','prink','teal','orange','black']

#parameter is defined in the function when its being set up in this case "name"

#create a function using def
# .format() formats this particular string
# {} are wildcards
# mySentence will go into the first {}
# you can use numbers inside the {} to help keep track of them
def color_function(name):
    lst = []
    for i in color_list:
        msg = '{0} {1} {2}'.format(name, mySentence, i)
        lst.append(msg)
    return lst
    
#new code from the next video
def get_name():
    #while go is true it will ask "what is your name?"
    go = True
    while go:
        name = input('what is your name? ')
        #if the name is left blank then it will ask you for your name
        if name == '':
            print('you need to provide the name')
        elif name == 'Sally':
            print('Sally, you may not use this software')
        #once a name is given go is set to False and the rest of the function is executed
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)


#the argument is passed into a function in this case "Daniel"

#lst = color_function('Daniel')
#for i in lst:
    #print(i)

get_name()

