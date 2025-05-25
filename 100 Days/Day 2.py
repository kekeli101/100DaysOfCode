#Data Types

# #String
"Hello"

# #Integers
123456

# # Float
12233.8958

# # Boolean
True
False

# #Number of  Characters
num_char = len(input("What is your name? "))
print("Your name has" + num_char +  "letters")
# # this raises a TypeError 

num_char = len(input("What is your name? "))
new_num_char = str(num_char)
print("Your name has " + new_num_char +  " letters")


# #adding 2 numbers

two_digit_number = input("Type a two digit number ")

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit)

print(result)


# #***********BMI Calculator**************

height = input("Enter your height in meters(m): ")
weight = input("Enter your weight in kilograms(kg): ")

BMI = int(weight) / float(height)**2
BMI_as_int= int(BMI)

print("Your BMI is "+ str(BMI))
print("Your BMI (whole number) is "+ str(BMI_as_int))


# the *round* keyword, precision (number of decimal places)
print(round( 8 / 3 , 6))


# the // method, solves strsight to integer
print(8//3)


# manipulating numbers 
# eg. 
score = 0
score += 1 #adds 1 to score
score -= 1 #subtracts 1 from score


#f-strings

score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, you are {height} meters tall and you are winning is {isWinning}")



# # Life in weeks assignment
age = input("What is your current age? ")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining =  years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left"

print(message)

