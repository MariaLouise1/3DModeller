print('### Welcome to MyMusclePal! ###')

input1 = input('What is your weight in kilograms (kg)? Type the number and press enter: ' )
weight = int(input1)
protein = weight * 2
calories = weight * 30.8
proteinCal = protein * 4
remainingCal = calories - proteinCal 
print('Based on your weight of ', weight, ' you need', int(calories), 'calories per day. You should aim to eat ', protein, ' grams of protein per day (which is', int(remainingCal), 'calories)')