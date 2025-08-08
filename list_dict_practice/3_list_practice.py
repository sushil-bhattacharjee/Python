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