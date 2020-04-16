
# Name: Mayuri Patel


#this function convert the list to dictionary
def converse(months):
	
	lstTo_dict = {}

	for i in months:
		month = i[0]		
		num_days = i[1]
		
		#building the dictionary
		lstTo_dict[month] = num_days
	
	return lstTo_dict
	#exit the function and return the dictionary


#this function reverse the dictionary key:values
def reverse(lstTo_dict):
	# reversed dictionary is stored
    daysMonths = {}

    for month in lstTo_dict.keys():
    	days = lstTo_dict[month]

    	if days in daysMonths.keys():
    		daysMonths[days].append(month)
    	else:
    		daysMonths[days] = [month]

    return daysMonths
    #exit the function and return the dictionary


#this main function holds flow of code
def main():
	# a list of months and dates is given 
	months = [["January", 31], ["February", 28],["March", 31],["April", 30],["May", 31],["June", 30],["July", 31],["August", 31],["September", 30],["October", 31],["November", 30],["December", 31]]

	lstTo_dict = converse(months) #calling the function
	print(lstTo_dict)

	daysMonths = reverse(lstTo_dict) #calling the function
	print(daysMonths)

if __name__ == "__main__":
	main()