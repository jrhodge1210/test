while True: 
    try: 
        fave_num = int(input("What's your favorite number? "))
        return False
    else: 
        print("You must enter an integer...")

if fave_num % 2 == 0: 
    print("Your favorite number is even!")
else: 
    print("Your favorite number is odd!")