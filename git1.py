

# Problem Statement:
# Write a Python program to check whether a given number is an Armstrong number or not.

n=int(input("enter a number"))
og=n
digits=len(str(n))
total=0

while n>0:
   digit=n%10
   total=total+digit**digits
   n=n//10
if total==og:
   print('amstrong number')
else:
   print("not amstrong number")
   





