"""
num=2
while(num<=20):
    print(num)
    num+=2
"""
#WAP To print first 10 odd number
"""
num=1
while(num<=20):
    print(num)
    num+=2

#WAP to print the sum of 10 natural number
#Using formula
n=10
print("Sum :-",(n*(n+1))/2)
"""
"""
num=1
main=0
while(num<=10):
    main=main+num
    num+=1
print(main)
"""
"""
#WAP to print the following Series: (10,20,30,40,....... ,300)
n = 10
while(n<=300):
    print(n)
    n+=10
"""
#WAP to print the following series (2,22,222,2222,22222)
"""
a='2'
i=0
while(i<5):
    print(a,end=" ")
    a=a+'2'#'2' , '22'
    i+=1
"""

# For loop
"""
     For loop is used for iterating over a sequence (that is either a list , a tuple, a dictionary,a set or a string) Ex:-a=["a","b","c"]
"""
#for i in range(0,5):
#     print(i)

#for i in range(10,15):
#    print(i)

#for i in range(1,11):
    #print(i)
#for i in range(2,22,2):
#    print(i)
#for i in range(1,22,2):
    #print(i)
#WAP to print table of a number accepted from user.
"""
a=int(input("Enter Any Number :- "))#10
for i in range(1,11):#1,2,3,4,5,6,7....10
    print(a*i)#10*1=10,10*2=20......10*10=100
"""
#WAP to print the following pattern
"""
1
12
123
1234
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")
"""
def max_of_two(x,y):
    if x>y:
        return x
    return y
def max_of_three(x,y,z):
    return max_of_two(x,max_of_two(y,z))
print(max_of_three(15,6,7))












