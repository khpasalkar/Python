#takes input of list to sort it according to new order 
def sortStringArray(order, word, n):      
	word = sorted(word, key = lambda words: [order.index(c) for c in words]) 
	print("New sorted list is:")
	print(word) 

def main():
	order=str(input("enter the new lexicographical order without separation:"))
	list=input("enter the list to be sort separated by spaces:")
	n = len(list)
	#input taken in string format, hence split string based on spaces as separator into list	
	word = list.split()
	#passing the new lexicographical order, its size and list of words to function sortStringArray 
	sortStringArray(order, word, n) 

#driver function
if __name__=="__main__":
	main()
