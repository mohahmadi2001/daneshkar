laptops = [
    # {"price": 1, "quality": 10},
    # {"price": 7, "quality": 3},
    # {"price": 1, "quality": 5},
    # {"price": 7, "quality": 9},
    # {"price": 5, "quality": 6},
    {"price": 2000, "quality": 1},
    {"price": 1000, "quality": 2},
    {"price": 3000, "quality": 3},
    {"price": 4000, "quality": 4},
    {"price": 5000, "quality": 5},
]
found = False
for i in range(len(laptops)):
    for j in range(i+1, len(laptops)):
        if laptops[i]["price"] < laptops[j]["price"] and laptops[i]["quality"] > laptops[j]["quality"]:
            found = True  
        else:
            found = False
if found:
    print("Founded")
else:
    print("Not Found")
           
# laptops = [
#     {"price": 2000, "quantity": 1},
#     {"price": 1000, "quantity": 2},
#     {"price": 3000, "quantity": 3},
#     {"price": 4000, "quantity": 4},
#     {"price": 5000, "quantity": 5},
# ]
# flag = False
# for laptop in laptops:
#     for other_laptop in laptops:
#         if laptop is  other_laptop:
#             continue
#         if (
#             (laptop["price"] - other_laptop["price"])
#             * (laptop["quantity"] - other_laptop["quantity"])
#         ) <= 0:
#             flag = True
#             break
#     else:
#         continue
#     break

# print("Found" if flag else "No found")
