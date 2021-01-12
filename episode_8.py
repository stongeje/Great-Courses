greeting = "Howdy!<nl>How are you today?<nl>I'm great!"

greet_split = greeting.split('<nl>')
print(greet_split)

for lines in greet_split:
    print(lines)
print("\n")

date = "01/01/2021"

date_split = date.split('/')

for line in date_split:
    print(line)
