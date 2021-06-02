
#considered global
name = 'Python'

def getName():
    #local variable, the function will use this over the local variable
    name = 'C#'
    print('I am coding with {}'.format(name))



getName()
