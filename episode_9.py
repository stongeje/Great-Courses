def getName():
    first = input("Enter your first name:")
    last = input ("Enter your last name:")
    full_name = last + ", " + first
    return full_name

#name = getName()

#print(name)

#def getGuess():
    number = input("Enter a number: ")
    return number

#guess = getGuess()

#print(guess)

#def getBirthday:
    month = input("Enter your birth month: ")
    day = input ("Enter your birth day: ")
    year = input("Enter your year: ")
    return month, day, year

#birthday = getBirthday()
#OR
#m, d, y = getBirthday()


#def factorial(n):
    x=1
    for i in range(1, n+1):
        x = x * i
    return x

#fact = factorial(20)
#print(fact)

def countChar(ch, teststring):
    count = 0;
    for i in range(len(teststring)):
        if teststring[i] == ch:
            count +=1
    return count

print(countChar("o", "The quick brown fox jumped over the lazy dogs."))