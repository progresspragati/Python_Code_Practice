def my_function():
  print("Hello from a function")

my_function()

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")

def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)

def my_function(*, name):
  print("Hello", name)
my_function(name = "Emil")

def my_function(*kids):
  print("The youngest child is " + kids[1])
my_function("Emil", "Tobias", "Linus")

def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)
my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

# Using * to unpack a list into arguments:
def my_function(a, b, c):
  return a + b + c
numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

# Using ** to unpack a dictionary into keyword arguments:
def my_function(fname, lname):
  print("Hello", fname, lname)
person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")

# Understanding the LEGB rule:
x = "global"
def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)
outer()
print("Global:", x)

def changecase(func):
  def myinner():
    return func().upper()
  return myinner
@changecase
def myfunction():
  return "Hello Sally"
print(myfunction())

def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase
@changecase(1)
def myfunction():
  return "Hello Linus"
print(myfunction())

def changecase(func):
  def myinner():
    return func().upper()
  return myinner
def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner
@changecase
@addgreeting
def myfunction():
  return "Tobias"
print(myfunction())

x = lambda a : a + 10
print(x(5))
x = lambda a, b : a * b
print(x(5, 6))

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)
countdown(5)

# Find the maximum value in a list:
def find_max(numbers):
  if len(numbers) == 1:
    return numbers[0]
  else:
    max_of_rest = find_max(numbers[1:])
    return numbers[0] if numbers[0] > max_of_rest else max_of_rest
my_list = [3, 7, 2, 9, 1]
print(find_max(my_list))

import sys
print(sys.getrecursionlimit())

import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

def my_generator():
  yield 1
  yield 2
  yield 3
for value in my_generator():
  print(value)

print("")
def large_sequence(n):
  for i in range(n):
    yield i
# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

# List comprehension - creates a list
list_comp = [x * x for x in range(5)]
print(list_comp)
# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))

# Calculate sum of squares without creating a list
total = sum(x * x for x in range(10))
print(total)

print("")
def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b
# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(3):
  print(next(gen))


def main():
  speak()
  repeat()

def speak():
  print("i am speaking")
def repeat():
    print("I am repeating")
main()