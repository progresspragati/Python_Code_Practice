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

