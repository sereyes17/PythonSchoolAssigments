__author__ = 'Sharayah Reyes'

n = int(input("Please enter your first number: "))
m = int(input("Please enter your second number: "))
even = 0
odd = 0

for x in range(n, m+1):
   if(x % 2 == 0):
       even = even + x
   else:
       odd = odd + x
print("Even sum =", even)
print("Odd sum =", odd)