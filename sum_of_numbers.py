def collector():
    # supply the first number from user
    n = float(input("Enter the first number: "))
    # create an empty list to store the numbers to be added
    c = []
    # store the first number in the list
    c.append(n) # if n = 20 , [20]
    # Perform a while loop to accept more numbers from the user
    while True:
        # prompt the user if he wants to continue to add more
        q = input("Add another number? (y/n)").lower()
        if q == "y":
            m = float(input(">>>? "))
            # if yes, accept number and store in the list
            c.append(m)     # if m = 40, [20, 40]  
            pass   
        elif q == "n":
            # if no, break from the loop
            break
    # return the list
    return c

def sum_the_numbers():
   ans = collector()
   print(f"Sum: {sum(ans)}")

def diff_of_numbers():
    n = float(input("Enter a number: "))
    while True:
        s = float(input("Enter another number: "))
        ans = n - s
        print(f"Answer: {ans}")
        q = input("Continue? (y/)").lower()
        if q == "y":
            pass
        elif q == "n":
            break

def mul_of_numbers():
    n = float(input("Enter a number: "))
    while True:
        s = float(input("Enter another number: "))
        ans = n * s
        print(f"Answer: {ans}")
        q = input("Continue? (y/)").lower()
        if q == "y":
            pass
        elif q == "n":
            break

def div_of_numbers():
    n = float(input("Enter a number: "))
    while True:
        s = float(input("Enter another number: "))
        ans = n / s
        print(f"Answer: {ans}")
        q = input("Continue? (y/)").lower()
        if q == "y":
            pass
        elif q == "n":
            break

def avg_of_numbers():
    ans = collector()
    print(f"Answer: {sum(ans)/len(ans)}") # ans = [2,3,4] sum(ans) = 9, len(ans) = 3 sum(ans) / len(ans) = 9/3 = 3


# main area
while True:
    # Output Usage and Program Instructions for User
    print("Simple Arithmetic Calculator")
    print("Press '1' for Addition operation.")
    print("Press '2' for Subtraction operation.")
    print("Press '3' for Multiplication operation.")
    print("Press '4' for Division operation.")
    print("Press '5' for Average of numbers operation.")
    print("Press 'q' to quit the program.")

    op = input(">>>? ")
    



