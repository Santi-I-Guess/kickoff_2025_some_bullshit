from dataclasses import dataclass
from operator import attrgetter
@dataclass
class team:
    team_num: int
    place_num: int
    time: int
    problems_correct: int
    problems_incorrect: int
    problems: list

if __name__ == '__main__':
    test_cases = int(input())
    for test_case_num in range(test_cases):
        num_teams = int(input().split(" ")[0])
        
        teams: list = []

        for team_desc_num in range(num_teams):
            try:
                curr_team = team(0, 0, 0, 0, 0, [int(i) for i in input().split(" ")])
                curr_team.team_num = team_desc_num + 1
                print("Team :", curr_team.team_num)
                curr_team.problems_correct = len(curr_team.problems) - curr_team.problems.count(-1)
                curr_team.problems_incorrect = curr_team.problems.count(-1)
                for time in curr_team.problems:
                    if time != -1:
                        curr_team.time += time
                curr_team.time += curr_team.problems_incorrect * 20
            except:
                pass
        # sort based on problems correct
        sorted_teams = sorted(teams, key=attrgetter('problems_correct'))
        
        place = 1
        for i in sorted_teams:
            i.place_num = place
            place += 1
            print(f"Team: {i.team_num} got Place {i.place_num} | ",end="")
        print()
 
