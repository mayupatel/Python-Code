
# Name: Mayuri Patel


# This code is all about if/else and try/except blocks.
# In this, an adventure story of a new student commencing first day in lab and carrying out an experiment.


#print statement for student's first day in lab..
print("It’s your first day in your new lab.")
print("What’s the first thing you do in your new role as Research Assistant?")
print("1. Check your Email..")
print("2. Begin a new experiment..")

# first step:
first = str(input("enter 1 or 2 from the given choice:"))
if first == str("1"):
	print("Oh no! The PI walked in and saw that you weren't working!")
	exit()
else:
	print("An excellent choice, there's no time for frivolous, non-science things like email")

#choosing the type of experiment to perform.
#second step:
choice = str(input("What type of experiment would you like to run? exp1 or exp2: "))
print("What an excellent choice! Your investigation into " 
	+ choice + " will surely benefit all of human kind and revolutionize the way we think about everything!")

# after commencing the experiment..
#third step:
print("You make it a few steps in to your experiment when you suddenly spill chemicals all over the bench! Was it..?")
print("1.Non-hazardous")
print("2.Very-hazardous")
try:
	spill = int(input("Enter value 1 or 2 from the given choice: "))
	if spill == 1:
		print("Okay great, this isn’t a problem!")
	elif spill == 2:
		print("Uh oh, this requires some quick thinking..")
	else:
		raise
except Exception:
	print("Error! Please try only given integer input values..")
	exit()


# The spill of chemicals during an experiment..
#fourth step:
print("How to handle the spill?")
print("1.Move down the bench to a different spot and pretend like it never happened")
print("2.Clean up the spill, making sure to abide by proper cleaning protocol.")
try:
	combine = int(input("Enter value 1 or 2 only: "))
	if combine == 1 and spill == 1:
		print("This will probably be okay, let’s move on..")
	elif combine == 1 and spill == 2:
		print("You leave the spill where it is and move forward."
		  + " Later that day, the postdoc who should have supervising you eats a sandwich where you made the spill." 
		   +" Once he stopped mutating, he really didn’t mind the wings he grew, but the PI was really mad at you anyway." 
		   +" Time to look for another job! [The end]")	
	elif combine == 2 and spill == 1:
		print("You do your due diligence and clean the spill up. Time to keep going!")
	elif combine == 2 and spill == 2:
		print("Disaster averted! " 
			+ "You kept your cool, and aside from some minor chemical burns (only on the postdoc, of course) everything was fine.")
	else:
		raise
except ValueError:
	print("You have entered character! Retype it")
except Exception:
	print("Error! Invalid input...")


# when accomplished the experiment after some difficult time handling the chemicals..
#fifth step:
result1 = str("You quickly work your way through the rest of the experiment, and to your surprise, the results are amazing!" 
	+ " Pride swells in your chest! Who would have thought you could have accomplished so much in the field of " 
	+ choice + " in just one day ")
result2 = str(" and with only the slight maiming of one postdoc")
result3 = str("Now that you have your amazing results, do you…")
if combine == 2 and spill == 2:	
	print(result1+result2+result3)
else:
	print(result1+result3)


#Interaction with the PI after completing the experiment with a report of results.
#sixth step
print("In just")
print("1.Rush off to tell your PI?")
print("2.Attempt to replicate the results before telling your PI?")
print("3.Screw the PI, you did all the work anyway. Time to write a press release and practice your Nobel acceptance speech!")
try:
	finalcall = int(input("Enter anyone of these options from 1 or 2 or 3: "))
	if finalcall == 1:
		print("Your PI doesn’t appreciate being bothered with unverified results, and quickly dismisses you from their office. "
		+" Sometime later, the lazy postdoc repeats your experiment and verifies your results, but your initial contribution is largely forgotten."  
	    + " In the end, you get mentioned in the acknowledgments of the paper the postdoc writes in Science.")
	elif finalcall == 2:
		print("Your PI appreciates your diligence and commitment to reproducible science." 
    		+ "You go on to publish the work in Nature, and upon graduating you receive numerous offers of prestigious postdoc positions. " 
    		+ "In your memoirs, you write a touching dedication to the programming instructor who taught you the importance of verifying results.")
	elif finalcall == 3:
		print("Your PI doesn’t appreciate your attempt at going behind their back, but once media outlets pick up the story of your accomplishments, there’s no stopping you. "
			+ " In a surprise move, the University fires your PI and offers you their tenured position. "
			+ " Your experiment leads to numerous other breakthroughs, eventually leading to human life expectancy tripling and humanity’s first contact with alien life." 
			+ "A monument is built in dedication to you on New Earth. ")
	else:
		print("Please input correct integer value....")
except ValueError:
	print("Change the string value....")

#End of all the steps done to carry out an experiment on the first day...
#seventh step
print("Finally accomplished the experiment....")