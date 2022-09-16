def remove_dups(data):
    res = []
    if len(data) != 0:
        fresh = data[0]
        i = 1
        while i < len(data):
            if data[i] != fresh:
                res.append(fresh)
                fresh = data[i]
            i += 1
        res.append(fresh)
    return res

def merge_dups_pairs(data):
    res = []
    if len(data) != 0:
        # The current word, which we will accumulate the file occurences for
        fresh = [data[0][0], [data[0][1]]]
        i = 1
        while i < len(data):
            # Same word
            if data[i][0] == fresh[0]:
                # Add the filename if it wasn't there before
                if data[i][1] not in fresh[1]:
                    fresh[1].append(data[i][1])
            else:
                res.append(fresh)
                fresh = [data[i][0], [data[i][1]]]
            i += 1
        res.append(fresh)
    return res
