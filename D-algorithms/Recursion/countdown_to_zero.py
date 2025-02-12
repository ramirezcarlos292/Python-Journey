def countdown(n):
    if n == 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)  # Output: 5, 4, 3, 2, 1, Blastoff!
