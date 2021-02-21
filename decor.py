def my_decoraror(func):

    def wrapper():
        print('before')
        func()

    return wrapper
@my_decoraror
def hi():
    print('Hi')

# hi=my_decoraror(hi)
hi()
