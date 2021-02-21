def my_decoraror(func):

    def wrapper():
        print('before')
        func()

    return wrapper

def hi():
    print('Hi')

hi=my_decoraror(hi)
hi()