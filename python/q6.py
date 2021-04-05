def for_version1(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0:
            total = total + num
            found_even = True

    return total


def for_version2(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0:
            total = total + num
        found_even = True

    return total

def for_version3(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0 and not found_even:
            total = total + num
        else:
            found_even = True
 
    return total

def for_version4(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0:
            total = total + num
        elif not found_even:
            found_even = True

    return total



values = []
for num in range(3, 10, 3):
    values.append(num)
print(values)


values = []
for num in range(3, 9, 3):
    values.append(num)
print(values)


values = []
for num in range(1, 3):
    values.append(num * 3)
print(values)


values = []
for num in range(1, 4):
    values.append(num * 3)
print(values)



