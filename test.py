import util, pearl

pairs = util.word_pairs(["test/grail.txt", "test/brian.txt"])

assert pearl.make_table(pairs) == [
    ['dead', ['test/brian.txt', 'test/grail.txt']],
    ['eunt', ['test/brian.txt']],
    ['spank', ['test/grail.txt']],
]

assert pearl.make_counted_table(pairs) == [
    ['dead', [
        ['test/grail.txt', 3],
        ['test/brian.txt', 1],
    ]],
    ['eunt', [
        ['test/brian.txt', 2],
    ]],
    ['spank', [
        ['test/grail.txt', 7],
    ]],
]

assert pearl.make_density_table(pairs) == [
    ['dead', [
        ['test/brian.txt', 0.3333333333333333],
        ['test/grail.txt', 0.3]
    ]],
    ['eunt', [
        ['test/brian.txt', 0.6666666666666666],
    ]],
    ['spank', [
        ['test/grail.txt', 0.7],
    ]]
]
