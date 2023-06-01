# ===============================================================================================================
# Add the first 3 letters after the computer chose a word from the list. Hidden letters should be replaced with hyphens ("-")
import random

VOCAB = ['python', 'java', 'kotlin', 'javascript']
hang = random.choice(VOCAB)
print('--------------- H A N G M A N ---------------')
# ===============================================================================================================

word = input('Guess the word {}{}:'.format(hang[:3], '-' * (len(hang) - 3)))
if word == hang:
    print('You survived!')
else:
    print('You are hanged!')



# ===============================================================================================================
