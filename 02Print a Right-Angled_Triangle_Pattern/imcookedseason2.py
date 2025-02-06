n = int(input())
for me in range (1,n+1):
    for you in range (1,me+1):
        print(you % 10 , end = "")
    print()