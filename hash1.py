#for fixed size of input numbers from 1 to 10
n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10,1]
m = [10, 11, 1, 9, 5, 67, 2]

hash_list=[0]*11
for num in n:
    hash_list[num]+=1
for num in m:
    if num < 1 or num > 10:
        print ("0")
    else:
        print(hash_list[num])

#for variable size of input numbers
n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 11, 1, 9, 5, 67, 2]
hash={}
for i in n:
    if i in hash:
        hash[i]+=1
    else:
        hash[i]=1
for i in m:
    if i in hash:
        print(hash[i])
    else:
        print("0")