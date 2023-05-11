
### List of Comprehensions with conditions

team_name = ['team1', 'team2', 'team3', 'team4' ,'team5' ,'team6' ,'team7']
print([x + ' VS ' + y for x in team_name for y in team_name if x != y])