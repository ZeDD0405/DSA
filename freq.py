#Printing Frequence Of each element in an array/list

n = [1,2,4,5,7,8,5,4,7,3,6,3,7,0,5,8,8]
freq = {}

for i in n:              # i is VALUE
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for key in freq:
    print(key, freq[key])


n = [1,2,4,5,7,8,5,4,7,3,6,3,7,0,5,8,8]
freq = {}
x = len(n)

for i in range(x):       # i is INDEX
    if n[i] in freq:
        freq[n[i]] += 1
    else:
        freq[n[i]] = 1

for key in freq:
    print(key, freq[key])
