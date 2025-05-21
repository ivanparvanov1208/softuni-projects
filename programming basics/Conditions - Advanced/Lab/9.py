productName = input()

if productName == "banana" or productName == "apple" or productName == "kiwi" or productName == "cherry" or productName == "lemon" or productName == "grapes":
    type = "fruit"

elif productName == "tomato" or productName == "cucumber" or productName == "pepper" or productName == "carrot":
    type = "vegetable"
else:
    type = "unknown"

print(type)