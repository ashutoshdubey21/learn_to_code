n1 = int(input("Enter your first number: "))

n2 = int(input("Enter your second number: "))

for i in range(n1, n2+1):
    if n1 > 1:
        for j in range(2, int(n2/2)+1):
            if i % j == 0:
                break
        else:
            print(i)
