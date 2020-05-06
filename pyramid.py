num = int(input("Input the number."))

columns = num * 2 - 1
for i in range(1,num+1):
    equals = i * 2 - 1
    minus = int((columns - equals)/2)
    for j in range(minus):
        print(" ", end="")
    for k in range(equals):
        print("=", end ="")
    for l in range(minus):
        print(" ", end="")
    print("\n")
