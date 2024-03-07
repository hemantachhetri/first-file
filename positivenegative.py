
userInput = input("Any numbers")
userInputType= type (userInput)
print ('The type of user input is:', userInput Type)

userInputNumber = float(userInput)
print ("the type of userInputNumber is:", type (userInputNumber))

if userInputNumber > 0:
    print('The number is positive')

elif userInputNumber < 0:
    print ('The number is negative')

elif userInputNumber == 0:
    print ('The number is zero')
