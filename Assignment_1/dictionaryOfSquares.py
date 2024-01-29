def create_squares(i):
    squares = {
         i : i*i
    }
    # squares = {
    #     'num': i,
    #     'sq': i*i
    # }
    return squares

n = int(input("Enter the value of n: "))
square_list = {}

for i in range(n) :
    temp = create_squares(i+1)
    square_list.update(temp)
    
    
print(square_list)