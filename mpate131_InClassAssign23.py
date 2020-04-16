
# Name: Mayuri Patel

#importing the module
import random

# global variable is assigned
lst = []

# this function calculate the average values with the numbers generated
def createList():
	#range of 20 numbers are generated using for loop.
	for line in range(1,21):
		#selecting 0-100 numbers and appending in list.
		lst.append(random.randint(0,100))
	
	#calculating the average..
	average = sum(lst)/len(lst)
	print("The Average of the numbers is: "+ str(average))
	
	#removing two largest numbers.
	largestNumber = max(lst)	
	lst.remove(largestNumber)
	
	secondLargeNum = max(lst)	
	lst.remove(secondLargeNum)
	
	#then calculating the average 
	average = sum(lst)/len(lst)
	
	print("The Average calculation after two largest numbers are removed: "
		+ str(average))


	#removing the two smallest numbers.
	smallestNumber = min(lst)
	lst.remove(smallestNumber)
	
	secondSmallNum = min(lst)
	lst.remove(secondSmallNum)
	
	#again calculating the average
	Average = sum(lst)/len(lst)
	
	print("The Average calculation after two smallest numbers are removed: "
	 + str(Average))
	
	#exit the function.


#main function handle all the other functions.
def main():
    createList() #calling the function
    

if __name__ == "__main__":
	main()