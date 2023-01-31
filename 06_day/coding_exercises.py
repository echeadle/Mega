# file = open("files/essay.txt", 'r')
# content = file.read()
# print(content.title())
#
# file = open("files/essay.txt", 'r')
# content = file.read()
# print(len(content))

new = [i for i in ['a', 'b', 'c']]
print(new)

names = ["john smith", "jay santi", "eva kuki"]

names = [name.title() for name in names]
print(names)

temperatures = [10, 12, 14]
temperatures=[str(i)+ '\n' for i in temperatures]
file = open("file.txt", 'w')

file.writelines(str(temperatures))