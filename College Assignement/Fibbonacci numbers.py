#A code to know N number of fibonacci numbers:

val=input()
val=int(val)
tim=val-2
num1=0
num2=1
fibo_=str(num1)+" "+str(num2)
for i in range(tim):
    num1,num2=num2,num1+num2
    fibo_+=" "+str(num2)
    
    
print(fibo_)