from dataclasses import dataclass
from operator import attrgetter
import pdb

@dataclass
class team:
    team_num: int
    place_num: int
    time: int
    problems_correct: int

if __name__ == '__main__':
    test_cases = int(input())
    for test_case_num in range(test_cases):
        num_teams, num_problems = [int(i) for i in input().split()]
        
        teams: list = []

        # lines 1 and 2 per team
        for team_desc_num in range(num_teams):
            curr_team = team(0, 0, 0, 0)
            curr_team.team_num = team_desc_num + 1

            solved_problems = [int(i) for i in input().split() if i != -1]
            rejected_runs   = [int(i) for i in input().split() if i == -1]

            curr_team.time = sum(i for i in solved_problems if i != -1)
            curr_team.time += 20 * sum(i for i in rejected_runs)

            curr_team.problems_correct = sum(1 for i in solved_problems if i != -1)
            teams.append(curr_team)


        curr_place = 1
        sorted_teams = sorted(teams, key=attrgetter('problems_correct'))
        for curr_team in sorted_teams:
            curr_team.place_num = curr_place
            curr_place += 1
        # final print
        for i in teams:
            print(f"{i.place_num} ",end="")
        print()
 
