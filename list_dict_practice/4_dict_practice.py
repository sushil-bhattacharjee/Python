# Step 1: Start with an empty dictionary
actor_roles = {}

# Step 2: Add items to the dictionary (key: actor, value: role)
actor_roles["Robert"] = "Iron Man"
actor_roles["Chris"] = "Captain America"
actor_roles["Scarlett"] = "Black Widow"
actor_roles["Tom"] = "Spider-Man"

print("After adding actors:\n", actor_roles)

# Step 3: Delete one actor by key
del actor_roles["Scarlett"]

print("After deleting 'Scarlett':\n", actor_roles)

# Step 4: Add a new actor
actor_roles["Zendaya"] = "MJ"

# Step 5: Wildcard-like search: find actors with roles containing "man"
match_roles = {k: v for k, v in actor_roles.items() if "man" in v.lower()}

print("Roles containing 'man':\n", match_roles)
