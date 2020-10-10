print("Enter your number")
number=int(input())
temp=number
reverse=0
5464
while(number>0):
    dig=number%10
    reverse=reverse*10+dig
    number=number//10
print(reverse)

if temp==reverse:
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")
    
