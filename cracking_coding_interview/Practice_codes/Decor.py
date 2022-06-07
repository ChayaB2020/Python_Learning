#This file will define decorators
def new_func(func):
    print("This is inside new_func")
    def my_func():
        print("inside my_func")
        func()
        print("End of my_func")
    return my_func

def another_func(func):
    print("This is inside another_fun")
    def inner():
        print("thi is inside inner function")
        func()
        print("end of inner function")
    print("This is end of another_fun")
    return inner


@another_func
@new_func
def decor_fun():
    print("This is decor func")

decor_fun()