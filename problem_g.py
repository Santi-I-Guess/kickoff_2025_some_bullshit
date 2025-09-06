
if __name__ == '__main__':
    towns = {} # name, mile
    towns_rev = {} # mile, name
    num_towns, num_questions = [int(i) for i in input().split()]
    for i in range(num_towns):
        town_name, mile_marker = input().split()
        towns.update({town_name:int(mile_marker)})
        towns_rev.update({int(mile_marker):town_name})
    for i in range(num_questions):
        question_type, question_input = input().split()
        if question_type == "1":
            print(towns_rev[int(question_input)])
        elif question_type == "2":
            print(towns[question_input])

