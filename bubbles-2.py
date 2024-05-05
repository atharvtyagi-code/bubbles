list = ["forbidden", "greed", "abandon", "abduct", "proactive", "responsible"]
print(list)
swap = True
while swap == True:
    swap = False
    for i in range(0, len(list)-1):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]

            swap = True

print(list)