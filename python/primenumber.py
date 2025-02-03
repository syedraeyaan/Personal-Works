def is_prime(num):
    if num == 2:
        return (f"2 is a prime number")
    if num == 1:
        return (f"1 is not a prime number")
 
    # Loop through all the numbers between 2 and the number
    for i in range(2, num):
        # Check if the number (num) can be divided by the potential prime number
        if num % i == 0:
            return (f"{num} is not a prime number")
 
    # this return is outside the for loop which will only run once the loop finishes and none of the numbers are divisible. Therefore it is prime.
    return (f"{num} is a prime number")

num = int(input("Enter any number: "))

print(f"{is_prime(num)}")