"""
overall = int(input("How many words: "))
list = []

for i in range(overall):
    number = input("Add a word in the list: ")
    list.append(number)

#list.sort()
print(list)
for i in range(0, overall):
    for j in range(i, overall):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]

print(list)
"""

list = [8, 1, 64, 27, 216, 512, 64]
for i in range(0, len(list)):
    for j in range(i, len(list)):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]

print(list)