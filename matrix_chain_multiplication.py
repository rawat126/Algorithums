# Matrix chain Multiplication....
# The algorithum used for optimum number of multiplications
# between different matrix sizes

# MCM function takes the size fo all matrixes and total combined size as input

def mcm(p,n):
    # Making first row and column to be zero
    m=[[0 for i in range(n)] for x in range(n)]

    # applying necessary steps to fill whole matrix
    for l in range(2,n):
        for i in range(1,n-l+1): 
            j=i+l-1

            # Taking maximum value for comparison
            m[i][j] = 1000000000000
            
            for k in range(i,j):
                q = m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]

                if(q<m[i][j]):
                    m[i][j]=q
    return(m[1][n-1])

# inputing number of arrays
num = int(input('How many matrics you enter : '))
arr = []

for i in range(num):
    val = input('Enter size of Array {} : '.format(i)).split('x')
    arr.append(int(val[0]))

    if(i==num-1):
        arr.append(int(val[1]))

# matrix size    
size=len(arr)

# function call
print('\nMinimum multiplications are : ',mcm(arr,size))
