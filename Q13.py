number = int(input("Starting Number: "))
last = int(input("Last Number: "))  

print("\nOdd numbers in the range:")

for num in range(number, last + 1):
    if num % 2 == 0:
        continue 
    print(num)

