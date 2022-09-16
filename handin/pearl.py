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
        # This fresh value accumulates all occurences of the current word
        # and is replaced ones this parser reaches a different word
        fresh = [pairs[0][0], [[pairs[0][1],1]]]
        i = 1
        while i < len(pairs):
            # If the word has changed
            # If not we have to count the occurence
            if pairs[i][0] == fresh[0]:
                added = False
                # A loop to find the right filename to increment
                for j in range(len(fresh[1])):
                    filename = fresh[1][j][0]
                    # Filename is found
                    if pairs[i][1] == filename:
                        fresh[1][j][1] += 1
                        added = True
                # If the occurence wasn't added in the line before,
                # the filename is new and has to be appended
                if not added:
                    fresh[1].append([pairs[i][1],1])
            else:
                # Sort the list before appending it to the table
                fresh[1] = sort.rev_merge_pairs_second(fresh[1])
                table.append(fresh)
                # Create the next fresh value
                fresh = [pairs[i][0], [[pairs[i][1], 1]]]
            i += 1
        # Append last value
        fresh[1] = sort.rev_merge_pairs_second(fresh[1])
        table.append(fresh)
    return table

import os, csv

def make_density_table(pairs):
    #Sort the pairs
    pairs = sort.merge_pairs(pairs)
    table = make_counted_table(pairs)

    files = {}
    # Count the words in each file mentioned in the pairs
    for word in table:
        file_occurences = word[1]
        for file in file_occurences:
            filename = file[0]
            if filename not in files:
                with open(filename, encoding="utf-8") as f:
                    words = 0
                    for w in csv.reader(f, delimiter=' '):
                        words += 1
                    files[filename] = words

    # Calculate densities
    for word in table:
        lexeme = word[0]
        file_occurences = word[1]
        for file in file_occurences:
            filename = file[0]
            file[1] /= files[filename]
        # Sort again
        word[1] = sort.rev_merge_pairs_second(file_occurences)

    return table
