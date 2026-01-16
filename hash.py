#for char searching frequencey

s = "azyzyzaaaa"
q = ['a', 'a', 'y', 'z']
hash={}
for i in s:
    asci = ord(i)
    index=asci - 97
    if index in hash:
        hash[index]+=1
    else:
        hash[index]=1

for ch in q:
    asc = ord(ch)
    ind = asc -97
    if ind in hash:
        print(hash[ind])