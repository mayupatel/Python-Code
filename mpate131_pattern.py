
NAME: MAYURI PATEL, EMAIL: mpate131@uncc.edu
        

#this function executing the code.
def checkarboard(patternInput,patternInput1,characterChoice):

	#assigning characters into two variables.
	symbol,symbol1 = characterChoice.split(',')
    
	#symbol = "#"
	#symbol1 = "%"
    
	for row in range(0,patternInput):#big box input.
		#print(row)
		for smallrow in range(0,patternInput1):#small box input.
			#print(smallrow)
			print()
			for col in range(0,patternInput):#big box input.
				for smallcol in range(0,patternInput1):#small box input.
					if row % 2 == col % 2:
						print(symbol , end = "")
					else:
						print(symbol1 , end = "")


                        
#the main function takes the input and call the function.
def main():
    
	#three input are given for a code to execute.
	patternInput = int(input("Enter the number used to form a Big Box: ")) # for big box in pattern

	patternInput1 = int(input("Enter the number used to form a Small Box within the Big Box: ")) # for small box in pattern

	characterChoice = input("Enter any two Special Characters(@#%&$*)(must be comma separated): ") # characters for the pattern


	# calling the function to take all the parameters to execute.
	checkarboard(patternInput,patternInput1,characterChoice)

    

if __name__ == '__main__':
	main()