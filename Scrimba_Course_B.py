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

msg ='Welcome  to  Python  101: Split  and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(msg.split())
print(msg.split(' '), type(msg.split(' ')))