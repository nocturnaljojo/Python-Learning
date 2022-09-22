import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
# input names - [Angela, Ben, Jenny, Michael, Chloe]
#Write your code below this line 👇
whoPays = random.randint(0,len(names)-1)

print(names[whoPays] + " is going to buy the meal today!")
