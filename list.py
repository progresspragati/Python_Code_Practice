thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist[1] = "blackcurrant"
print(thislist)
print(len(thislist))
list1 = ["abc", 34, True, 40, "male"]
print(list1)
print(type(list1))
thislist = list(("apple", "anjeer", "cherry")) # note the double round-brackets
print(thislist)
print(thislist[1])
print(thislist[-1])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[3:])
print(thislist[-4:-1])
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
thislist[1:2] = ["blackcurrant", "strawberry"]
print(thislist)
thislist[1:5] = ["coconut"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
thislist.append("orange")
print(thislist)
thislist.insert(1, "coconut")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# If there are more than one item with the specified value, the remove() method removes the first occurrence:
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist

# The clear() method empties the list. The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Print all items by referring to their index number:
for i in range(len(thislist)):
  print(thislist[i])

print("")
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# A short hand for loop that will print all items in a list:
print("")
[print(x) for x in thislist]

print("")
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

print("")
newlist = [x for x in fruits if "a" in x]
print(newlist)

print("")
newlist = [x for x in fruits if x != "apple"]
print(newlist)
print(newlist)

print("")
# can use the range() function to create an iterable:
newlist = [x for x in range(10)]
print(newlist)
newlist = [x for x in range(10) if x < 5]
print(newlist)
newlist = [x.upper() for x in fruits]
print(newlist)

# Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
newlist = ["orange", "mango", "kiwi", "pineapple", "banana"]
newlist.sort()
print(newlist)

# Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]
print(newlist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# To sort descending, use the keyword argument reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# You can also customize your own function by using the keyword argument key = function.
# Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Reverse the order of the list items:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

print("")
# Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# You can also make a copy of a list by using the : (slice) operator.
yourlist = thislist[:]
print(yourlist)

print("")
# Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:
list1 = ["a", "d" , "c"]
list2 = [1, 2, 4]
for x in list2:
  list1.append(x)
print(list1)

# Use the extend() method to add list2 at the end of list1:
list1 = ["a", "s" , "c"]
list2 = [1, 2, 8]
list1.extend(list2)
print(list1)
