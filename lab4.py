#Task 1
checking = "yes"

while checking == "yes":
    print("What is your age")
    user_input = input()

    if int(user_input) >= 18:
        print("Yes, you can vote.")

    else:
        print("No, you can't vote brochacho.")

    def checking_loop():
        while True:
            if 1<= (user_input) <= 18:
                return user_input
              

    user_input = input ("Would you like to check another age?(yes/no)").strip().lower()

    if user_input == "yes":
        continue

    elif user_input == "no":
        print("Bye bye. Returning to menu..")
        break

    else:
        print ("Invalid Input. Please type in yes/no.")



    #user_input2 = input()
    #checking = user_input2

#Task 2
Number_List = [-9,7,0,10,20,37,52]
for i in Number_List:
    if i > 0:
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

    print (i)
    


