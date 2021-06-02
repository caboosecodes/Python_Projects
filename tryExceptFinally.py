

def getVar():
    x = input('please input a number: ')
    y = input('please input another number: ')
    return x, y



def addNum():
    go = True
    while go:
        x, y = getVar()
        try:
            z = int(x) + int(y)
            go = False
        except:
            print("an error occured, please be sure to type a number")
        finally:
            print('the function has completed')
    return print('{} + {} = {}'.format(x,y,z))
        

addNum()
