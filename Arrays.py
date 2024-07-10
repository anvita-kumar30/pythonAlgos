new_list = [1, 2, 3, 4, 5, 6]
print(new_list)
result = new_list[0]
print(result)

if 1 in new_list: print(True)

for n in new_list:
    if n==1:
        print(True)
        break

for i in range(len(new_list)):
    print(new_list[i])

numbers = []

print(len(numbers))

numbers.append(2)
numbers.append(200)
print(numbers)

num2 = []
num2.extend([4, 5, 6])
print(num2)

num2.insert(2, 11)
print(num2)

num2.remove(11)
print(num2)

print(num2.index(5))

if 5 in num2: print(True)
if 30 not in numbers: print(True)

num2[0] = 22 # Updates first element in list to 22
print(num2)