import random


hashes['#' , '-']

randomSet = ['#'] * 31

count = 0
while count < 15:
    ra = random.randint(1, 29)
    if( randomSet[ra] == '-' ):
        continue
    count += 1
    randomSet[ra] = '-'

print "".join(randomSet)
