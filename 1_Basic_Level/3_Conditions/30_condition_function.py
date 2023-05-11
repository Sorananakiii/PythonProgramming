
# Conditionals 
# if function will do the next line if condition is True 

def test_high_score(player_score, high_score):
    if player_score > high_score:   #Similarly for a conditional, we have an if statement ending with :
        print('High score!')
        high_score = player_score

    return high_score

print(test_high_score(95, 93))
print(test_high_score(83, 98))