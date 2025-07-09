#Task 1
checking = "yes"

while checking == "yes":
    print("What is your age")
    user_input = input()

    if int(user_input) >= 18:
        print("Yes you can vote")

    else:
        print("No you can't vote")
        print ("Would you like to check another age?")
    #user_input2 = input()
    #checking = user_input2

#Task 2
List = [-9,7,0]
for i in list:
    if i <0:
        print('positive')
    elif i < 0:
        print('negative')
    else:
        print('0')


#Task 3
inventory = ("tnt", "grass", "netherite", "waxed lightly weathered chiseled copper stairs")
for i in inventory:
    if i == "waxed lightly weathered chiseled copper stairs":
        print("why do you have this in your inventory?")
    elif i == "tnt":
        print("tnt")



