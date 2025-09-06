from dataclasses import dataclass
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
            solved_problems = [int(i) for i in input().split()]
            rejected_runs   = [int(i) for i in input().split()]
            curr_team.time = sum(i for i in solved_problems if i != -1)
            curr_team.time += 20 * sum(i for i in rejected_runs)
            curr_team.problems_correct = sum(1 for i in solved_problems if i != -1)
            teams.append(curr_team)

        # sort by affluence, give places, sort by team num
        curr_place = 1
        teams.sort(reverse=True, key=lambda x: [x.problems_correct, x.time])
        for idx, curr_team in enumerate(teams):
            teams[idx].place_num = curr_place
            if idx != 0:
                if teams[idx].problems_correct == teams[idx-1].problems_correct and \
                teams[idx].time == teams[idx-1].time:
                    teams[idx].place_num = curr_place
                else:
                    teams[idx].place_num = curr_place + 1
                    curr_place += 1
        teams.sort(key = lambda x: x.team_num)

        # final print
        for i in teams:
            print(f"{i.place_num} ",end="")
        print()
