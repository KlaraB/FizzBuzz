__author__ = 'U269074'

x = int(raw_input("Insert a number from 1 do 100: "))

for x in range(1, x+1):
    if x%3 == 0 and x%5 == 0:
        print("Fizz Buzz")
    elif x%5 == 0:
        print("Buzz")
    elif x%3 == 0:
        print("Fizz")
    else:
        print("Stevilo je: " + str(x))

