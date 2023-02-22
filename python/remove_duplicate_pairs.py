import numpy

from typing import Sequence, List, Tuple

def remove_duplicate_pairs(A: Sequence, B: Sequence) -> Tuple[List, List]:

    A_and_B = [(a, b) for a, b in zip(A, B)]
    unique_A_and_B = set(A_and_B)

    if len(unique_A_and_B) == len(A_and_B):
        # A and B are unique pairs, nothing to do
        return A, B

    # use unique A and B indexes to create a boolean mask
    unique_idx = [A_and_B.index(pair) for pair in unique_A_and_B]
    is_unique_mask = numpy.full(len(A_and_B), False)
    is_unique_mask[unique_idx] = True 

    return list(numpy.array(A)[is_unique_mask]), list(numpy.array(B)[is_unique_mask])


