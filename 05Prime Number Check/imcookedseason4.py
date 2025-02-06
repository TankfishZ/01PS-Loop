n = int(input(""))
is_prime = True
for i in range (2,n):
    if n % i == 0:
        is_prime = False
        break

if n == 1:
    print("Neither Prime or Composite")
elif is_prime == True:
    print("Prime")
else:
    print("Composite")