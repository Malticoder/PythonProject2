print("hello world!\n hello malti?")
print("Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl")
print("hello" + " " "malti")
#print("hello" + input("what is ur name?")+ "!")
name = "jack" #input("what is ur name?")
print(name)
#print(len(input("what is your name?")))
#username = input("what is your name?")
#length = len(username)
#print(length)
glass1 = "milk"
glass2 = "juice"
temp = glass1
glass1 = glass2
glass2 = temp
print(temp)
print("Hello"[0])
print(int("123") + int("456"))
#print(type("numbers of letter in your name"))
#print(type(length_of_name))

#print("number of letters in your name:" + str(length_of_name))

score = 0
height = 1.8
is_wining = True
print(f"your score is ={score}, your height is ={height}. your is_wining is ={is_wining}")
#print("welcome to ride:")
#height = int(input("enter the height in cm:"))
#if height >=120:
    #print("you can the ride")
    #age=int(input("enter your age:"))
    #if age <=20:
    #    print("you cannot swim:")
   # elif age >=20:
   #     print("you can swim:")
  #  else:
 #       print("sorry")
#else:
   # print("cannot ride swim")
import random
friends = ["abay","moni","kartik","deepak"]
print(random.choice(friends))
random_index = random.randint(0 , 4)
print(friends[random_index])
fruits =["apple","banana","cherry","pineapple","kiwi"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie ")
    print(fruits)
student_scores =[23,25,45,67,89,78]
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)
for number in range(1,10,3):
    print(number)

total=0
for number in range(1,101):
    total += number
print(total)



