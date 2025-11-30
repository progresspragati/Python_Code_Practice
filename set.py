thisset = {"apple", "banana", "cherry", "banana"}
thisset = {"apple", "banana", "cherry", True, 1, 2}
thisset.add("orange")

print(len(thisset))
print(thisset)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set2.add(6)

set3 = set1.union(set2)
print(set3)
fset = frozenset({"apple", "banana", "cherry"})
print(fset)
print(type(fset))

# You cannot access items in a set by referring to an index or a key.

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# You can use the | operator instead of the union() method, and you will get the same result.
#  The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)
print("")

# You can use the - operator instead of the difference() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)
# Note: The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.

# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)
# Note: The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.






