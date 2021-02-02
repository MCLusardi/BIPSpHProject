file = open("TestWrite.txt", "a") #opening file for writing, will create if it doesn't exsit
if(file == None):
    print("File could not be opened\n")
else:
    file.write("pH, DateTime")
    file.close()
print("All Done!");