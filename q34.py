# Using is_prime(), display all prime numbers between two integers start and end.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
print("Prime numbers between", start, "and", end, "are:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")