test_case = int(input("Enter test case: "))
t = 1
if 1 <= test_case <= 25:
    while test_case >= t:
        N = int(input("Enter number: "))
        n = 0
        if 1 <= N <= 80:
            while N > n:
                print("*" * N)
                n += 1
        else:
            print("Number should less then 81")
        t += 1
else:
    print("Test should be less then 25")
print("Finished")