def search(num,start,end,list_):
    ind = (start+end)//2
    le = len(list_)
    if(le==1):
        if(num == list_[0]):
            return '0'
        
    elif -1< ind <le:
        if(list_[ind]==num):
            return ind
        
        elif(end-start == 0 and list_[ind]!=num or ind>=le):
            return False 

        elif(list_[ind]>num ):
            last = ind
            start = 0
            return search(num,start=start,end=last,list_=list_)
            
        elif(list_[ind]<num ):
            last = le
            start = ind+1
            return search(num,start=start,end=last,list_=list_)
    else:
        return False


data = list(map(int,input("Enter The values : ").split()))
value = int(input("Enter the number you want to search : "))

index = search(value,0,len(data),data)

if(index == False):
    print("Value not found.....!")
else:
    print("Found at index : ",index)
