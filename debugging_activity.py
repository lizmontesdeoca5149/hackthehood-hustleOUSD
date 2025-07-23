# Debugging Activity - Liz Montes


#Code Snippet 1:
# Incorrect:
x = 10
y = 5
result = x / y
print("Result:", result)
#Zerodivisionerror
#Don't divide by zero


#Code Snippet 2:
# Incorrect:
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
   print(numbers[i])

#Adding 1 to index makes the loop exceed the list length


#Code Snippet 3:
# Incorrect:
def calculate_area(radius):
   area = 3.14 * radius ** 2
   return area

#missing a colon at the end of def



#Code Snippet 4: missing a colon at the end of 0 and else
# Incorrect:
def is_even(number):
   if number % 2 == 0:
       return True
   else:
       return False
 
print(is_even(4))
print(is_even(7))




#Code Snippet 5: missing a colon at the end of (5)
# Incorrect:
for i in range(5):
   print(i)



#ode Snippet 6: name was outside the ""
# Incorrect:
def greet(name):
   return "Hello, name"

print(greet("Alice"))



#Code Snippet 7:
# Incorrect:
numbers = [1, 2, 3, 4, 5] #missing an indent/space at the second sum
sum = 0
for number in numbers:
    sum += number
print("Sum of numbers:", sum)



#Code Snippet 8:
# Incorrect:
def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n - 1) #should be - 1 instead of + 1
 
 #5! = 5 * 4 * 3 * 2 * 1 = 120
 
print(factorial(5))

#Code Snippet 9:
# Incorrect:
name = input("Enter your name: ")
if name == "Alice" or name == "Bob": # was infinitely true, needed name ==
   print("Hello, " + name)
else:
   print("Hello, stranger!")



#Code Snippet 10:
# Incorrect:
def divide_numbers(x, y):
   if y == 0:
      return "Can't divide by zero"
   else:
      result = x / y
   return result
 
num1 = 10
num2 = 3 # dividing by zero, u cant do that
print(divide_numbers(num1, num2))
