test_case = int(input("Enter test case: "))
T = 0
if 1 <= test_case <= 100:
    while T < test_case:
        r1, r2, b = map(float, input().split())
        if 1 <= r1 <= 1000 and 1 <= r2 <= r1 and 1 <= b <= 300:
            played_ball = 300 - b
            current_run_rate = (r2 / played_ball) * 6
            required_run_rate = ((r1 - r2 + 1) / b) * 6
            print("%0.2f %0.2f" % (current_run_rate, required_run_rate))
        else:
            print("You entered Wrong!")
        T += 1
else:
    print("Test Case Should less then 100")