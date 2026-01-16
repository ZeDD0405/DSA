#Printing Frequence Of each element in an array/list

n = [1,2,4,5,7,8,5,4,7,3,6,3,7,0,5,8,8]
x=len(n)
freq=dict()
for i in n:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
        
for key in freq:
    print(freq[key])

