
# Name: Mayuri Patel

# importing the modules
import random
import re


#amino acids as reference.
aa_dict = {'Met':['ATG'], 'Phe':['TTT', 'TTC'], 'Leu':['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'], 'Cys':['TGT', 'TGC'], 'Tyr':['TAC', 'TAT'], 'Trp':['TGG'], 'Pro':['CCT', 'CCC', 'CCA', 'CCG'], 'His':['CAT', 'CAC'], 'Gln':['CAA', 'CAG'], 'Arg':['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 'Ile':['ATT', 'ATC', 'ATA'], 'Thr':['ACT', 'ACC', 'ACA', 'ACG'], 'Asn':['AAT', 'AAC'], 'Lys':['AAA', 'AAG'], 'Ser':['AGT', 'AGC', 'TCT', 'TCC', 'TCA', 'TCG'], 'Val':['GTT', 'GTC', 'GTA', 'GTG'], 'Ala':['GCT', 'GCC', 'GCA', 'GCG'], 'Asp':['GAT', 'GAC'], 'Glu':['GAA', 'GAG'], 'Gly':['GGT', 'GGC', 'GGA', 'GGG'], '*':['TAA','TAG','TGA']}


#this function generates a new sequence.
def newSeq(average,freq_AA,finaldict,userchoice):
	
	#takes average and check for divisible by 3 or not.
	if average % 3 == 0:
		codon_lt = int(average)
	else:
		while True:
			a= average-10
			b= average+10
			avgcheck = random.randint(int(a),int(b))
			if avgcheck % 3 == 0:
				codon_lt = avgcheck				
				break

	#Creating mutliple Seq based on user choice			
	dnaBaselist =[]
	dnaMapList={}
	usercount =0
	while(usercount!=userchoice):
		usercount =usercount+1
		baseseq = creatnew_seq(codon_lt,average,freq_AA,finaldict)
		dnaMapList[usercount] =baseseq
				
	#End of the creating multiple sequence
	return dnaMapList


#generating a DNA sequence using the codon and Amino acid frequencies.
def creatnew_seq(codon_lt,average,freq_AA,finaldict):

	lstStopCodon = ["TAA","TGA","TAG"]
	codon_lt = int(average/3)
	
	finalLt = codon_lt-2
	#print("NEW SEQ LENGTH " + str(finalLt))
	seq_read = []
	final_seq_read = []
	dnaStr = ""
	for n in range(1,finalLt):
			
			number1 = random.randint(1,10) # selected random Amino acid freq
			for key,value in freq_AA.items():# find the amino acid
				if key == "*": 
					continue
				if number1 ==value:
					for fkey,fvalue in finaldict.items():# for AA we are looking for codon freq
						if key==fkey:
							for fskey,fsvalue in fvalue.items():
								while True:
									number2 =random.randint(0,100)
									if number2 == fsvalue:
										seq_read.append(fskey)
										break
	#appending start codon							
	final_seq_read.append("ATG")
	ctSeq =0
	for m in seq_read:
		ctSeq =ctSeq+1
		final_seq_read.append(m)
		if ctSeq==finalLt:
			stopcodon = random.choice(lstStopCodon)
			final_seq_read.append(stopcodon)# appending stop codon
			break

	#converted into a string.
	dnaBase = dnaStr.join(final_seq_read)
	#print(dnaBase)

	#exit the function by returing dna sequence
	return dnaBase


#this function mutate the sequence
def subsitute_base(dnaBase):

	newNucleotide = ""
	#stop codos are taken
	lstStopCodon = "TAA" or "TGA" or"TAG"
	mutate_count = 0
	seqlen = len(dnaBase)
	final_stopcodon = False
	# looping for substitution untill the condition is met
	while True:
		substitute_dna = ""
		mutate_count = mutate_count + 1		
		seqlen = len(dnaBase)
		lst = []

		# selecting the random position and random base
		position1 = random.randint(0, len(dnaBase)-1)
		firstRandom = dnaBase[position1]
		#print("position: " + str(position1) + " nucleotide: "+ firstRandom)

		count = 0
		
		nucleotideList = list(dnaBase)# string converted to list
		position2 = random.randint(0, len(nucleotideList)-1)# generated second random number
		secondRandom = nucleotideList[position2]
		#print("The another nucleotide: " + secondRandom)

		# second random base is placed at first random position selected.
		nucleotideList[position1] = secondRandom.lower() 
		newNucleotide = "".join(nucleotideList)# list is converted to string
		

		mutatedSeq = newNucleotide.upper()# new mutated sequence 
		
		# First condition
		if position1 ==0 or position1 ==1 or position1 ==2:
			print("FIRST CONDITION - START CODON DISRUPTION MATCH")
			#print("Number OF Iteration took to match The Condition: " + str(mutate_count))
			break

		elif position1 ==(seqlen-1)or position1 ==(seqlen-2) or position1 ==(seqlen-3):
			print("SECOND CONDITION - STOP CODON DISRUPTION MATCH")
			#print("Number OF Iteration took to match The Condition: " + str(mutate_count))
			break
		# in this regex method is used to find premature stop codon.
		else:
			codon = ""
			count = 0
			mutated_codon = []
			mutate_lt = len(mutatedSeq)

			for b in mutatedSeq:
				codon = codon + b
				count = count + 1
				if count == 3:
					mutated_codon.append(codon)
					count = 0
					codon = ""

			mutated_codonLt = len(mutated_codon)
			for i in range(0,mutated_codonLt):
				if i != mutated_codonLt-1:
					# using regular expression
					if bool(re.findall("[A-Z]",mutated_codon[i])):
						if mutated_codon[i] in lstStopCodon:
							print("THIRD CONDITION - PREMATURE STOP CODON FOUND")
							#print("Number OF Iteration took to match The Condition: " + str(mutate_count))
							final_stopcodon = True
							break
			if final_stopcodon:
				break

	#Exit the code with return of count and sequence
	return mutate_count,mutatedSeq
		

#this function execute amino acid counts,and their frequencies.
def aminoA_freq(fastaDict):
	lis = []
	seq_read = ""
	sumLt = 0
	count = 0

	for tup in fastaDict.values():		
		#join the sequences.	
		lis.append(tup)
	
	final_seq = seq_read.join(lis)
	numberBase = len(final_seq)
	
	#count of Amino acids. 
	AA_dict ={}
	
	for b in range(0, numberBase):
		codon = final_seq[ b:b + 3]#sliding window is used
		
		for key, value in aa_dict.items():
			if codon in value and key in AA_dict.keys():
				AA_dict[key] += 1
			elif codon in value:
				AA_dict[key] = 1
	
	#average/freq of Amino acids.	
	vsum = 0
	Each_val = []
	keyAA = []	
	valueAA = []
	for key, valuelst in AA_dict.items():
		Each_val.append(valuelst)
		vsum = vsum + valuelst
		keyAA.append(key)
	
	for val in Each_val:
		#calculating the average
		average_Aa = int((val/vsum)*100)
		valueAA.append(average_Aa)
	
	#building dictionary by zipping key and value
	freq_AA = dict(zip(keyAA,valueAA))
	
	#exit the function to return the AA frequencies.
	return freq_AA



#this function executes codon counts,and their frequencies.
def codon_freq(fastaDict):
	lis = []
	seq_read = ""

	#joins all the sequences into one.
	for tup in fastaDict.values():
		lis.append(tup)
		final_seq = seq_read.join(lis)
		numberBase = len(final_seq)
	
	#codon count
	newdict = {}	
	for b in range(0, numberBase):
		codon = final_seq[ b:b + 3]#sliding window is used
		#print(codon)
		for key, value in aa_dict.items():
			if codon in value and codon in newdict.keys():				
				newdict[codon] += 1
			elif codon in value:
				newdict[codon] = 1
	
	#frequencies of codons.
	finaldict = {}
	for key, valuelst in aa_dict.items():
		freqDict = {}
		count = 0
		vsum = 0
		for value in valuelst:
			count +=1
			if value in newdict.keys():
				vsum = vsum + newdict[value] #summing the number count.
		if count == len(valuelst):
			for v in valuelst:
				if v in newdict.keys():
					#calculating the frequency of codon for same Amino acid.
					freqDict[v] = int((newdict[v]/vsum)*100)
		finaldict[key] = freqDict
	
	#exit the function by returing the codons and their frequencies.
	return finaldict


#this function parse fasta file and concatenate the sequence reads.
def read_fasta(appleGen):
	#this uses yield as a generator.
	header,sequence = None,[]
	
	for line in appleGen:
		line = line.rstrip().replace('\n','')
		
		if line.startswith(">"):
			if header:
				yield (header,"".join(sequence))
				
			header,sequence =line,[]
		else:
			sequence.append(line)
 
	if header:
		yield (header,"".join(sequence))
	#exit the function by yeilding header and sequence to the main function


#this function is for average count of the sequences.
def Avg_count(filehandle):
	#parsing fasta file
	count = 0
	tot_lt = 0
	for line in filehandle:
		line = line.rstrip().replace('\n','')
		length = len(line)
		tot_lt = tot_lt + length
		if line.startswith(">"):
			pass
		else:
			count = count + 1	
	#calculating the average	
	average = int(tot_lt/count)
	
	#exit the function by returing average
	return average


#main function executes the code.
def main():
	#this is to handle file for average count.
	with open("Mdomestica_491_v1.1.cds_primaryTranscriptOnly.fa","r") as filehandle:
	
		average = Avg_count(filehandle)
		
	with open("Mdomestica_491_v1.1.cds_primaryTranscriptOnly.fa","r") as appleGen:
	
		#generator is used to parse fasta file.
		fastaDict = {}		
		for header,sequence in read_fasta(appleGen):
			fastaDict[header] = sequence
		
		#function takes parsed fasta file & returns the output for freq of AA.
		freq_AA = aminoA_freq(fastaDict)
		
		#function takes parsed fasta file and returns the output for freq of codon.
		finaldict = codon_freq(fastaDict)
		

		#this function takes all the arguments,
		#and return new sequence in the main function and also takes user input
		userchoice = int(input("How Many Sequences You Want To Generate(in number): "))

		# calling the function
		dnaMapList = newSeq(average,freq_AA,finaldict,userchoice)
		for key, value in dnaMapList.items():
			print(str(key)  + "-" +  str(value))
		
		# ask the user which seq you want to mutate
		userchoiceSeq = int(input("Which One of the Sequences You Want To Mutate, Please Select Number As Shown: " ))
		
		# this while loop is to generate and mutate the sequence.
		while True:
			if userchoiceSeq <= userchoice: 
				selectUserSeq = dnaMapList.get(userchoiceSeq)
				break
			else:
				userchoiceSeq = int(input("Invalid Choice, Please Select The Number From The Output: " ))
				selectUserSeq = dnaMapList.get(userchoiceSeq)
				continue

		# Pass User selected Sequence here in subsitute method to mutate a sequence
		mutate_count, mutatedSeq = subsitute_base(selectUserSeq)
		print("The Mutated Sequence: " + str(mutatedSeq))
		print("Number OF Iteration took to match The Condition: " + str(mutate_count))



if __name__ == "__main__":
	main()