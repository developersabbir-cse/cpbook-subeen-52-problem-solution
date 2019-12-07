test_case = int(input("Enter test case: "))
t = 1
if t < 100:
    while test_case >= t:
        x = list(map(int, input("\nEnter a multiple value: ").split()))
        print("Case {}: ".format(t), end="")
        for n in x[::-1]:
            if n <= 1000:
                print(n, end=" ")
            else:
                print("Every input should be less then 1001!")
        s = 1
        t += 1
