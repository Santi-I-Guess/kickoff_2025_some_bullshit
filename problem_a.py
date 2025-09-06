
if __name__ == '__main__':
    test_cases = int(input())
    for test_case_num in range(test_cases):
        list_len = int(input())
        blackboard = [int(i) for i in input().split()]
        questions = [input() for i in range(list_len)]
        for i in questions:
            if i == "max":
                print(max(blackboard), end=" ")
                blackboard.pop(blackboard.index(max(blackboard)))
            elif i == "min":
                print(min(blackboard), end=" ")
                blackboard.pop(blackboard.index(min(blackboard)))
        print()

