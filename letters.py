cumle = input("Enter your sentence: ").lower()
harf = {}
for i in cumle:
    if i not in harf:
        harf[i] = 1
    else:
        harf[i] += 1
print(harf)
