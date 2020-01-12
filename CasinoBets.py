"""
When John gambles at the casino bets in one of the 2 ways in each game:
1. 1 chip
2. all in
wins are paid equal to the wager so if he bets c chips and he wins he take 2*c back, if he loses he take 0 back

yesterday he won all the games starting with 1 chip and left with N chips and he played all-in no more than K times. calculate the smallest possible number of rounds that he could have played.

c = 1 is never considered as all in

write a function that given N and K returns the minimum number of rounds that he needs to leave the casino

for n = 8 kai k = 0 the answer is 7
n = k =10 the answer is 4
n = 18 k = 2  the answer is 6

k in [0,100], n in [1, 2.345.234.234]

"""
import math
def solution(N,k):
    total = 1
    if N <= 1:
        return 0
    p = math.ceil(math.log(N)/float(math.log(2)) )
    if p<=k:
        return p


    total = math.ceil(N/float(2**k)) 
    rounds = k
    while total>1:
        rounds = rounds + 1
        total = total -1
    return rounds
