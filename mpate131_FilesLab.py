


# this function runs the user input and give desire output.
def SearchInfo():

    userInput = input("Through which of the following ways you want to Search the Data from the file?\nEnter that: ")



    # open the file

    soybaseFile = open("soybase_genome_annotation_v2.0_10-17-2019v2.txt", "r")

    # print(soybaseFile)

    # this is to skip first 10 lines which is not required

    soybaseData = soybaseFile.readlines()[12:]

    # print(soybaseData[0])

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

                # print(descriptions)

    newDetail = ("\n").join(descriptions)  # joining list back to string

    print(newDetail)


    #providing user with two choice.
    print("You Want To Continue And Save The File Or Do Another Search?")

    options = input("Enter yes: save the file or No: Another search: ")

    if options.lower() == "yes":

        filename = input("Type the file name with less characters: ")

        file1 = open(filename, "w")

        # print(file1)

        file1.write(newDetail) # this write the file which is searched.

        # print(writeFile)

        file1.close()

        quit()

    else:

        SearchInfo()





# main function runs whole of the script.

def main():

    # search the information given in the file

    print("Search by GeneID\nSearch by GO_ID\nEnter any Keyword Search")

    SearchInfo()


if __name__ == "__main__":

    main()

