#global scope
x = 90

def foo():
    #local x - no relation to global x
    x = 10

    def visit():
        nonlocal x
        x = 100 * 100
        print(x)

    visit()
    print(x)


foo()
print(x)


