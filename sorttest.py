from sort import bubble,merge,merge_pairs
from util import lines

print('bubble([2,5,1,6,2,8,4,2])')
print(bubble([2,5,1,6,2,8,4,2]))

print('merge([2,5,1,6,2,8,4,2])')
print(merge([2,5,1,6,2,8,4,2,3]))

import time
start = time.process_time()
bubble(lines("Unabr.dict"))
end = time.process_time()
print(f"Time bubble with Unabr.dict: {round((end-start) * 10**6)}ms")

start = time.process_time()
merge(lines("Unabr.dict"))
end = time.process_time()
print(f"Time merge with Unabr.dict: {round((end-start) * 10**6)}ms")

start = time.process_time()
bubble(lines("hacktest.txt"))
end = time.process_time()
print(f"Time bubble with hacktest.txt: {round((end-start) * 10**6)}ms")

start = time.process_time()
merge(lines("hacktest.txt"))
end = time.process_time()
print(f"Time merge with hacktest.txt: {round((end-start) * 10**6)}ms")

print('merge([["a",3],["a",2],["b",1],["ab",10]])')
print(merge([["a",3],["a",2],["b",1],["ab",10]]))

print('merge_pairs([["a",3],["a",2],["b",1],["ab",10]])')
print(merge_pairs([["a",3],["a",2],["b",1],["ab",10]]))
