result = []

for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        result.append(i)

output = ", ".join(map(str,result))

print(output)
 