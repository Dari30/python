def f():
    global a
    a = 3
    f2()
def f2():
    print(a)
a=5
f()
