import math
test_case = int(input("Enter test case: "))
n = 1
while n <= test_case <= 100:
    N = int(input('Enter number: '))
    sqt = math.sqrt(N)
    if  sqt * sqt == N:
        print("YES")
    else:
        print("NO")
    n += 1




    # test_case = int(input("Enter test case: "))
    # number = []
    # T = 1
    # while T <= 2 ^ 31:
    #     number.append(T * T)
    #     T += 1
    # T = 1
    # while T <= test_case <= 100:
    #     n = int(input("Enter value of n: "))
    #     if n in number:
    #         print("Yes")
    #     else:
    #         print("No")
    #     T += 1