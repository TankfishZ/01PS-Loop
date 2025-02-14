n = str(input())
r = ""
for i in range(0,len(n)):
    if n[i] not in r:
        r+=n[i]
        count = 1
        for me in range(i+1,len(n)):
            if n[i] == n[me]:
                count+=1
        print(n[i], "->", count)