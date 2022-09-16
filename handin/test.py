import util, pearl

pairs = util.word_pairs(["tgrail.txt", "tbrian.txt"])

assert pearl.make_table(pairs) == [
    ['dead', ['tbrian.txt', 'tgrail.txt']],
    ['eunt', ['tbrian.txt']],
    ['spank', ['tgrail.txt']],
]

assert pearl.make_counted_table(pairs) == [
    ['dead', [
        ['tgrail.txt', 3],
        ['tbrian.txt', 1],
    ]],
    ['eunt', [
        ['tbrian.txt', 2],
    ]],
    ['spank', [
        ['tgrail.txt', 7],
    ]],
]

assert pearl.make_density_table(pairs) == [
    ['dead', [
        ['tbrian.txt', 0.3333333333333333],
        ['tgrail.txt', 0.3]
    ]],
    ['eunt', [
        ['tbrian.txt', 0.6666666666666666],
    ]],
    ['spank', [
        ['tgrail.txt', 0.7],
    ]]
]
