# Write a recursive solution to the Tower of Hanoi puzzle for n disks.
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print("Move disk 1 from", source, "to", target)
    else:
        hanoi(n - 1, source, auxiliary, target)
        print("Move disk", n, "from", source, "to", target)
        hanoi(n - 1, auxiliary, target, source)

# Example usage
disks = 3
hanoi(disks, 'A', 'C', 'B')
