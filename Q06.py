number = int(input("Enter number : "))

if number % 3 == 0 and number % 5 == 0 and number % 10 != 0:
	print("Number  is  divisible by both  3 and 5  but not by 10. ")
else :
	print("The condition is not satisfied.")

