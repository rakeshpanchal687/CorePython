def writeFile():
    file = open("../file/hii.txt", "w")
    file.write("Hi\n")
    file.write("This is Python file")
    file.close()


writeFile()