from ordsearch import linear

print('linear([2,3,3,4], 3)')
print(linear([2,3,3,4], 3))

print('linear([2,3,6,7], 5)')
print(linear([2,3,6,7], 5))

# These will complain that a comparison
# can't be made between a string and an int
#print(linear([1,2],"foo"))
#print(linear(["bar","foo"],2))

from ordsearch import binary
print('binary([2,3,3,4,6,7,9],7)')
print(binary([2,3,3,4,6,7,9],7))

print('binary([2,3,3,4,6,7,9],5)')
print(binary([2,3,3,4,6,7,9],5))

#low: 63 high: 63 mid: 62
print('print(binary(range(200),62))')
print(binary(range(200),62))

from ordsearch import binary_pairs
x = [["Anne",7],["John",5],["Pete",9]]

print('binary_pairs(x,"Brenda")')
print(binary_pairs(x,"Brenda"))

print('binary_pairs(x,"John")')
print(binary_pairs(x,"John"))
