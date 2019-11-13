test_case = int(input("Enter test case: "))
w = 1
while test_case >= w:
    n = int(input("Enter number: "))
    a = 1
    print("Case %d:" % w, end=" ")
    while n >= a:
        if n % a == 0:
            print(a, end=" ")
        a += 1
    print()
    w += 1
