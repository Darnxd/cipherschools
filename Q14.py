start = int(input("Starting Number: "))
last = int(input("Last Number: "))

print("\nNumbers in the range:")

for num in range(start, last + 1):
    if num % 4 == 0 and num % 7 == 0:
        print(f" Breaking at {num} (divisible by both 4 and 7)")
        break
    print(num)

