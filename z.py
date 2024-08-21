# Problem:
# There will be a party in my home on Sunday. I will divide the people into 4 groups. The first group will be the kids group (age < 18). The second group will be Group A (age % 3 == 0). The third group will be Group B (age % 3 == 1). The rest of the people will be in Group C. Each group will sit in a table where males will sit in the left side and females will sit in the right side.


# Obtain input from the user
age = int(input("Enter your age: "))
sex = input("Enter your sex (male/female): ").lower()

# Validate the age
if age < 0:
    print("Something went wrong. Please enter a valid age.")
# Validate the sex
elif sex is not "male" or sex is not "female":
    print("Something went wrong. Please enter a valid sex.")
else:
    # Determine the message based on age and sex
    if age < 18:
        group = 'Kid Group'
    elif age % 3 == 0:
        group = "Group A"
    elif age % 3 == 1:
        group = "Group B"
    else:
        group = "Group C"

    if sex == "male":
        sitting_message = "You are a male. Please sit in the left section."
    else:
        sitting_message = "You are a female. Please sit in the right section."

    # Output the results
    print(f"You are in {age}.")
    print(sitting_message)