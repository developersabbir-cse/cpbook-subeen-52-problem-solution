x = 1000
while x >= 1:
    print(x, end=" \t")
    # if you do reminder 5 % 5 it will be 0 , again 10 % 10 = 0
    if x % 5 == 0:
        print('\n \t')
    x -= 1
