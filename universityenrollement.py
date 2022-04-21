"""Creating a program for Screening student for university enrollment"""


def enter_value(val):
    if val.isdigit():
        return val
    else:
        print("Invalid entry. Please, enter the correct score (e.g 5, 10, 200).")


print("UNIVERSITY ENROLLMENT SYSTEM. PLEASE FOLLOW THE INSTRUCTION.")


while True:
    try:
        jamb_score = int(input("What is your UTME(JAMB) Score? (e.g 200)"))
        score = enter_value(jamb_score)
    except ValueError:
        print("Invalid entry. ")
        continue
    if score < 200:
        print("Sorry, you are not eligible. The cut-off mark for admission is 200 marks.")
    elif score >= 200:
        print("Your UTME score meets the required marks for enrollment.")
        o_level_credit = int(input("How many O'level credit pass do you have? (e.g 5)"))
        olevel = enter_value(o_level_credit)
        if olevel < 5:
            print("Sorry, you must have at least 5 credit pass in your O'level result.")
        elif olevel >= 5:
            print("Congratulations. You have been offered admission.")
    ques = input("Continue? (Y/N)").lower()
    if ques == "y":
        pass
    elif ques == "n":
        break
