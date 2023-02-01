from modules import parsers14
from modules import converters

feet_inches = input("Enter feet and inches: ")

parsed = parsers14.parse(feet_inches)
result = converters.convert(parsed['feet'], parsed['inches'])
print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters")
if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use this slide.")
