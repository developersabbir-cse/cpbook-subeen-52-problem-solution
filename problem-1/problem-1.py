for_test_case = int(input("Enter test case: "))
i = 0
while i<for_test_case:
    #taking user input
    t = int(input("Enter Number: "))
    if 1<=t<=100:
        if t%2==0:
            print("Even\n")
        else:
            print("Odd\n")
    if i==for_test_case-1:
        print("\nYou have finished the test!\n")
    i+=1
