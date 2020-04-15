
# Name: Mayuri Patel

# this function converts temperature from Fahrenheit to Celsius or Vice Versa.
def temperatureConversion():
	#Entering temperatureConversion Function
	try:
		#taking user input choice
		temperatureInput = int(input("How would you like to convert the Temperature, please select one of the numeric option" +
		"\n1.Fahrenheit to Celsius " +
		"\n2.Celsius to Fahrenheit \n"))

		if temperatureInput == 1:
			# entering Fahrenheit temperature by user
			convertTemptoC = float(input("What is the Temperature in Fahrenheit?:"))
			temperatureResult = (convertTemptoC - 32) * (5/9) # converting the temperature
			print("The Temperature in Celsius is: " + str(temperatureResult) + "C")
		elif temperatureInput == 2 :
			# entering Celsius temperature by user
			convertTemptoF = float(input("What is the Temperature in Celsius?: "))
			temperatureResult = ((9/5) * convertTemptoF) + 32 # converting the temperature
			print("The Temperature in Fahrenheit is: " + str(temperatureResult) + "F")
		else:
			print(" Invalid input, Please Select any one of the valid option from the given list")
	except:
		print("Invalid Data Type, Please Enter ONLY Numeric value..")

	#Exit the function
	

# Forecast Prediction for given Temperature
def forestCastPredict():
	#Entering forestCastPredict Function
	#asking user for Fahrenheit temperature.
	ftemperature = float(input("What is the Temperature in Fahrenheit?: "))
	celsius_temp = (ftemperature - 32)/1.8 #converted into Celsius
	if (celsius_temp >= 18):
		print("It is too Hot, stay hydrated and enjoy beach vacation")
	elif (celsius_temp < 18)  and  (celsius_temp > 7.5):
		print("It is Warm today, good for hiking, biking")
	elif (celsius_temp < 7.5) and (celsius_temp > -4.5): 
		print("It is Cool and enjoy the fresh breeze")
	elif (celsius_temp <= -4.5):
		print("It is Cold, wear jacket and stay warm")
	else:
		print("enter the Numeric only..")
	#Exit the function


# Average Rainfall Prediction for given years
def averageRainfallPredict():
	#Entering: averageRainfallPredict function
	totalNumberofMonths = 0
	totalInchesofRainfall = 0
	# asking user to enter the number of years
	numberOfYears = int(input("Please Enter the Number of Years (Only in Number): "))
	for currentYear in range(1, numberOfYears + 1):
		for currentMonth in range(1,13):
			monthlyRainfall = float(input("Please Type the Inches of Rainfall for a Month "
			 + str(currentMonth) + ", Year " + str(currentYear) + ": " ))
			totalInchesofRainfall = totalInchesofRainfall + monthlyRainfall
			totalNumberofMonths = totalNumberofMonths + 1
	# calculating the average rainfall. 
	averageRainfall = totalInchesofRainfall/totalNumberofMonths

	print("Number of Months:" + str(totalNumberofMonths) +
     "\nTotal inches of rainfall: " + str(totalInchesofRainfall) 
     + "\nAverage rainfall: " + str(averageRainfall))

	#Exit the function

     
# Sea level rising for given years
def seaLevelRise():
	#Entering: seaLevelRise function
	try:
		#taking the user input..
		Years = int(input("How Many Years of Sea Level rise you want to know from the start year?:  "))
		print("Year\t", "Sea Level Rise\n------\t-----------\n")
		for currentYear in range(1, Years + 1):
			seaLevelRise = currentYear * 1.6  #Assuming 1.6mm rise per year as a reference.
			print(currentYear, "\t " , format(seaLevelRise, ".2f") + " mm")
	except ValueError:
		 print("That's not an int!, please give a valid numeric year")
	#Exit the function
	

#Season for the given month
def seasonsofMonth():
	#Enter:seasonsofMonth function
	# taking the user input
	number = int(input("Enter the number of a month (only one number): "))
	# making list of each season number.
	spring = [3,4,5]
	summer = [6,7,8]
	autumn = [9,10,11]
	winter = [12,1,2]
	# looking for the user number in the given list
	if number in spring:
		print("Month {} is the SPRING \n".format(number))
	elif number in summer:
		print("Month {} is the SUMMER\n".format(number))
	elif number in autumn:
		print("Month {} is the AUTUMN\n".format(number))
	elif number in winter:
		print("Month {} is the WINTER\n".format(number))
	else:
		print("please enter one valid number between 1 and 12\n")
	#Exit the function
	

#WindSpeedPrediction	
def windSpeedPrediction():
	#Enter: WindSpeedPrediction
	try:
		#taking user input
		windSpeed = input("Enter the speed of wind in mph or m/s: ")
		if windSpeed == "mph":
			speed = int(input("Type the wind speed: "))
			speed_multiplier = 2.237
			#calculating the speed
			speed = speed_multiplier * speed
		elif windSpeed == "m/s":
			speed = int(input("Type the wind speed: "))
			speed_multiplier = 1
			speed = round(speed)
	except NameError:
		print("only type words not numbers..")
	
	# forecasting the wind speed to user
	if (speed / speed_multiplier) < 0:
		print("There is No Wind as the wind speed is below zero")
	elif (speed / speed_multiplier) <= 2.23:
		print("the wind speed is low, go for the ride ")
	elif (speed / speed_multiplier) <= 6.70:
		print("speed is medium, continue normal outdoor activities ")
	else:
		print("speed is high, chance of bad weather, stay safe ")

	#Exit the function
	
	
# the main MENU Function handles the code..
def main():
	# starting with a menu that does calculation or conversion
	print("Please select one of the menu choice for given WEATHER AND CLIMATE FORECASTING...." +
		"\n1.Temperature Conversion " +
		"\n2.Average Rainfall Prediction" + 
		"\n3.Sea Level Rise  " + 
		"\n4.Season of the Month " +
		"\n5.Prediction of Wind Speed " +
		"\n6.Forecast Prediction")

	try:
		#user is asked for a choice to select,and based on that function is called
		choice = int(input("Select only one Number from the given Menu options: "))
		if choice == 1:
			temperatureConversion() #calling for Temperature Conversion
		elif choice == 2:
			averageRainfallPredict() #calling for Average rainfall Prediction
		elif choice == 3:
			seaLevelRise() #calling for sea level rise
		elif choice == 4:
			seasonsofMonth() #calling for season of the month
		elif choice == 5:
			windSpeedPrediction() #calling for function to know prediction of wind speed
		elif choice == 6:
			forestCastPredict() #calling for Forecast Prediction
		else:
			print("The Menu option doesn't exist...please try again ")
	except ValueError:
		print("Invalid input is given with more than one number...")


if __name__ == '__main__':
	main()