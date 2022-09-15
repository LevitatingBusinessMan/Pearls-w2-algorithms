def bubble(data):
    res = data[:]
    ui = len(res)-1
    while ui > 0:
        si = 0
        i = 0
        while i < ui:
            if res[i] > res[i+1]:
                foo = res[i]
                res[i] = res[i+1]
                res[i+1] = foo
                si = i
            i += 1
        ui = si
    return res

def merge(data):
    if len(data) <= 1:
        return data
    else:
        mid = len(data)//2
        fst = merge(data[:mid])
        snd = merge(data[mid:])
        res = []
        fi = si = 0
        while fi < len(fst) and si < len(snd):
            if fst[fi] < snd[si]:
                res.append(fst[fi])
                fi += 1
            else:
                res.append(snd[si])
                si += 1
        if fi < len(fst):
            res.extend(fst[fi:])
        elif si < len(snd):
            res.extend(snd[si:])
        return res

def merge_pairs(data):
    if len(data) <= 1:
        return data
    else:
        mid = len(data)//2
        fst = merge(data[:mid])
        snd = merge(data[mid:])
        res = []
        fi = si = 0
        while fi < len(fst) and si < len(snd):
            if fst[fi] < snd[si]:
                res.append(fst[fi])
                fi += 1
            else:
                res.append(snd[si])
                si += 1
        if fi < len(fst):
            res.extend(fst[fi:])
        elif si < len(snd):
            res.extend(snd[si:])
        return res    
