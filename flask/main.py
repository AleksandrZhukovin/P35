def decorator(func):
    def inside():
        print('Hello')
        func()
    inside()


@decorator
def a():
    print('func')
