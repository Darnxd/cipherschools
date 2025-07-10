a = int(input("Enter a number a : "))
b = int(input("Enter  a number b : "))
c = int(input("Enter a number c : "))

if a >= b  and a >= c:
	print("the largest number is : ",a)
elif b >= a and  b >= c:
	print("The Largest number is : ",b)
else:
	print("The Largest number is : ", c)
