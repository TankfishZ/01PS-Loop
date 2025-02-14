n = input()
alpha_lower = 'abcdefghijklmnopqrstuvwxyz'
alpha_upper =  alpha_lower.upper()
encode = ""

for i in range(0,len(n)):
    if n[i] in alpha_lower:
        for j in range(0, len(alpha_lower)):
            if n[i] == alpha_lower[j]:
                pos = j
                encode += alpha_lower[(pos+13)%26]
                break
    elif n[i] in alpha_upper:
        for j in range(0, len(alpha_upper)):
            if n[i] == alpha_upper[j]:
                pos = j
                encode += alpha_upper[(pos+13)%26]
                break
    else:
        encode += n[i]
print(encode)