def findMin(x):
    min = x[0]
    for i in range(0,len(x)):
        if(x[i]<min):
            min = x[i]
    return min

items = [9,5,6,4,3]

minimum = findMin(items)
print(minimum)
    
