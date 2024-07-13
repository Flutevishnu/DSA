def primenumber(n):

    if(n<2):
        return 1
    for i in range(2, (n//2)+1): #2, 6

        if(n%i==0):
            return "It is not a prime number"
    else:
        return "it is prime number "


def perfect_number(n):
    '''
    description: 
        checks whether the number is perfect number or not 

    input: takes the integer n

    process: take a for loop in  range half of the intfeger and checks whether the i is a proper divisor of n if it is then  i add it to  initialized variable 

    output: output-type - return ( perfect or not perfect) 

    '''

    pn = 0
    for i in range(1, (n//2)+1):
        if n%i==0:
            pn += i
    if pn==n:
        return "perfect number"
    else: 
        return "Not a perfect number"


def harshad_number(n):
    '''
    description: 
        checks whether the number is harshad_number or not 

    input: takes the integer n

    process: use while loop wih  a condition  and take the each number from the input and add it . 

    output: output-type - return ( harshad- not harshad) 

    '''
    temp1 = 0
    temp2 = n
    while(n>0):
        temp1 += n %10 
        n //= 10
    
    if temp2%temp1==0:
        return "harshad number"
    else:
        return "not harshad number"


def abundance_number(n):
    '''
    description: 
        checks whether the number is abundance_number or not 

    input: takes the integer n

    process: take a for loop in  range half of the intfeger and checks whether the i is a proper divisor of n if it is then  i add it to  initialized variable  and then if the sum of the proper divsiors greator the the input it is abundant

    output: output-type - return ( it is abundace number and the number is- it is abundace number and the number is) 

    '''
    pn = 0
    for i in range(1, (n//2)+1):
        if n%i==0:
            pn += i
    if pn>n:
        return "it is abundace number and the number is : ", pn-n
    else: 
        return "it is abundace number and the number is"

def automorphic_number(n):
    '''
    description: checks whether the number is automorphic or not

    input: integer

    precess: 
        takes the last number form the sqaure of the input and the origianl input and checks where they  are equal or not

    output: output-type return (Automorphic-Non Automorphic)
    '''
    
    square = n * n
    if (n%10)==(square%10):
        return "Automorphic"
    else:
        return "Not Automorphic"

print(automorphic_number(7))