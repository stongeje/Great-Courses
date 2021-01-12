#num_people = int(input("How many people are there? "))
#i = 0
#total_age = 0.0
#while (i < num_people):
    #age = float(input("Enter the age of person" +" "+str(i+1)+ ":"))
    #total_age = total_age + age
    #i = i+1
#average_age = total_age / num_people
#print("The average age was", average_age)

#for loop is simpler version of while loop -> used when there is a precise about of interations or repeats needed

#for i in range(78,4,-3):
    #print(i-1)

#for i in range(1,11):
    #for j in range(1,11):
        #print(i, "*", j, "=", (i)*(j))

#numpeople = int(input("How many people are there?"))

#what know how many pairs of people there can be from the total amount of people
#e.g. if there are 4 people then there would be distinct 6 pairs

#for i in range(1, numpeople+1):
    #for j in range(i+1, numpeople+1):
        #print(i,j)

n = int(input("Enter a number:"))
count = 0

while n != 1:
    count += 1
    if n % 2 == 0:
        n = n/2
    else:
        n = 3*n+1
    print(n)

print("We reached 1 in", count, "steps.")