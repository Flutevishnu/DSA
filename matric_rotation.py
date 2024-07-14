matrix1 =[
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

matrix2 =[
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]


def  matrix_multiplication(m1 , m2 ):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            print(m1[i][j]*m2[i][j],'' , end='')
        print()

def transpose(m):

    for i in range(len(m)):
        for j in range(i+1, len(m)):
            m[i][j], m[j][i] = m[j][i], m[i][j]
            # print(m[j][i],'', end='')
    print(m)
# matrix_multiplication(matrix1, matrix2)

# transpose(matrix1)

# for row in zip(*matrix1):
#     print(row)

def array_rotation(ar, n, d):
    temp = []
    i = 0
    while(i<d):
        temp.append(ar[i])
        i = i+1
    print(temp)
    i= 0 
    while(d<n):
        ar[i] = ar[d]
        i += 1
        d += 1
    ar = ar[:i] + temp
    print(ar)



def array_rotate(arr, rotation):
    for i in range(rotation):
        temp = arr[0]
        for j in range(len(arr)-1):
            arr[j] = arr[j+1]
        arr[-1] = temp
        print(arr)
# array_rotate([1, 2, 3, 4, 5, 6, 7], 3)  
def gcd(a, b):
    if b==0:
        return a 
    else: 
        return gcd(b, a%b)

def array_rotate_juggling_algo(arr, d, n):
    for i in range(gcd(n, d)):
        temp = arr[i]
        j = i
        print("i", i)
        print()
        while 1:
            print("j", j)
            k = j + d
            print("k", k)
            if k >= n:
                k = k - n
                print("K-n", k)
            if k == i:
                print("K==i")
                print(k, i)
                break
            arr[j] = arr[k]
            print(arr)
            j = k
        arr[j] = temp
    print(arr)
# array_rotate_juggling_algo([1, 2, 3, 4, 5, 6, 7], 3, 7)

def rotateList(arr, d, n):
    arr = arr[d:n] + arr[:d]
    print(arr)
# rotateList([1, 2, 3, 4, 5, 6, 7], 3, 7)




