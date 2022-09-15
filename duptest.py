from dup import remove_dups
from util import lines

print(f"grail.txt: {len(remove_dups(lines('grail.txt')))}")
print(f"hacktest.txt: {len(remove_dups(lines('hacktest.txt')))}")
