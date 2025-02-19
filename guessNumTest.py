# using library to import random

import random

# assign a target num and guess num
# used a two values to two variable in one line, random.randint => to target_num and 0 => guess_num
target_num, guess_num = random.randint(1, 5), 0 

# start a while loop until ENTER the guess number
while target_num != guess_num:
    guess_num = int(input('Guess the numb: '))

print('Well Guessed !')