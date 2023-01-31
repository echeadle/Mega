# while True:
#     country = input("What country are you from? ")
#     country = country.strip()
#     match country:
#         case 'USA':
#             print("Hello")
#         case "India":
#             print("Namaste")
#         case 'Germany':
#             print('Hallo')
#         case 'exit':
#             break
#         case _:
#             print(f"How do you say hello in {country}?")
#


ingredients = ["john smith", "sen plakay", "dora ngacely"]
for name in ingredients:
    print(name.title())