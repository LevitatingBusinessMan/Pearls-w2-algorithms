def linear(data, value):
    """Return the index of 'value' in 'data', or -1 if it does not occur"""
    # Go through the data list from index 0 upwards
    i = 0
    # continue until value found or index outside valid range
    while i < len(data) and data[i] != value:
        # assuming a sorted list, we know the value isn't in the list
        # if a larger value is encountered
        if data[i] > value:
            return -1
        # increase the index to go to the next data value
        i = i + 1
    # test if we have found the value
    if i == len(data):
        # no, we went outside valid range; return -1
        return -1
    else:
        # yes, we found the value; return the index
        return i

def binary(data,value):
    low = 0
    high = len(data)-1
    mid = high//2
    while low <= high and data[mid] != value:
        mid = (low+high)//2
        if value < data[mid]:
            high = mid -1
        else:
            low = mid + 1
    #print(f"low: {low} high: {high} mid: {mid}")
    return mid if data[mid] == value else -1

def binary_pairs(data,value):
    low = 0
    high = len(data)-1
    mid = high//2
    while low <= high and data[mid][0] != value:
        mid = (low+high)//2
        if value < data[mid][0]:
            high = mid -1
        else:
            low = mid + 1
    #print(f"low: {low} high: {high} mid: {mid}")
    return mid if data[mid][0] == value else -1
