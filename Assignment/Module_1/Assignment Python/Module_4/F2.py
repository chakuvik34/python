file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London"]
file1.writelines(L)
file1.close()
 

file1 = open("myfile.txt", "a")  
file1.write("Today \n")
file1.close()
 
file1 = open("myfile.txt", "r")
print(file1.read())
print()
file1.close()
 
