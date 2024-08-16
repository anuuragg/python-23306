# ------------------------------- File IO & Exception Handling ------------------------------ #

try:
    file_path = "./Python/Assignment_3/content.txt"
    
    #write file
    file_data = open(file_path, 'w')
    file_content = file_data.write("New text")

    #readfile
    file_data = open(file_path, 'r')
    file_content = file_data.read()
    print("Read file content:\n", file_content)

    #Append
    file_data = open(file_path, 'a')
    file_content = file_data.write("\n New line")
    file_data = open(file_path, 'r')
    file_content = file_data.read()
    print("Appended 'New line' to the file:\n", file_content)

    #number of lines
    file_data = open(file_path, 'r')
    nummOfLines = len(file_data.readlines())
    print("Number of lines: ", nummOfLines)

    #number of words
    file_data = open(file_path, 'r')
    numOfWords = file_data.read().split(" ")
    numOfWords = len(numOfWords)
    print("Number of words", numOfWords)

    #number of charecters
    file_data = open(file_path, 'r')
    numOfChar = len(file_data.read())
    print("Number of characters: ",numOfChar)


except FileNotFoundError as err:
    print("can't open the file!")
