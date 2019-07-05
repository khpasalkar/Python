# function to take the last element
def last(n):                                                          
    return n[-1]  

# sorting the list using the last element of tuple 
def sort(tuples):                                                     
    return sorted(tuples, key=last)

a = input ("Enter the list of tuple:")      
print(sort(a))                                                      
