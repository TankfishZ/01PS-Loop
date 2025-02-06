n = input()
rev = ""
for me in range(len(n)-1,-1,-1):
    rev = rev + n[me]

print(rev)