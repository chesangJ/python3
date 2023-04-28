# Write a function that uses while, if and continue
#  statements to print all the even numbers between 0 and 50. 


def evenNumbers():
    x=0
    while x<50:
        x+=1
        if x%2!=0:
            continue
        print(x)

#  Write a function that takes an integer argument 
# and prints "Prime" if the number is prime, and "Not prime" if the number is not prime.

def prime(num):
    if num<2:
        return false
    i=2
    while i<num/2:
       if num%i==0:
        return false
        i+=1
     return true
    

# Write a function that takes a list of integers as input and 
# prints the sum of all the even numbers in the list.

def add(nums):
    x=0
    for i in nums:
        if i%2==0:
            x+=1
    print(x)

nums=[1,2,3,4,5,6,7,8,9,10]
add(nums)
            
#   Write a function that takes any two integers as input,
#    and prints the sum of all the numbers between the two integers
    # (inclusive) that are divisible by 3.
def divisible_by_three(num1,num2):  
     total=0
     for number in range(num1,num2+1):
        if number%3==0:
            total+=number
        print(total)

divisible_by_three(10,20)
     
         
     


    