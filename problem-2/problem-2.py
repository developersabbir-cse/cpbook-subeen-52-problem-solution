#test case (number of line)
t = int(input("Enter test case: "))
i = 0
while i<t:
    n = int(input("Enter number: "))

    if type(n)==str:
        print("You must have write something!")
        
    if 1<=n<=100:
        if n%2 == 0:
            print("Even\n")
        else:
            print("Odd\n")
    if i == t-1:
        print("You have finished test!")
    i+=1
