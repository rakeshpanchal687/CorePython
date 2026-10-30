def readFile():
    file = open("../file/hello.txt", "r")
    text = file.read()  # Read all data
    print(text)
    file.close()  # Close a file


readFile()