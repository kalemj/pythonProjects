import time

def singletotripleint(num):
    return int(str(num)*3)

try:
    n = int(input("Enter a digit between 1 and 9!"))

    if not 1 <= n <= 9:
        print("Please enter a single digit from 1 to 9")
    else:
        print(f"{singletotripleint(n)} divided by {n+n+n}")

        calculation = singletotripleint(n) / (n+n+n)

        if calculation == 37:
            print(calculation)
            time.sleep(1)
            print(f'{n} = 37')
        else:
            print("wrong")

except ValueError:
    print("Invalid Number Entered!")
