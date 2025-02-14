a= int(input())
b= int(input())
c= int(input())

if a==b==c:
    print('eq')
elif a==b or b==c or a==c:
    print('is')
else:
    print("sc")