def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

numbers = input("Enter the comma-separeted values of numbers :")

N = numbers.split(",")
result=[]

for i in N:
    result.append(fact(int(i)))
    
output = ",".join(map(str,result))

print(output)