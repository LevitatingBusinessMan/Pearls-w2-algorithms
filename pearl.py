import util
import sort
import dup

def make_table(pairs):
    #Sort the pairs
    pairs = sort.merge_pairs(pairs)
    # Remove and merge duplicates
    table = dup.merge_dups_pairs(pairs)
    return table

def make_counted_table(pairs):
    #Sort the pairs
    pairs = sort.merge_pairs(pairs)
    table = []
    if len(pairs) != 0:
        fresh = [pairs[0][0], [[pairs[0][1],1]]]
        i = 1
        while i < len(pairs):
            if pairs[i][0] == fresh[0]:
                added = False
                for j in range(len(fresh[1])):
                    filename = fresh[1][j][0]
                    if pairs[i][1] == filename:
                        fresh[1][j][1] += 1
                        added = True
                if not added:
                    fresh[1].append([pairs[i][1],1])
            else:
                fresh[1] = sort.rev_merge_pairs_second(fresh[1])
                table.append(fresh)
                fresh = [pairs[i][0], [[pairs[i][1], 1]]]
            i += 1
        fresh[1] = sort.rev_merge_pairs_second(fresh[1])
        table.append(fresh)
    return table

import os, csv

def make_density_table(pairs):
    #Sort the pairs
    pairs = sort.merge_pairs(pairs)
    table = make_counted_table(pairs)

    files = {}
    for filename in os.listdir("."):
        if filename.endswith(".txt"):
            words = 0
            with open("." + filename, encoding="utf-8") as f:
                for w in csv.reader(f, delimiter=' '):
                    words += 1
                files[filename] = words

    for word in table:
        lexeme = word[0]
        file_occurences = word[1]
        for file in file_occurences:
            filename = file[0]
            file[1] /= files[filename]
        # Sort again
        word[1] = sort.rev_merge_pairs_second(file_occurences)

    return table
