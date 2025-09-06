from dataclasses import dataclass
from itertools import accumulate

'''
    PROBLEM E:

    for case in cases:
        faults := line2.split(" ")
        camp_height = sum(faults[:campnum-1])
        camps_by_height = sort camps on camp height
        return camps_by_height[0], camps_by_height[-1]
'''

@dataclass
class campsite:
    camp_num: int
    height: int

if __name__ == '__main__':
    test_cases = int(input())
    for test_case_num in range(test_cases):
        input() # unneeded
        altitude_changes = [int(i) for i in input().split(" ")]
        altitudes = list(accumulate(altitude_changes))
        the_min = 0
        the_max = 0
        the_min_idx = 1
        the_max_idx = 1
        altitudes = [0] + altitudes
        for idx, i in enumerate(altitudes):
            if idx == 0:
                the_min = i
                the_max = i
                continue
            if i < the_min:
                the_min = i
                the_min_idx = idx + 1
            if i > the_max:
                the_max = i
                the_max_idx = idx + 1
        print(f"{the_min_idx} {the_max_idx}")
