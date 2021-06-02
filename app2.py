

import app


def print_app2():
    name = (__name__)
    return name

#the "__name__" is the name of the "app" (the file called "app")
# '__main__' is the script that is being run so this script that's being run is
# __main__

# if the conditional is true then run the code if not, do not run the code
if __name__ == '__main__':
    #the following is calling code from within the script
    print('I am running code form {}'.format(print_app2()))

    #the following is calling code from the imported app.py
    #app.print_app() calls on the module "app" and then that module's method print_app
    print('I am running code form {}'.format(app.print_app()))
