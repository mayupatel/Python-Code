
NAME: MAYURI PATEL, EMAIL: mpate131@uncc.edu

#importing the module random.        
import random


# this function takes header as parameter.
#Function reports a) Gene name b) GeneID c) ProteinID
def header_file(fastaHeader):
    '
	#1. Parse the header string for gene name.  
	geneName = fastaHeader.strip().split(" ")[1].split("=")[1].strip("]")
	print("The Gene Name is: " + geneName)

    
	#parsing header for gene id.
	geneID = ""
	fastaHeaderSplit = fastaHeader.split()[2].split(",")
	for gene in range(len(fastaHeaderSplit)):
		if fastaHeaderSplit[gene].split(":")[0].find("GeneID") != -1:
			geneID = fastaHeaderSplit[gene].split(":")[1].strip("]")
	print("The GeneID is: " + str(geneID))

    
	#parsing header for protien id.
	proteinID = fastaHeader.strip().split(" ")[-2].split("=")[1].strip("]")
	print("The ProteinID is: " + proteinID)

	#exit the function
    

#this function takes sequence as parameter
#function reports a) length of sequence b) GC content c) Reverse complement sequence
def sequence_record(seqRecord):
    
	#2. Parse the sequence record for its length.
    total = len(seqRecord)
    print("This is the total length of the sequence: " + str(total))

    #calculating GC count.
    gc_total = seqRecord.count("C") + seqRecord.count("G")
    GCcontent = gc_total/total
    print("This is the GC_content of seqRecord: " + str(GCcontent))

    #generating the reverse complement.
    reverseComplement = seqRecord[::-1]
    print("This is the reverse complement of the sequence:" + str(reverseComplement))

    #exit the function! 


#function returns the new mutated string
def nucleotide(nucleotideSeq, mutation):
	
	for i in nucleotideSeq:
		if i in "ATGC":
			continue
		else:
			#nucleotideSeq != ["A", "G", "T" , "C"]:
			print("Invalid nucleotide base....")
			# this exit the code
			exit()

	nucleotideSeq = nucleotideSeq.lower() # lowercase string

	newNucleotide = ""
    
	#the index position starts at 0
	for mutationResult in range(mutation):
		position1 = random.randint(0, len(nucleotideSeq)-1)# generated first random number
		firstRandom = nucleotideSeq[position1] # select the character of it
		print("The random position is: " + str(position1) + " and the nucleotide present is: "
			+ firstRandom)

		nucleotideList = list(nucleotideSeq)# string converted to list
		position2 = random.randint(0, len(nucleotideList)-1)# generated second random number
		secondRandom = nucleotideList[position2] # select the character of it
		print("The another nucleotide selected: " + secondRandom)

		nucleotideList[position1] = secondRandom.upper() # upper case
		newNucleotide = newNucleotide.join(nucleotideList)# list is converted to string
		print(newNucleotide)

		mutatedSeq = newNucleotide.upper()# new mutated sequence 
		print(mutatedSeq)

    #exit the function!


#this function takes sequence to mutate by transition substitution.    
def transitionSeq(nucleotideSeq,mutation):
    
    #transitions = set([('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')])
    
    newNucleotide = ""
    
    for mutationResult in range(mutation):
    	position1 = random.randint(0, len(nucleotideSeq)-1)# generated first random number
    	firstRandom = nucleotideSeq[position1]
    	print("The random position is: " + str(position1) + " and the nucleotide present is: "+ firstRandom)
    	nucleotideList = list(nucleotideSeq)
    	position2 = random.randint(0, len(nucleotideList)-1)# generated second random number
    	secondRandom = nucleotideList[position2]
    	print("The another nucleotide selected: " + secondRandom)

        # this causes the substitution of the nucleotide.
    	if firstRandom in ("A", "G") and secondRandom in( "A" , "G"):
    		nucleotideSeq[position1] = secondRandom
    		
    	if firstRandom is "C" or "T" and secondRandom is "C" or "T":
    		nucleotideSeq[position1] = secondRandom


    	print(nucleotideList)
    	newNucleotide = newNucleotide.join(nucleotideList)# list is converted to string
    	print(newNucleotide)
    
    #exit the function!


        
#this main finction handles the flow of the code.
def main():
    
    #using this fastaheader to parse and other commented header are for validating the written code.
	fastaHeader = ">lcl|NG_005905.2_cds_NP_009225.1_1 [gene=BRCA1] [db_xref=CCDS:CCDS11453.1,GeneID:672,LRG:p1] [protein=breast cancer type 1 susceptibility protein isoform 1] [exception=annotated by transcript or proteomic data] [protein_id=NP_009225.1] [gbkey=CDS]"
    
	#fastaHeader = ">lcl|NC_000007.14_cds_XP_011514170.1_1 [gene=ELN] [db_xref=GeneID:2006] [protein=elastin isoform X1] [protein_id=XP_011514170.1] [gbkey=CDS]"
	#fastaHeader = ">lcl|NC_000017.11_cds_NP_000537.3_1 [gene=TP53] [db_xref=CCDS:CCDS11118.1,GeneID:7157] [protein=cellular tumor antigen p53 isoform a] [protein_id=NP_000537.3] [gbkey=CDS]"
	#fastaHeader = ">lcl|NC_000011.10_cds_NP_000509.1_1 [gene=HBB] [db_xref=CCDS:CCDS7753.1,Ensembl:ENSP00000333994.3,GeneID:3043] [protein=hemoglobin subunit beta] [protein_id=NP_000509.1] [gbkey=CDS]"
    
    #using the sequence to parse it.
	seqRecord = "ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTG"

    #passing the parameters as header and sequence
    
	header_file(fastaHeader) # calling the function
	sequence_record(seqRecord) # calling the function
    

	# the third function is called through the input
	nucleotideSeq = input("Enter the sequence: ")
	mutation = int(input("How many mutations do you want?: "))
    
    #passing the parameters
	nucleotide(nucleotideSeq, mutation)	# calling the function

	transitionSeq(nucleotideSeq, mutation) # calling the function
	
    
    

if __name__ == "__main__":
	main()