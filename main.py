from set import Set

print("Set A")
set_a = Set()

# insert elements
set_a.insert(1)
set_a.insert(2)
set_a.insert(3)
set_a.insert(4)
set_a.insert(5)

# 1 2 3 4 5 
set_a.print()

print("\n\nRemove element 2")

set_a.remove(3)

# 1 2 4 5 
set_a.print()

print("\n\n--------------------------------\n")

print("Set B")
set_b = Set()

set_b.insert(6)
set_b.insert(7)
set_b.insert(8)
set_b.insert(9)
set_b.insert(10)

# 6 7 8 9 10
set_b.print()

print("\n\nMerge Set A with Set B")

# 1 2 4 5 6 7 8 9 10 
union_set = set_a.union(set_b)
union_set.print()

print("\n\n--------------------------------\n")

print("Set C")
set_c = Set()

set_c.insert(3)
set_c.insert(4)
set_c.insert(5)

# 3 4 5
set_c.print()

print("\n\nIntersection Set A with Set C")

# 4 5
intersection_set = set_a.intersection(set_c)
intersection_set.print()



print("\nDifference Set A with Set C")

# 4 5
intersection_set = set_a.difference(set_c)
intersection_set.print()