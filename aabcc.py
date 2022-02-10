# Take  Input as aaabbccc
# the output is 3a2b3c

s = input("Enter the word :  ")
counts = 1
strg = len(s) - 1
finalword = ""
for i in range(strg):
    if s[i] == s[i+1]:
        counts += 1

    elif s[i] != s[i+1] and s[i+1] != "":
        finalword = finalword + str(counts) + s[i]
        counts = 1

finalword = finalword + str(counts) + s[i]
print(finalword)
