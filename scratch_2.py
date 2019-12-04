#guess the number
import random
x=random.randint(1,18)
y=0
for y in range(18):
    y = input('your guess\n')
    if int(y) > 18:
        print('u exceed limit, guess inside 18 only')
        break
    if int(y) > x:
        print('the number is smaller ')
    elif int(y) < x:
        print('the number is greater than the last one')
    else:
        print('congrats u guessed correct', y, 'is the correct answer')
        break
