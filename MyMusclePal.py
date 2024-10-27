print('### Welcome to MyMusclePal! ###')

input1 = input('What is your weight in kilograms (kg)? Type the number and press enter: ' )
weight = int(input1)
protein = weight * 2
calories = weight * 30.8
proteinCal = protein * 4
remainingCal = calories - proteinCal 
print('Based on your weight of ', weight, ' you need', int(calories), 'calories per day. You should aim to eat ', protein, ' grams of protein per day (which is', int(remainingCal), 'calories)')

name = input("What is your name? ")
if name == "John":
    print("Welcome back John! ")
else:
    print("Welcome " + name)

user_input = input("Enter an integer to find out if it is even or odd: ")

# Convert the user input to an integer
user_integer = int(user_input)

if(user_integer % 2 == 0):
    print("That number is even!")
else:
    print("That number is odd!")
