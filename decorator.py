def myDecorator(func):
    def wrapper():
        print("First called of function")
        func()
        print("Second arguments function is called")
    return wrapper

@myDecorator
def say_hello():
    print("Hello")

say_hello()


def auth_and_login(func):
    def wrapper():
        print("Checking authentication")
        func()
    
    return wrapper

@auth_and_login
def login():
    print("User Logged in")

login()

def logout():
    print("USer logout")

logout()