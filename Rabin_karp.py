# rabin -karp Algorithum......
# The algorithum uses simple Hash codes function and can
# be manipulated according to the specific requirements...... 

import random
import math

# hash codes...
def hash_codes(s):
    num = random.randint(10,100)
    adder = random.randint(3,7)
    alp = set(s)
    d = dict()
    for j,i in enumerate(alp):
        d[i]= math.fmod(num,j+adder)

    return d

# calcute sum of hash codes.....
def calc_codes_sum(s,vals):
    l=[]
    for i in s:
        l.append(vals[i])

    return sum(l)
        
# rabin-karp function.....

def rabin_karp(string,pattern):
    indixes = []
    len_pat = len(pattern)
    vals = hash_codes(string)
    
    sum_pat = calc_codes_sum(pattern,vals)
    
    for i in range(len(string)): 
        sum_sub = calc_codes_sum(string[i:len_pat+i],vals)
        if(sum_sub==sum_pat):
            
            for j in range(len_pat):
                if (pattern == string[i:len_pat+i]):
                    indixes.append(i)
                
        else:
            #print('NO')
            pass
    if(len(indixes) == 0):
        print('Pattern Not Found....')
    else:
        rm_dup = set(indixes)
        print('Total occurance : ',len(rm_dup))
        print('Pattern found at : ',rm_dup,' indixes......')


# Enabling the input from user....
s = input('Enter the string : ')
pat = input('Enter the Pattern : ')

rabin_karp(string = s,pattern = pat)
    
