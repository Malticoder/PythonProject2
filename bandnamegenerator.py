print("welcome to band name generator:")
city = input("which city do you grew up in?\n")
pet = input("what is the name of the pet?\n")
print("your band name is:" + city + " " +pet)

# calculate BMI
height = 12.7
weight = 84
bmi = weight/height**2
if bmi >=25:
    print("overweight")
elif bmi >=18.5:
    print("normalweight")
else:
    print("underweight")
