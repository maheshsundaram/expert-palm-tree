import pprint
from itertools import combinations, chain, permutations
import random

expected = ["team", "role", "user", "group", "distributionList", "forum"]

# Cases that should pass
all_correct_combinations = list(
    chain(*map(lambda x: combinations(expected, x), range(1, len(expected) + 1)))
)

def is_correct_order(permutation):
    indexes = [expected.index(item) for item in permutation]
    return indexes == sorted(indexes)


all_unique_permutations: set[tuple[str, ...]] = set()

for r in range(1, len(expected) + 1):
    for combination in combinations(expected, r):
        for permutation in permutations(combination, r):
            all_unique_permutations.add(permutation)

# Cases that should fail
all_incorrect_combinations = [
    permutation
    for permutation in all_unique_permutations
    if not is_correct_order(permutation)
]

sample = random.sample(all_incorrect_combinations, 30)

pprint.pprint(sample)
