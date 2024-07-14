def countarr(n):
    count = 0 
    for i in range(len(n)):
        if n[i]==0 and n[i+1]==1:
            count+=1
    print(count)

countarr([0, 1, 0, 0, 1, 1])