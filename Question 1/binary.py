def binary_search(no_array,first,last,key):
	#base condition
	if last >= first:
		mid=last+(first-last)/2
		#if element is present in mid of array
		if no_array[mid] == key:
			return mid
		#if element is less than mid element then it must be present in left subarray
		elif no_array[mid] > key:
			return binary_search(no_array,first,mid-1,key)
		#else element is greater than mid element and must be present in right subarray
		else:
			return binary_search(no_array,mid+1,last,key)
	#return -1 if element not found
	else: 
		return -1


#main function
def main():
	#creating list and adding nos to it
    no_array=list()
    n=input("enter the no. of elements:")
    print("enter nos in array:")
    for i in range(int(n)):
    	no=input("")
    	no_array.append(int(no))
    
    #taking input of element to be searched
    key=int(input("enter the no. to be searched:"))
    
    #it is set to index if element found else its value is -1
    flag=binary_search(no_array,0,n-1,key)
    
    #checking if element found or not
    if(flag!= -1):
    	print("Element found at index %d" %flag)
    else:
        raise Exception('Element not found')

# Driver Code      
if __name__ == '__main__': 
    main() 