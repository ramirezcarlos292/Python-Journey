# Tutorial video: https://www.youtube.com/watch?v=nlCKrKGHSSk
# python docs
#    https://docs.python.org/3/tutorial/errors.html
# Syntax Errors: Python compiler cannot compile since is syntax error
# Zero Division Error:
# File not found:
# Type error: when two data types are combined in a not possible combination
# Value error: math domain error like square root -1

# create your own exceptions instiating a class of Base Exception -> Exception

# try:
    # runs first
    # <code>
# except:
    # Runs if exception occurs in try block
    # <code>
# else:
    # Executes if try blocks succeeds
    # <code>
# finally: 
    # this code *always* executes
    # <code>

# Normal
def isNumber():
    x = int(input("Please enter a number: "))
    return x

while True:
    try:
        x = isNumber()
        break
    except ValueError:
        print("oops not a number, try again ...")


# OOP
class NumberInput:
    def __init__(self):
        self.number = None

    def is_number(self):
        try:
            self.number = int(input("Please enter a number: "))
            return True
        except ValueError:
            print("Oops, not a number, try again...")
            return False

    def get_number(self):
        while not self.is_number():
            continue
        return self.number


if __name__ == "__main__":
    number_input = NumberInput()
    number = number_input.get_number()
    print(f"The number you entered is: {number}")
