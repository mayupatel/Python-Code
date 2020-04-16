
# Name: Mayuri Patel


# this function runs the user input and give desire output.
def SearchInfo(soybaseData,userInput):

    # search the information given in the file
    # each word/sentence separated by the tab is split through first for loop.

    newDetail = ""
    descriptions = []
    count = 0

    for line in soybaseData:

        newList = line.split("\t")

        count += 1

        # print(newList)

        emptyList = []

        for i in range(len(newList)):

            # find search for userinput.

            if newList[i].find(userInput) != -1 and len(emptyList) == 0:

                emptyList.append(i)

                # three descriptions are appended

                descriptions.append(str(count) + "\t" +

                                    newList[12] + "\t" + newList[14] + "\t" + newList[16])

    newDetail = ("\n").join(descriptions)  # joining list back to string

    return newDetail
    #exit the function and return the details of search

    
# main function handle the flow of the code.
def main():

	# open and read the file to search the data
    soybaseFile = open("soybase_genome_annotation_v2.0_10-17-2019v2.txt", "r")

    # this is to skip first 10 lines which is not required
    soybaseData = soybaseFile.readlines()[12:]

    # search data based on the user input
    print("Search by:\nGeneID\nGO_ID\nEnter any Keyword")

    userInput = input("Whichever way you want to Search the Data from the file?" 
        "\nEnter/Type only one of ID/word here only: ")

    newDetail = SearchInfo(soybaseData,userInput) #calling the function
    print(newDetail)
    
    #providing user with two choice.
    print("You Want To Continue And Save The File Or Exit?")
    options = input("Enter yes to save the file or No to Exit: ")

    if options.lower() == "yes":
    	#saving the file by naming it.
        filename = input("Type the file name with less characters: ")
        file1 = open(filename, "w")

        file1.write(newDetail) # this write the file which is searched.
        file1.close()

        quit()
    else:
    	#this exit
        exit()

if __name__ == "__main__":
    main()

