test_case = int(input("Enter test case: "))
t = 1
if 1<=test_case<=10000:
    while test_case>=t:
        n = int(input("Enter Number: "))
        s = 1
        if 10000<=n<=99999:
            first_num = str(n)
            print("Sum = {}".format(int(first_num[0])+int(first_num[4])))
        else:
            print("Number should be greater then 10000")
        t += 1
else:
    print("test case should be less then 1 or greater then 10000")
print("finished")