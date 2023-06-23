import random


def say_hello(name):
    print(f"Hello {name}")


say_hello("Abybakar")
say_hello("Abybakar")
say_hello("Abybakar")
say_hello("Abybakar")
say_hello("Abybakar")

def square_area(a):
    r=a*a
    print(r)

square_area(7)

def lottery():
    tickets= [30,79,84]
    ticket=random.choice(tickets)
    return ticket
r=lottery()
print(r)

def multi_lottery():
    tickets = [30,79,84]
    ticket=random.choice(tickets)
    tickets.remove(ticket)
    ticket2=random.choice(tickets)
    return ticket,ticket2
r,r2=multi_lottery()
print(r,r2)

def factorial(n):
    r=1
    for i in range(1,n+1):
        r*=i
    return r
print(factorial(5))

mult = lambda a,b: a*b
print(mult(8,2))

