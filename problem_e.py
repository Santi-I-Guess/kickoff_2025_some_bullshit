'''
    PROBLEM E:

    for case in cases:
        faults := line2.split(" ")
        camp_height = sum(faults[:campnum-1])
        camps_by_height = sort camps on camp height
        return camps_by_height[0], camps_by_height[-1]
'''
if __name__ == '__main__':
    test_cases = int(input())
    for test_case_num in range(test_cases):
        input()
        altitudes = input().split(" ")
        print(*altitudes)
        campsite.height = sum(altitudes[:campsite_num-1])

