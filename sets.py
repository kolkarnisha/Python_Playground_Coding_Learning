set={1,2,3,4,4,5,5,6,7,6,6,7}
print(set)
#{1,2,3,4,5,6,7} .....removes duplicates
set.add(10)
print(set)
set.update([8,9])
print(set)
set.remove(10)
set.discard("nisha")#no error if missing
set.pop()  #sets are unordered so a random element removed
print(1 in set)
set.clear()
set1={21,22,23,23,21,24}
print(set|set1)
print(set&set1)
print(set.intersection(set1))
print(set-set1)
