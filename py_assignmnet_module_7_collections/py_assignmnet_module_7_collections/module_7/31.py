# 7. Working with Dictionaries

#  Write a Python program to convert two lists into one dictionary using a for loop.

list1 = ["name", "age", "city"]

list2 = ["jinal", 21, "Ahmedabad"]

my_dict = {}

for i in range(len(list1)):
    my_dict[list1[i]] = list2[i]

print(my_dict) 
