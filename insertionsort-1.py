def insertionSort1(n, arr):
    val = arr[-1]

    for i in range(n-2, -1, -1):

        if arr[i] > val:
            arr[i+1] = arr[i]
            if i==0:
                print(*arr)
                arr[i] = val
        else:
            arr[i+1] = val
            print(*arr)
            break
        print(*arr)
          
n = input().split(' ')
insertionSort1(101  , n)