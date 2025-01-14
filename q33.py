# Write a function is_prime(num) that checks if a number is prime.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number to check if it's prime: "))
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
    