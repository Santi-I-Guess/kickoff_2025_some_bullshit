
def neighbors(point: list) -> list:
    neighs = [
        [point[0] + 1, point[1]],
        [point[0] - 1, point[1]],
        [point[0], point[1] + 1],
        [point[0], point[1] - 1]
    ]
    return neighs

if __name__ == '__main__':
    test_cases = int(input())
    square_coords = {}
    for test_case_num in range(test_cases):
        curr_coord = [int(i) for i in input().split()]
        square_coords.update({str(curr_coord):1})
 

    perimeter = 0
    for curr_node in square_coords.keys():
        perimeter += 4
        curr_node_list = [int(i) for i in curr_node.strip("[]").split(",")]
        for neigh_node in neighbors(curr_node_list):
            try:
                square_coords[str(neigh_node)]
                perimeter -= 1
            except KeyError:
                pass
    print(perimeter)
