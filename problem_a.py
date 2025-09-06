
if __name__ == '__main__':
    test_cases = int(input())
    for test_case_num in range(test_cases):
        list_len = int(input())
        blackboard = [int(i) for i in input().split()]
        questions = [input() for i in range(list_len)]
        blackboard.sort()
        for i in questions:
            if i == "max":
                the_max = blackboard[-1]
                print(the_max, end=" ")
                blackboard.pop()
            elif i == "min":
                the_min = blackboard[0]
                print(the_min, end=" ")
                blackboard.pop(0)
        print()

