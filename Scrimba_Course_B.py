# Number 7,10, 13, 16 Scrimba 
# Exercise 7
# item_name = 'hydrid car'
# item_price = float(5000.97)
# inventory = int(10)
# is_in_inventory = True
# print(item_name, item_price, inventory,is_in_inventory )

# # Exercise 10
# # '1 Welcome Ring To Tyler'
# msg='welcome to Python 101: Strings'
# print(msg)
# split_strings = msg.split()
# numbers_only = split_strings[3][0]
# first_word = msg[0:7]
# second_word = split_strings[1]
# last_word = split_strings[4][2:]
# name= split_strings[4][1] + split_strings[2][1] +  split_strings[0][2]  +  split_strings[0][1]  + split_strings[4][2] 
# whole_string = numbers_only + " " + first_word.capitalize() +  " " +  last_word.capitalize() +  " " +  second_word.capitalize() + " " +  name.capitalize()
# print(whole_string)
# reverse_string = whole_string[::-1]
# print(reverse_string)
# ### Alternative solution 
# msg='welcome to Python 101: Strings'
# msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]  
# print(msg1.title())
# print(msg1[::-1].t)

#Exercise 13
# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name
# first_name = str(input("Please enter name: "))
# kilo_meter = int(input("Please enter distance: "))
# distance_mls = float(kilo_meter) /1.609 
# #print(first_name.capitalize(), kilo_meter)
# kilo_meter = int(input("Please enter distance: "))
# print(f'Hi {first_name.title()}! {kilo_meter}km is equivalent to {round(distance_mls,1)} miles.')

# Excercise 16
# friends = ['John','Michael','Terry','Eric','Graham']
# cars = [911,130,328,535,740,308]
# print(friends)
# friends.sort()
# print(friends)
# friends.sort(reverse=True)
# print(friends)
# friends.reverse()
# print(friends)
# sales_w1 = [7,3,42,19,15,35,9]
# sales_w2 = [12,4,26,10,7,28] #add new number
# sales = []

# extra_sales = int(input("Add sales for Week 2 final day:"))
# sales_w2.append(extra_sales)
# sales = sales_w1 + sales_w2
# best_day_profits = max(sales) * 1.5
# worst_day_profits= min(sales) * 1.5
# total_profits = sum(sales) * 1.5
# print("Best day: $", best_day_profits)
# print("Worst day: $", worst_day_profits)
# print("Total: $", total_profits)

# msg ='Welcome  to  Python  101: Split  and Join'
# print(msg.split())
# print(' '.join(msg.split()))
#alternatively we could achieve the same results by:
#print(msg.replace(' ', "")) #where you replace all space non-spaces
# csv = 'Eric,John,Michael,Terry,Graham'
# friends_list = ['Eric','John','Michael','Terry','Graham']
#print(msg.split())
#print(msg.split(' '), type(msg.split(','))) # the split needs to be a delimeter type
# to join two lists together
#print('-'.join(friends_list+friends_list))

#Exercise 18: Split & Join
# csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
# friends_list = ['Exercise: fill me with names']
# print(friends_list)

# Lesson 19& 20: Tuples, Lists, Sets 
# friends = ['John','Michael','Terry','Eric','Graham']
# friends_tuple = ('John','Michael','Terry','Eric','Graham')
# friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
# my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}
# print(friends[2:4])
# print(friends_tuple[2:4]) #similar to lists output 
# print(friends_set.intersection(my_friends_set)) #finds the intersection
# print(friends_set.difference(my_friends_set))#finds the difference
# print(friends_set.union(my_friends_set)) #finds the union between both sets


# #Sets - blazingly fast unordered Lists 
# #empty Lists
# empty_list = []
# empyt_list = list()

# #empty Tuple
# empty_tuple = ()
# empty_tuple = tuple()

# #empty Set
# #empty_set = {} # this is wrong, this is a dictionary
# empty_set = set()

# #Sets - Exercise
# friends = {'John','Michael','Terry','Eric','Graham'}
# my_friends = {'Reg','Loretta','Colin','John','Graham'}
# cars =['900','420','V70','911','996','V90','911','911','S','328','900']
# #1. Check if ‘Eric’ and ‘John’ exist in friends
# if "Eric" in friends: print(True)
# if "John"  in friends: print(True)
# #alternative:
# print('Eric' in friends and 'John' in friends)
# #2. combine or add the two sets - +
# print(friends.union(my_friends))  
# #3. Find names that are in both sets - &
# print(friends.intersection(my_friends)) 
# #4. find names that are only in friends - "-"
# print(friends.difference(my_friends))
# #5. Show only the names who only appear in one of the lists - ^
# print(friends.symmetric_difference(my_friends))
# print(friends ^ my_friends)
# #6. Create a new cars-list without duplicates
# cars_set = {'900','420','V70','911','996','V90','911','911','S','328','900'}
# #alternatively 
# cars_set = list(set(cars))
# print(cars_set)


# Lesson 23-27: Functions

# def greeting(name, age):
#     name = name.capitalize()
#     age = str(age)
#     msg = "Hello " + name  +", you are "  +age + "!"
#     return msg

# greeting_func = greeting("brian", "32")
# print(greeting_func)

#f{} is a string literal ie this is a string variable 

# def greeting(name, age, color):
#     #print('Hello ' + name.capitalize() + ", you will be " + str(age+1) + " on your next birthday!")
#    # print(f'Salam {name.capitalize()} , you will be {str(age+1)} on your next birthday!"')
#     #print(f'aloha we hear you like the color {color.lower()}!')
#     msg = f'aloha we hear you like the color {color.lower()}!'
#     return msg
# name = "Barbora"
# age = 32
# color = "pink"

# print(greeting(name, int(age), color))


def simple(x):
    if x > 11 :
        return "A"
    elif x == 11:
        return "B"
    else:
        return x

    

print(simple(5))
print(simple(14))
print(simple(11))

