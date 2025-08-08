test_list = []

#append three items with the empty list
test_list.append("Bond")
test_list.append("Hrithik")
test_list.append("Baby")

print("After appending: ", test_list)

test_list.pop(1)
print("After poping : ", test_list)

search = [u for u in test_list if "a" in u]
print("After wildsearch result: ", search)