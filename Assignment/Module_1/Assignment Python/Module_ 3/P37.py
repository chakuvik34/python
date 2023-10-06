from itertools import product

data = {'1': ['a', 'b'], '2': ['c', 'd']}

combinations = list(product(*data.values()))

combinations_as_strings = [''.join(combination) for combination in combinations]

print(' '.join(combinations_as_strings))
