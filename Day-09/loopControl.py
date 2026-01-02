numbers = [1, 2, 3, 4, 5]
print("break")
for i in numbers:
    if i==3:
        break
    print(i)
print("continued")
for i in numbers:
    if i==3:
        continue
    print(i)