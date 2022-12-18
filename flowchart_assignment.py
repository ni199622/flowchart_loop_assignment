# 1. To input a number and check if its second last digit is 7 or not
n = 127
for i in range(n+1):
    a = n%10
    if a%7==0:
        print("yes")
        break
    else:
        print("no")



'''
2. To input three sides of a triangle, a, b, and c and check if the triangle is valid.
If a+b>c and a+c>b and c+b>a , Then a triangle is possible. Do not use the and
operator.'''
a,b,c = map(int,input().split())
if a+b>c and a+c>b and c+b>a:
    print("triangle")
else:
    print("not")




'''3. You have denominations of rupee notes in the following form - 1, 2, 5, 10, 20, 100, 200,
500, 2000. Take any amount from the user and print the minimum number of notes
needed to add up to that number.'''
a = 2000
notes = [1, 2, 5, 10, 20, 100, 200, 500, 2000]
c = 0
for i in range(len(notes)):
    num = notes[i]
    x+=a//num
    a = a%num
    if a>0:
        x=-1
    print(x)



# 4. To input a number, and print all of its factors.
n = 4
for i in range(1,n+1):
    if n%i==0:
        print(i)



def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
num = 320
print_factors(num)



# 8. To find max of given N numbers
num = [4,6,2,8]
a = num[0]
for i  in range(len(num)):
    if num[i]>a:
        a = num[i]
print(a)
   

num = [9,3,2,5,7]
num.sort()
print(num[-1])


num = [9,10,3,2,5,7]
print(max(num))


# 9. To find second max of given N numbers
num =[10,2,6,5,9]
a = num[0]
for i in range(len(num)):
    if num[i]>a:
        a=num[i]
        print(a)



# 11. To input a number and check if the number is prime or not.
num = 13
flag = False
if num>1:
    for i in range(2,num):
        if num%i==0:
            flag = True
            break
if flag:
    print("not prime")
else:
    print("prime")



# 12. To input a number, N, and print first N prime numbers
lower = int(input())
upper = int(input())
for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)





# 13. To print only the prime factors of a given number N.
n = 42
for i in range(1,n+1):
    if (n%i==0):
        flag = 1
        if n>1:
            for j in range(2,i):
                if (i%2==0):
                    flag = 0
                    break
        if flag:
            print("prime number are",i)
        # else:
        #     print("prime")
        # print(i)


n = 12
i = 2
while n>1:
    if n%i==0:
        n//=i
        print(i)
    else:
        i+=1
# print(i)



'''
15. To input two numbers and print the HCF (Highest Common Factor) of those numbers.
Use the division method '''
x = 54
y = 24
if x > y:
    smaller = y
else:
    smaller = x
for i in range(1, smaller+1):
    if((x % i == 0) and (y % i == 0)):
        hcf = i 
print(hcf)


# 16. To input a number and print the sum of its digits
n=int(input("Enter a number:"))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("The total sum of digits is:",tot)




# 17. To input a number and print the reverse of that number
n=int(input())
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print(rev)


'''
18. To input a number and check if the given number is palindrome or not. A Palindromic
number is a number that remains the same when its digits are reversed. For example -
3443, 676 are palindromic numbers'''
n=int(input())
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")




'''
19. To input a number, N, and print first n numbers of the Fibonacci series. The Fibonacci
series is an infinite series, starting from '0' and '1', in which every number in the series is
the sum of two numbers preceding it in the series. Eg, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
144, 233 ….'''
num = int(input())
a = 0
b = 1
c = 0
for i in range(num):
    print(c)
    a = b
    b = c
    c = a+b