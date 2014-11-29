print "Simple Fizz-Buzz Game."
print "Type 'quit' to exit."
while True:
    userInput = raw_input("Please enter a number: ")
    try:
        intVal = int(userInput)
        print "Fizz-Buzz" if intVal%3 == 0 and intVal%5 == 0 else "Fizz" if intVal%3 == 0 else "Buzz" if intVal%5 == 0 else intVal
    except ValueError:
        if userInput == "quit":
            break
        else:
            print "Error - not an integer, please try again!"
