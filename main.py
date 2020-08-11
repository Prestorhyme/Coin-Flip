import random

coin = [0, 1]

if random.choice(coin) == 0:
    print('heads')
else:
    print('tails')