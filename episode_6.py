with open("results.txt", "w") as outfile:
    outfile.write("The first file is " + str(volume1) + '\n')
    outfile.write("The second file is " + str(volume2) + '\n')

myfile = open(important.txt, r)
#can also be written as a for loop statement

for linefromfile in myfile:
    #instructions

linefromfile = myfile.readline()

readline = float(linefromfile)

