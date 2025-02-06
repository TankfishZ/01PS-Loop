n1 = int(input(""))
n2 = int(input(""))
m = 0
if n1 < n2:
    m = n1
else:
    m = n2

while (n1%m!=0 or n2%m!=0):
    m = m-1
print(m)