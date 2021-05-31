def name():
    go = True
    while go:
        x = input('what is your name? ')
        if x == '':
            print('a name is needed ')
        else:
            go = False
    print('hello ' + x)
        
name()
