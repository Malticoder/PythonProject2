def greet_with_name(name,location):
    print(f"hello {name}")
    print(f"what is it like in {location}")
#greet_with_name("malti","gurugram")
greet_with_name(name="malti",location="paris")

def life_in_weeks(age):
    years_remaining = 90 - age
    weeks_remaining = years_remaining * 52
    print(f"You have {weeks_remaining} weeks left.")


life_in_weeks(12)

def calculate_love_score(name1,name2):
    combined_names = name1+name2
    lower_names = combined_names.lower()
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t+r+u+e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l+o+v+e
    score = int(str(first_digit) + str(second_digit))
    print(score)
calculate_love_score("Kanye West", "Kim Kardashian")


