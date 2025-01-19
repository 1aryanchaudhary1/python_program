#while loops ( jab tak)
 # print hello 5 times

'''i =  0   # i or any other variable called iterator and running in the loop called iteration 
while i <=5:
    print("hello")
    i += 1 ''' 

# Practise question
#print number from 1 to 100
'''i = 1
while i<=100:
    print(i)
    i +=1'''

    # print number from 100 to 1
'''i = 100
while i>=1:
    print(i)
    i -=1'''
# print the multipication table of a number n
'''n = int(input())
i = 1 
while i<=10:
    print( n*i)
    i +=1'''

# print the element of the following list using a 
'''list = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(list):
    print(list[idx],idx)
    idx += 1'''


#search for element of the following tuple using loop
'''tuple = (1,4,9,16,25,36,49,64,81,100)
ele = 36
i = 0      
while i < len(tuple):
    if(tuple[i] == ele):
        print("Found at idx", i)
    i +=1   

tuple = (1,4,9,16,25,36,49,36,81,100)
ele = 36
i = 0      
while i < len(tuple):
    if(tuple[i] == ele):
        print("Found at idx", i)
    else:
        print("Finding")
    i +=1 '''




# BREAK AND CONTINUE
# BREAK: used to terminate the loop when encountered
'''i = 1
while i <=5:
    print(i) 
    if( i == 3):
        break
    i +=1
print("end of loop")  

tuple = (1,4,9,16,25,36,49,36,81,100)
ele = 36
i = 0      
while i < len(tuple):
    if(tuple[i] == ele):
        print("Found at idx", i)
        break
    else:
        print("Finding")
    i +=1 
print("end of looop")'''






#continue : terminate executioon in the current iteration & continues exection of the loop with the next iteration


'''i = 0
while i<=5:
    if(i == 3):
        i += 1
        continue    #skip the print of 3 bye adding 1 to it
    print(i)
    i +=1'''


# IF WE AHD TO WORK WITH THE HELP OF ITERATOR THEN WE USE WHILE LOOP MEAN IF HAD VAIRABLE IN LIST OR TO UPDATE ITS  VALUE HAVING STOPING CONDITION WE USE WHILE
#IF WE HAD TO WORK ON DATA TYPE AND TRAVERSE 



# For Loops are used for sequential traversal. for transeversiing list string tuple etc which had index.       
# syntax for loops
# for el in list
     #somework
'''list = [1,2,3,4,5]
for element in list:
    print(element)

list1 = ["a","b","c",3.6,5] 
for val in list1:
    print(val)   

str = "iloveher"
for char in str:
    print(char)  ''' 


# While using FOR LOOPS OR WHILE LOOPS we can use optional else      after completion of loop if we wanted to do some other work then we can use else

'''str = "iloveher"
for char in str:
    if(char == "o"):
        print("o found")
        break
    print(char)
print("END")   # in this case end is print no matter full loop is executed or not 

# so in case of we wanted to do some work when loop is completed then we use else

str = "iloveher"
for char in str:
    if(char == "o"):
        print("o found")
        break
    print(char)
else:
    print("END")





str = "iloveher"
for char in str:
    if(char == "o"):
        print("o found")
    print(char)
else:
    print("END")'''






#print the element of the following list using a loop:
'''list = [1,4,9,16,25,36,49,64,81,100]
for ele in list:
    print(ele)'''


    # search a number x in this tuple using lloop
'''tuple = (1,4,9,16,25,36,49,64,81,100)  
x = int(input())
for ele in tuple:
    if(ele == x):
        print(ele,"X is found")
        break
    print(ele)'''

# Another 

'''tuple = (1,4,9,16,25,36,49,64,81,100)  
x = int(input())
for ele in tuple:
    if(ele == x):
        print(ele,"X is found")
        break
    print(ele)
else:    # if a number not founded mtlb if wali condtion false hogai toh sarey element print hoke else ki condtion print hojaegi
    print("NOT found Program ended")'''






#RANGE   range function returns a sequence of numbers, starting from 0 by default, and increments by 1(by default), and stops before a specified number    

# stntax range(start?(0 by default),stop,step?(by default1)) if we havent given start value it will start from 0 asame as in step size but stop value is compulsory 

'''print(range(5))   # range(stop)                 started from 0 increment of 1 and till the 5 
print(range(2,10))      #range(start,stop)    started from 2 end at 10 increment of 2
print(range(2,10,2))    #range(start,stop,step)
for el in range(2,20,3):
print(el)'''


#PRACTICE QUESTION
# PRINT NUMBER FROM 1 TO 100
'''for num in range(1,101,1):
    print(num)
    print("\n")'''

#print number from 100 to 1
'''
for num in range(100,0,-1):
    print(num)'''

#print the multiplication table of n
'''n = int(input())
for i in range(1,11,1):
    print(n,"x",i,"=",n*i)'''


#PAAS STATEMENT : pass is a nulll statemen that does nothing. it is required as a placeholder for future code

# Syntax
for el in range(10):
    pass

# for i in range(5):
                            # if we wanted to keep is empty
# print("some useful work")   # expected an indented block after 'for' statement on line 223 to avoid this 

'''for i in range(5):
    pass    # skip the loop 
print("some useful work")'''

#PASS CAN BE USED IN IF ELSE ALSO
# if i>5:
#    pass

#practice quetsion

# write  a program to find the num of first n number (using while)
'''n= int(input())
i=1
sum=0
while i<=n:
    sum += i
    i += 1
print("Sum of first",n,"num is ",sum)'''

'''
n= int(input())
sum=0
for i in range(1,n+1):
    sum += i  
print("Sum of first",n,"num is ",sum)'''







'''#wap to find the factorial of n using while loop 
n = int(input())
i = 1
fact = 1
print("step of fact of",n,"is" )
while i<=n:
    fact=fact*i
     i += 1
    print(fact,"*",i,"=",fact*1)  
       # these both print command is in loop so it print each step  
print("factorial of",n,"is",fact)        #fact of 5 is 120  it priny only final answer'''




# factorial of n using for loop
'''n = int(input())
fact=1
for i in range(1,n+1):
     fact *= i
    # or fact=fact*i
print("factorial of",n,"is",fact)'''


