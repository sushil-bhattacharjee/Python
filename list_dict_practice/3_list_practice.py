actor_list = []

# 1. Print empty list
print("Print the initial list: ", actor_list)

# 2. Append 5 actors
actor_list.append("Robert")
actor_list.append("Chris")
actor_list.append("Scarlett")
actor_list.append("Tom")
actor_list.append("Natalie")

print("After appneding: ", actor_list)

# 3. Remove the 3rd item (index 2 -> Scarlett)
actor_list.pop(2)
print("After removing 3rd items: ", actor_list)

# 4. Append "Zendaya" (adds at the end)
actor_list.append("Zendaya")
print("After update last item : ", actor_list)

# 5. Wildcard search for names containing lowercase "t"
wild_match = [u for u in actor_list if "t" in u.lower()]
print("Print the wildcard search match: ", wild_match)


movie_list = [
    {"name": "Tomorrow never dies", "genre": "Spy", "series": "James Bond"},
    {"name": "No Time to Die", 
     "genre": "Spy", 
     "series": "James Bond"},
    {"name": "Rogue Nation", "genre": "Spy", "series": "MIF"},
    {"name": "Golden Eye", "genre": "sci-fi", "agency":"MI6"}
]

# For the above list, find the series name for movie name "Rouge Nation"
# find the genre name for movie name Golden Eye
print("\n ### USING enumerate(list) ####")
for index, value in enumerate(movie_list):
    if value["name"].lower() == "Rogue Nation".lower():
        print(f"Movie {value['name']} is in {value['series']}")
    elif "gold".lower() in value["name"].lower():
        print(f"Movie {value['name']} is in {value.get('agency')}")

print("\n ############ Using List comprehension ##############")
result = [value["series"] for value in movie_list if value["name"].lower() == "Rogue Nation".lower()]
print(result[0] if result else "Not Found")
result = [value["agency"] for value in movie_list if "gold".lower() in value["name"].lower()]
print(result[0] if result else "Not Found")