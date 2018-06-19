#! python 3
# Written by - Kevin Rose
# Project Euler
# Problem 1
# Multiples of 3 and 5

multiples = []
length = 1000

for x in range(1, length):
    if x % 3 == 0 or x % 5 == 0:
        multiples.append(x)

print(multiples)
print(sum(multiples))
