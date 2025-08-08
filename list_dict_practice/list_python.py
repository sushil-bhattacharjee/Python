fruits = ["apple", "banana", "cherry"]
# Print second item in the list
print("Print second item in the list")
print(fruits[1])


fruits = ["apple", "banana"]
#Add item to the above list, cherry
fruits.append("cherry")
print("\nAdd item to the above list, cherry")
print(fruits)




fruits = ["apple", "banana", "cherry"]
#Remove an item from the list
fruits.remove("cherry")
print("\n Remove an item from the list")
print(fruits)
fruits.append("blueberry")
print("\n pop index")
print(fruits)
fruits = fruits.pop(1)
print(fruits)


#Searching an item in the list as wildcard search
fruits = ["apple", "banana", "cherry"]
fruit_name_wildsearch = [f for f in fruits if "rry" in f]
print("\n Searching an item in the list as wildcard search")
print(fruit_name_wildsearch)




# Searching an item with exact match
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("banan found")






fruits = ["apple", "banana", "cherry", "blackberry"]