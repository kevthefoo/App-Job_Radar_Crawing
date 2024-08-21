cost = float(input("Cost of items: "))

def revise(discount):

    revised_cost = cost * (1 - discount)

    return revised_cost




if cost>=300:

    revised_cost = revise(0.2)

    print(f"You qualify for a 20% discount! The new discounted cost of your items is ${revised_cost}.")
elif cost>=250:
    revised_cost = revise(0.15)

    print(f"You qualify for a 15% discount! The new discounted cost of your items is ${revised_cost}.")
elif cost>=200:
    revised_cost = revise(0.1)

    print(f"You qualify for a 10% discount! The new discounted cost of your items is ${revised_cost}.")
elif cost>=100:
    revised_cost = revise(0.05)

    print(f"You qualify for a 5% discount! The new discounted cost of your items is ${revised_cost}.")
elif cost >0:
    print(f"You do not qualify yet! You still need to add something to your cart to the value of ${100 - cost}.")
else:
    print("You did not buy anything. You still need to add something to your cart to the value of $100.")


if cost == 0:
    print("You did not buy anything. You still need to add something to your cart to the value of $100.")

elif cost < 100:

    print(f"You do not qualify yet! You still need to add something to your cart to the value of ${100 - cost}.")

elif cost >= 100 and cost < 200:

    revised_cost = revise(0.05)
    print(f"You qualify for a 5% discount! The new discounted cost of your items is ${revised_cost }")

elif cost >=200 and cost <250:

    revised_cost = revise(0.1)

    print(f"You qualify for a 10% discount! The new discounted cost of your items is ${revised_cost}.")

elif cost>=250 and cost <300:

    revised_cost = revise(0.15)

    print(f"You qualify for a 15% discount! The new discounted cost of your items is ${revised_cost}.")

else:

    revised_cost = revise(0.2)

    print(f"You qualify for a 20% discount! The new discounted cost of your items is ${revised_cost}.")