num = int(input("Enter the number ::::"))
s=0
while(num):
    r=num%10
    s=s+r
    num=num//10
    print("Sum of digits is ",s)
