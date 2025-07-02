# Lab 3 Lizbeth M

# Task 1: Working with strings
food = "pumpkin pie"
print(food[0:3])
print(food[-3:-1])
first_last = food[0] + food[-1]
print(first_last)
food_list = food.split()
print(food_list)
joined_food = ' '.join(food_list)
print(joined_food)

#Task 1: Strings
food = "cheese cake" #step1
      #12345678910

print("The first 3 characters: ", food[0:3]) #2
print("The last 3 characters ", food[8:]) #3
first_last =food[0] + food[-1]
print("The first characters + last character:", first_last)





# Task 2: Working with Lists
number_list = [1,7675647456, 32, -5, 0, 234]
number_list.append(67)
#print(number_list)
print(number_list)
number_list.insert(3, 1000)
#print(number_list)
number_list.pop()
print(number_list)
number_list.remove(number_list[1])



# Task #2
number_list = [1,2,3,4,50,100,150]
print(number_list[0:3])
print(number_list[-3:])


books = {"Sing Shong" : "Omniscient Reader", "Chu Gong" : "Solo Leveling", "Gege Akutami" : "Jujutsu Kaisen", "Neville Astley" : "Peppa Pig"} #1
print(books.keys()) #2
print(books.values()) #3
print(books.get("Sing Shong")) #4
books.pop("Omniscient Reader")
print(books)
