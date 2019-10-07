# Complete exercise 7.1:
# Write a function that prints the numbers from 0 to 50 counting by 5.
# This function must use a while loop.
a = False
b = 0
while not a :
    print(b)
    b+=5
    if b ==55:
        a = True
    else:
        continue

# Complete exercise 7.2:
# Write a function that takes a string as a parameter and returns the number of spaces in the string.
# This function must use a while loop.
c = False
string = "Count the spaces in this sentence"
counter = 0
while not c :
    for i in string:
        if i == ' ' or i == '\n':
            counter += 1
print(counter)

# Complete exercise 7.3:
# Write a function that asks the user to enter exam scores one at a time until the word stop is entered.
# When stop is entered, the program should compute the average of the scores.
count = 0
total = 0
Grade = "y"
while Grade != "n":
    grade = int(input("Enter grades here.: "))
    for eachPass in range(grade):
        count = count + 1
        total = total + grade
        print('eachPass: {}, total: {}'.format(eachPass, total))
    Grade = input ("Are there any more grades? If not then type stop ")
    if Grade == "stop":
        print("The grade average is", round(total / count, 1))
        break

