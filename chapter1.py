# Shaik Fahad
# 07 Nov, 2024

# Problem number 1, This program generate random greetings a friendly or an angry.

import random

def my_name(name):
    if random.randint(0,1) == 0:
        print (f"Hello, my friend {name}, How are you?." )
    else:
        print (f"Hey, it's you, {name}... WHAT DO YOU WANT?")

my_name("Fahad")

# Shaik Fahad
# 07 Nov, 2024

# Problem number 3, This program generates 10 random numbers, multiplies 10–50 by 5, and provides an updated list.

def lets_see(number):
    if 10<= number <=50:
        return True
    return False

def multiply_if():
    numbers = [random.randint(1, 1000) for i in range (10)]
    updated_numbers = []
    for num in numbers:
        if lets_see(num):
            updated_numbers.append(num * 5)
        else:
            updated_numbers.append(num)
    return updated_numbers

updated_list = multiply_if()
print(updated_list)


# Shaik Fahad
# 07 Nov, 2024

# Program 4, This program returns the input list in ascending order after removing duplicates.

def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    unique_list.sort()
    return unique_list

test_list = [1, 3, 3, 3, 6, 2, 3, 5]
print(unique_elements(test_list))