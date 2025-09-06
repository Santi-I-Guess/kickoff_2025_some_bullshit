
if __name__ == '__main__':
    test_cases = int(input())
    for test_case_num in range(test_cases):
        size_cube = int(input())
        corner = 8
        center = 6 * ((size_cube - 2)**2)
        edge = 12 * (size_cube - 2)
        print(f"{corner} {edge} {center}")
