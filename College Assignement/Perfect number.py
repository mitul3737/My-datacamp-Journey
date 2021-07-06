#Write a Python program that takes a number and tells if it is a perfect number or not. [The input number has to be an INTEGER]

#Perfect Number: An integer number is said to be a perfect number if its factors, including 1 but not the number itself, sum to the number.



num = int(input(''))
div = ""
sum=0
for j in range(1, num):
       if num % j == 0:
            sum+=j
​
if sum==num:
    print(num,"is a perfect number")
else:
    print(num,"is not a perfect number")
    