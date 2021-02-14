
arr = list(map(ord,input('enter input String : ')))

'''
I am using Selection Sort Algorithum
'''

def selection_sort_fun(arr):    
    for j in range(len(arr)):
        min_ = arr[j]  #32
        imin = j #1 
        
        for i in range(j+1,len(arr)):#2,9
            if min_ > arr[i]:#32>13
                min_ = arr[i]#13
                imin = i #5
                
            else:
                pass

        temp = arr[imin]
        arr[imin] = arr[j]
        arr[j] = temp

    return arr

output = "".join(map(chr,selection_sort_fun(arr)))
print('\nThe Output is : ',output)
