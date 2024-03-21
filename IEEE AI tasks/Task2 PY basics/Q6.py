while True:
    try:
        i = input("Please enter a number: ")
        n = float(i) 
        print("You entered:", n)
        break 
    except ValueError:
        print("Invalid input. Please enter a valid number.")


