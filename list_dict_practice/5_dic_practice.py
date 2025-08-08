fav_authr = {}

fav_authr["George Orwell"] = "1984"
fav_authr["J.K. Rowling"] = "Harry Potter"

print("After adding two author: ", fav_authr)
del fav_authr["J.K. Rowling"]
print("After deleting and author: ", fav_authr)
fav_authr["Baby Bhattacharjee"] = "James Bond"
print("After adding and author :", fav_authr)


# Step 5: Use .get() to safely access values
print("\nGet 'George Orwell':", fav_authr.get("George Orwell"))  # exists
print("Get 'Dan Brown':", fav_authr.get("Dan Brown"))  # was deleted, returns None
    
# Step 6: Wildcard search (e.g., any title that has 'har' in it)
wild_result = [author for author, book in fav_authr.items() if "har" in book.lower()]
print("\nWildcard search (book titles with 'har'):", wild_result)