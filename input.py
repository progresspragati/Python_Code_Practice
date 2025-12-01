import math
print("Enter Your Name:-")
x = input()
print(f"Name:-{x}")

x = input("Enter a number:")

#find the square root of the number:
y = math.sqrt(float(x))
print(f"The square root of {x} is {y}")
y = True

while y == True:
  x = input("Enter a number:")
  try:
    x = float(x);
    y = False
  except:
    print("Wrong input, please try again.")
print("Thank you!")