a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# One-line if/else that prints a value:
a = 2
b = 330
print("A") if a > b else print("B")
# A conditional expression (sometimes known as a "ternary operator")

print("")
# You can also use a one-line if/else to choose a value and assign it to a variable:
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200
if b > a:
  pass
# The pass statement is a null operation - nothing happens when it executes. It serves as a placeholder.


