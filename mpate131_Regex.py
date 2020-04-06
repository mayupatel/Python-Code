
# NAME: Mayuri Patel, Email:mpate131@uncc.edu


#importing the module re for regular expression
import re


#1.Write a Python program to check that a string contains only a certain set 
#of characters (in this case a-z, A-Z and 0-9).

# this function checks the string validate.
def searchHead(string):
	charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    if not bool(string):
    	print("True")
    else:
        print("False")

   #exit the function by printing the boolean.


#2.Write a Python program that matches a string that has an a followed by zero or more b's

# this function checks for pattern as needed.
def searchText(a):
	char = "ab*?"
    if re.search(char,  a):
        print("Pattern Match")
    else:
        print('Pattern Not Match')

    #exit the function by printing the statement.


#3. Write a Python program that matches a string that has an a followed by one or more b's

# this function checks for pattern as needed.
def text_match(b):
	char = "ab+?"
	if re.search(char,  a):
    	print("Yes, Match Found")
  	else:
    	print('No Match')

    #exit the function by printing the statement.


#main function handles the code flow.
def main():

	print("First Question Code")
	seq = "gctaATCGtaagc"
	header = ">s1#@34#!"
	searchHead(seq) # calling the function by passing sequence
	searchHead(header) # calling the function by passing header


	print("Second Question Code")
	#each time calling a function to take different parameters.
    searchText("abcc")
    searchText("acdef")
    searchText("bbcd")
  

    print("Third Question Code")
    #each time calling a function to take different parameters.
    text_match("abc")
    text_match("ac")

  
if __name__ == "__main__":
  main()