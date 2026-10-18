name = 'Idzi'
print (name + ' hello')

age = 26
AgePlusOne = age + 1
print (f'my age is {AgePlusOne+1}')

names = ('Idzi', 'Szymon', 'Agata')
x, y, z = names
print (y +f' {z}')

value = 'pepe'
x = y = z = value
print (y +f' {z}')



g = 'wow'
g = 1, 2, 3
g = 10

print (f"{g}, {type(g)}")


age = 5
print(age, type(age))

age = 5
print(f"{age} {type(age)}")

def greet():
    print ("Hello world!")

greet()



def add(a, b):
    return a+b

print(add(2,3))




def add (p, i):
    i = 33
    p = 8
    return p+i

result = add (1, 2)
print (result)


p = 9

def add (i):
    i = 5
    return p+i

result = add (3)
print (result)


def add (i):
    i = 5
    return p+i+g

result = add (3)
print (result) 



d = 8


def add (c):
    global d
    d = 0
    return c+d

result = add (3)
print (result) 


def add (i):
    return d+i

result = add (2)
print (result)


def calculate_sum():
    a = 10
    b = 20
    result = a + b
    print(result)
calculate_sum()



result = 0.1 + 0.2
print(result)

print(0.1 + 0.2 == 0.3)


def experiment_1():
    a = 10
    b = 3
    result = a/b
    print(round(result, 2))

experiment_1()


import math

print (math.pi)




def highest_lowest_numer(numbers):
    print(max(numbers))
    print(min(numbers))

highest_lowest_numer((1, 5, 3, 9, 2))

# beautifull code
c = 7.00001
print (c//c+c-1)



def boom():
    return """\tboom\nboom
\"boom\""""
print (boom())


first_name = "John"
last_name = "Doe"
full_name = first_name +" "+ last_name
print(full_name)


def border():
    return  "x" * 20

print (border())

def edge():
    return x + " " * 20 + x

print (edge())


j = (5, 6)
x, y = j
print (f'my age is {x}, my brother age is {y}')