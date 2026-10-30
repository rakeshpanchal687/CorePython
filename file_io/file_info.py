def fileInfo():
    fo = open("../file/hello.txt", "w")
    print("File Name: ", fo.name)
    print("Mode of Opening: ", fo.mode)
    print("Is Closed: ", fo.closed)
    fo.close()
    print("Is Closed After Closing: ", fo.closed)

fileInfo()