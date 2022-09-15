import util
import sort
import dup

def make_table(pairs):
    #Sort the pairs
    pairs = sort.merge_pairs(pairs)
    # Remove and merge duplicates
    table = dup.merge_dups_pairs(pairs)
    return table

make_table(util.all_word_pairs())
