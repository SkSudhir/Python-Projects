sum = 0
while(True):
    userInput = input("Enter the amount or press q to quit\n")
    if userInput != 'q':
        sum = sum + int(userInput)
        print(f"Your total yet: {sum}")
    else:
        print(f"Your bill total is: {sum}")
        print("Thanks for visiting us")
        break