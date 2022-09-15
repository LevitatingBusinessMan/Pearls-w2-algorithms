def linear(data, value):
    """Return the index of 'value' in 'data', or -1 if it does not occur"""
    # Go through the data list from index 0 upwards
    i = len(data)-1
    # continue until value found or index outside valid range
    while i >= 0 and data[i] != value:
        # increase the index to go to the next data value
        i = i - 1
    # test if we have found the value
    if i == -1:
        # no, we went outside valid range; return 'does not occur'
        return 'does not occur'
    else:
        # yes, we found the value; return the index
        return i

#B
# This change will skip the first element when searching

#C
# This change will cause an index out of range error when no match is found

#D
# Reversing the search yields might yield a different result
# if the list contains multiple of the same elements
# ie print(linear([4, 2, 3, 2], 2)) will yield 3 instead of 1
