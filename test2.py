x = 0

while x == 0: 
    try: 
        fave_num = int(input("What's your favorite number? "))
        x += 1
    except: 
        print("You must enter an integer...")

if fave_num % 2 == 0: 
    print("Your favorite number is even!")
else:
    print("Your favorite number is odd!")