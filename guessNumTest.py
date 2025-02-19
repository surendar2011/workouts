# using library to import random

import random

# assign a target num and guess num
target_num, guess_num = random.randint(1, 5), 0 

# start a while loop until ENTER the guess number
while target_num != guess_num:
    guess_num = int(input('Guess the numb: '))

print('Well Guessed !')