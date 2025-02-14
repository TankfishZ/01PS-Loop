n = int(input())
summ = 0
summ1 = 0
while n>0:
    summ+=n%10
    n//= 10
    if (n == 0 and summ >= 10):
        n = summ
        summ = 0
print(summ)
