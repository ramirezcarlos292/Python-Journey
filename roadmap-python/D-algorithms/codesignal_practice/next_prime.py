def next_prime(n):
    if n > 1:
        temp = n + 1
        i = 2
        while temp > n:
            if temp % i != 0:
                return temp
            else:
                i += 1
    #     for i in range(2, (n//2)+1):
    #         temp = n//2
            
    #         if (n % i) == 0:
    #             print(n % i)
    #             print(n, " is not a prime number")
    #             break
    #     else:
    #         print(n, "is a prime number")
    # else:
    #     print(n, "is not a prime number")
    
        
        
if __name__ == "__main__":
    print(next_prime(11))