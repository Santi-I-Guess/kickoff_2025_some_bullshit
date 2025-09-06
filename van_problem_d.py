from dataclasses import dataclass
from operator import attrgetter
@dataclass
class team:
    team_num: int
    place_num: int
    time: int

if __name__ == '__main__':
    test_cases = int(input())
    for test_case_num in range(test_cases):
        try:
            num_teams = int(input().split(" ")[0])
        except:
            break
        
        teams: list = []

        for index in range(num_teams):
                team_num = index + 1
                try:
                    problems = [int(i) for i in input().split(" ")]
                except EOFError:
                    problems = []
                    pass
                time = 0
                problems_correct = len(problems) - problems.count(-1)
                problems_incorrect = problems.count(-1)
                for time in problems:
                    if time != -1:
                        time += time
                time += problems_incorrect * 20

                new_team = team(team_num, 0, time)
        # sort based on problems correct
        sorted_teams = sorted(teams, key=attrgetter('problems_correct'))
        
        place = 1
        for i in sorted_teams:
            i.place_num = place
            place += 1
            print(f"Team: {i.team_num} got Place {i.place_num} | ",end="")
        print()
 
