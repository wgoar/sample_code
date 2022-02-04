#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
cost = float(input("What is the cost of the bill before tax?\n"))

number_people = int(input("How many people are splitting the bill?\n"))

tip_percent = float(input("What percentage of tip would you like to give? 10, 12, or 15?\n"))/100

cost_per_person = "{:.2f}".format(float(((cost*tip_percent)+cost)/number_people))
print(f'Each person needs to pay {cost_per_person}.')