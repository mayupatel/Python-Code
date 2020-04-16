
# Name: Mayuri Patel


#amino acid names as a reference to use.
aa_dict = {'Met':['ATG'], 'Phe':['TTT', 'TTC'], 'Leu':['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'], 'Cys':['TGT', 'TGC'], 'Tyr':['TAC', 'TAT'], 'Trp':['TGG'], 'Pro':['CCT', 'CCC', 'CCA', 'CCG'], 'His':['CAT', 'CAC'], 'Gln':['CAA', 'CAG'], 'Arg':['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 'Ile':['ATT', 'ATC', 'ATA'], 'Thr':['ACT', 'ACC', 'ACA', 'ACG'], 'Asn':['AAT', 'AAC'], 'Lys':['AAA', 'AAG'], 'Ser':['AGT', 'AGC', 'TCT', 'TCC', 'TCA', 'TCG'], 'Val':['GTT', 'GTC', 'GTA', 'GTG'], 'Ala':['GCT', 'GCC', 'GCA', 'GCG'], 'Asp':['GAT', 'GAC'], 'Glu':['GAA', 'GAG'], 'Gly':['GGT', 'GGC', 'GGA', 'GGG'], '*':['TAA','TAG','TGA']}


#this function search for the value based on the search criteria,
#just for one key.
def headerRead(SearchData,fileTOdict):

	if SearchData in fileTOdict:
		headerValue = fileTOdict[SearchData]
		print('The Key Values Are '+ str(headerValue))
	else:
		print('That Key Is Not In The Dictionary.')

	return headerValue
	#exit the function by returning the value
	


#this function is for only one header search.
#it takes key value and user input.
def sequenceRead(headerValue,userprompt):

	
	#sequence read from the value is taken
	#with index position.
	sequenceRead = headerValue[0]
	
	number_of_bases = len(sequenceRead)
	
	#orf 0,1,2 positions are used.
	#user input is taken
	start_position = userprompt 
	count = 1

	newdict = {}
	for b in range(start_position, number_of_bases):
		codon = sequenceRead[b:b + 3]#sliding window is used
		for key, value in aa_dict.items():
			if codon in value and key in newdict.keys():
				newdict[key] += 1
			elif codon in value:
				newdict[key] = 1
	print(newdict)
	#exit the function
	#sequence read is converted to Amino acid count.


#this function is only for one header - quality score.
def qualityScore(headerValue,userprompt1):

	seq_read = headerValue[0]

	#ord() is used to work on quality score and assign by ASCII character.
	qualityScoring =[ord(letter)-64 for letter in headerValue[1]]

	total = len(qualityScoring)
	
	trimmed_score = []
	start_position = 0
	count = 0

	for	b in range(total):
		count = count + 1
		#sliding window for quality score.
		slidingwin = qualityScoring[b:b+3]
		averageScore = sum(slidingwin)/len(slidingwin)

		length = len(slidingwin)
		#user input is looked for.
		if averageScore > userprompt1:
			trimmed_score.append(averageScore)
		else:
			#breaks when userinput is reach.
			break
	
	
	#trimming the value from the dictionary based on quality score.
	trimmed_read = (headerValue[0][:count],headerValue[1][:count])

	print(trimmed_read)
	#exit the function with the trimmed read.

			

#whole file is taken into function to count amino acids.
#user input is ORF 0,1,2.
def wholeFileSeq(fileTOdict,userprompt):
	
	aminoacidDict = {}

	for keyfile,filevalue in fileTOdict.items():
   		#picking the value based on index number.
	    sequenceRead = fileTOdict[keyfile][0]

	    number_of_bases = len(sequenceRead)
	    #user input as start point.
	    start_position = userprompt

	    count = 1
	    newdict = {}
	    for b in range(start_position, number_of_bases):
	        codon = sequenceRead[b:b + 3]
	        for key, value in aa_dict.items():
	            if codon in value and key in newdict.keys():
	                newdict[key] += 1
	            elif codon in value:
	                newdict[key] = 1
	    
	    aminoacidDict[keyfile] = newdict
	
	for key,value in aminoacidDict.items():
		print(str(key) + ": " + str(value) + "\n")
	#exit the function and prints whole file amino acid count.
	

#this function takes whole file and trim that file.
def wholeFileScore(fileTOdict,userprompt1):

	qualityscore = {}

	for key,headerValue in fileTOdict.items():

	    qualityScoring =[ord(letter)-64 for letter in headerValue[1]]
	    #print(qualityScoring)
	    total = len(qualityScoring)
	    

	    trimmed_score = []
	    start_position = 0
	    count = 0
	    for b in range(total):
	        count = count + 1
	        slidingwin = qualityScoring[b:b+3]
	        averageScore = sum(slidingwin)/len(slidingwin)
	        length = len(slidingwin)
	        
	        #print(averageScore)
	        
	        if averageScore > userprompt1:
	            trimmed_score.append(averageScore)
	        else:
	            break
	   	#print("CutoffSize " + str(count))
	    #trimming the value from the dictionary based on quality score.
	    qualityscore[key] = [headerValue[0][:count], headerValue[1][:count]]
	
	#writing the file with trimmed sequence and quality score.
	openFile = open("assignment2_trimmed.fastq", "w")
	for key, value in qualityscore.items():
		fileFast = (str(key) + "\n" + str(value[0]) + "\n" + str(key.replace('@','+')) + "\n" + str(value[1]) +"\n")
		openFile.write(fileFast)
	openFile.close()
	print("File Saved..Check The Directory")
	
	#exit the function by returning trimmed seq and score in new fastq file.


#execute all functions through Main.
def main():

    #open and read the file to convert it into a dictionary.
    with open("assignment2v2.fastq", "r") as fastq:
    	lines = fastq.readlines()
    	lstKey = []
    	lstValue = []
    	count = 0
    	tempList = []
    	for line in lines:
    		#print(line)
    		line = line.rstrip().replace('\n','')
    		
    		count = count + 1
    		if line.startswith('@'):
    			tempList = []
    			lstKey.append(line)
    		if count % 2 == 0:
    			#print(count)
    			if len(tempList) == 0:
    				tempList.append(line)
    			else:
    				tempList.append(line)

    		if len(tempList) != 0 and len(tempList) == 2:
    			lstValue.append(tempList)
    
    	fileTOdict = dict(zip(lstKey,lstValue))
    	#print(fileTOdict)

    	#The choice to parse file with one segment of record, translate whole file for Amino acids, cutoff score for whole file.
    	print("What Do You Want To Do???")
    	print("1.Parse From One Header Search\n2.Translate Whole File for Amino Acid Count\n3.Trim The Whole File For Good Quality")
    	print("Choose One Choice From The Given Menu")
    	mainSearch = int(input("Choose The Number From The Given Menu Only,Enter Here: "))
    	#parsing one header.
    	if mainSearch == 1:
    		SearchData = input("Use Entire Header Line To Search?(include @,>): ")
    		#function taking the input.
    		headerValue = headerRead(SearchData,fileTOdict)

    		print('What Is The Next Step You Want To Do??\n1.Generate The Count Of Amino Acid From The Given Sequence\n2.Trim The Nucleotide Sequence From The Quality Score.')

    		userInput = int(input('Type The Number Please: '))

    		#amino acid count.
    		if userInput == 1:
    			userprompt = int(input("Type The Reading Frame You Want To choose:(type from these three = 0,1,2): "))
    			#function takes return header value and user input.
    			sequenceRead(headerValue,userprompt)

    			#options to search more from the given input.
    			print("Do You wish To Continue?\n1.yes \n2.no")
    			continueSearch = int(input('Type From The Number Given In the Choice: '))

    			if continueSearch == 1:
    				userprompt1 = int(input("Provide Score Cutoff Value You Want To Use As A Threshold(range upto 50): "))
    				#function takes return header value and user input.
    				qualityScore(headerValue,userprompt1)

    			elif continueSearch == 2:
    				exit()

    			else:
    				print("Not Valid Input, Check Again...")

    		#trim by quality score.		
    		elif userInput == 2:
    			userprompt1 = int(input("Provide Score Cutoff value You Want To Use As A Threshold(range upto 50): "))
    			#function takes return header value and user input.
    			qualityScore(headerValue,userprompt1)

    		else:
    			print("Not From The Given Choice, Try Again....")


#exit from one header search criteria.

		#work with entire dictionary.
    	elif mainSearch == 2:
    		userprompt = int(input("Type The Reading Frame You Want To choose:(type from these three = 0,1,2): "))
    		#function takes user input and dictionary.
    		wholeFileSeq(fileTOdict,userprompt)
    		
    	#work with entire dictionary.
    	elif mainSearch == 3:
    		userprompt1 = int(input("Provide Score Cutoff value You Want To Use As A Threshold(range upto 50): "))
    		#function takes dictionary and user input.
    		wholeFileScore(fileTOdict,userprompt1)

    	else:
    		print("Oops!!! Number Doesn't Match The Search...")



if __name__ == "__main__":
    main()
