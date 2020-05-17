# Fractional Knapsack Problem
# Based on Greedy approch for optimum solution

# capacity of bax and total items
capacity = int(input('Enter the capacity of Knapsack : '))
num = int(input('\nEnter number of products to consider : '))

# Necessary Inputs like :
# - price of product
# - weights of product
# - product by weight for unitry calculation
# - profit in bag
# - items in bags
price = []
weights = []
prod_by_wei = []
profit = []
items = []

# taking user defined input.....
for i in range(num):
    p = int(input('\nEnter price of Product {} : '.format(i+1)))
    w = int(input('Enter weight of Product {} : '.format(i+1)))
    p_w = p/w
    
    price.append(p)
    weights.append(w)
    prod_by_wei.append(p_w)

# Algorithum for Greedy Knapsack Problem....

while(True):
    ma = max(prod_by_wei)
    index = prod_by_wei.index(ma)

    # complete products
    if(capacity >= weights[index]):
        capacity = capacity-weights[index]
        prod_by_wei[index] = 0
        profit.append(price[index])
        items.append(index+1)

    # fractional products
    else:
        val = weights[index]/capacity
        pro = price[index]/val
        profit.append(pro)
        items.append(index+1)
        break

# Output Displayed...
print('\nItems in bag are : ',items)
print('Maximum Profit Achived : ',int(sum(profit)))
    

    



    
