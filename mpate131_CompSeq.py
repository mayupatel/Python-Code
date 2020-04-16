
#Name: Mayuri Patel

#this function generates a complementary sequence from a given one.
def complementary(strand):
	#empty string to store the sequence.
	complementary_strand= ""
	for dna in strand:
		if dna == "A":
			complementary_strand += "T"
		elif dna == "G":
			complementary_strand += "C"
		elif dna == "T":
			complementary_strand += "A"
		elif dna == "C":
			complementary_strand += "G"
		else: 
			complementary_strand += "N"

	return complementary_strand
	#exit the function with return of complementary seq


#this function generates reverse complementary strand.   
def reverse_complement(complementary_strand):

	reverse_comp = complementary_strand[::-1]
	print("The Reverse complementary Sequence is: " + reverse_comp)

	# converting the DNA to RNA..
	rna = ""
	for i in reverse_comp:
		if i == "T": # replacing the base
			rna += "U"
		else:
			rna += i

	print("Replacing T with U for RNA sequence " + str(rna))

	#locating the position of start codon.
	number_of_bases = len(rna)
	start_position = 0
	for	b in range(number_of_bases):
	    if(rna[b:b+3]=="AUG"):
	    	start_position=b

	return start_position
	#exit the function.   	
	    	   

# this handles the flow of code
def main():
	#input the sequence by user.
	print("Only Type the sequence in UpperCase")
	strand = str(input("Type the DNA sequence..? "))

	complementary_strand = complementary(strand) # calling the function.
	print("The Complementary Sequence is: " str(complementary_strand))

	# finding the invalid characters from comp seq.
	base = "N"
	indices =  [i+1 for i in  range (len(complementary_strand)) if complementary_strand[i] == base]
	print("You have given Invalid base at the position's " + str(indices))

	print("Calling for Reverse complementary strand")
	start_position = reverse_complement(complementary_strand) #calling the function.
	print("The Start Codon is at position: " + str(start_position))
			                          
	
if __name__ == "__main__":
	main()