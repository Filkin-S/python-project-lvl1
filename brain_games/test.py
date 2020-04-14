import random

step = random.randint(1, 10)
number = random.randint(1, 10)
miss = random.randint(0, 9)
progression, answer = '', ''

print('start = {0}, step = {1}, miss = {2}'.format(number, step, miss))

for counter in range(9):
    if counter == miss:
        answer = str(number)
        progression = '{0}.. '.format(progression)
        number += step
    progression += '{0} '.format(str(number))
    number += step

print(progression)
print(answer)

