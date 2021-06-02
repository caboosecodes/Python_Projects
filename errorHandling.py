

def getInfo():
    var1 = input('\nPlease provide the first numeric value: ')
    var2 = input('\nPlease provide the second numeric value: ')
    return var1, var2


def compute():
    go = True
    while go:
        var1, var2 = getInfo()
        try:
            #need change the text to number value; input is always text
            var3 = int(var1) + int(var2)
            go = False
        # as key word creates an alias
        except ValueError as e:
            print('{} \n\nYou did not provide a NUMERIC value!'.format(e))
        except:
            print('\n\nOops, you provided invalid input, program will close now')
        """#after all the previous exceptions have been
        #resolved "finally" will happen no matter what
        finally:
            print('Moving on...')"""
    print('{} + {} = {}'.format(var1, var2, var3))




if __name__ == '__main__':
    compute()

