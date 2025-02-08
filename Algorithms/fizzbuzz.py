def fizzbuzz(input_number):
    input_number += 1
    for number in range(input_number):
        if (number % 3 == 0) and (number % 5 == 0):
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


print("input a number")
input_number = input()
fizzbuzz(int(input_number))