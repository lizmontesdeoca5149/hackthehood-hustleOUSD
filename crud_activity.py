# CRUD Activity - Liz M

#Step 1
cookbook = []

# Step 2
def create(recipe):
    cookbook.append(recipe)
    print(f"{recipe} has been added to the cookbook.")

print(create('chicken wings'), cookbook)


# Step 3
def read():
    pass

# Step 4
def update():
    pass

cookbook = ['sushi', 'ramen', 'udon', 'tacos', 'pupusas', 'pasta']
# Step 6
def list_all_recipes():
    for recipe in cookbook:
        print(recipe)

list_all_recipes

for x in cookbook:
    print(x)

def main():
    while True:
        print("\nCookbook Recipes")
        print("1. Add a Recipe")
        print("2. Read a Recipe")
        print("3. Update a Recipe")
        print("4. Delete a Recipe")
        print("5. Display all Recipes")
        print("6. Exit")


        choice = input("Choose an option (1-6): ")


        if choice == "1":
            recipe = input("Enter the name of the recipe: ")
            create(recipe)
        elif choice == "2":
            index = input("Enter the index of the recipe to read: ")
            index = int(index)
            read(index)
        elif choice == "3":
            index = input("Enter the index of the recipe to update: ")
            recipe = input("Enter the name of the recipe you want to update it with: ")
            index = int(index)
            update(index, recipe)
        elif choice == "4":
            index = input("Enter the index of the recipe to delete: ")
            index = int(index)
            destroy=(index)
        elif choice == "5":
            list_all_recipes()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


main()

