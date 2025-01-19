        #conditional statement program 

        # if - elif - else (syntax)
# if-elif
#if all are right 

#if(conditions):
    #statement1 like print(aryan)
#elif(condition):
    #statement2 like print(tashu)
#.
#.
#.
# and so on number of condtion 
  

#traffic light program

'''
light=input("Light : ")
if(light=="red"):
    print("red")
elif(light=="yellow"):
    print("LOOk")
elif(light=="green"):
    print("GO")
else:
    print("Light is Broken")'''


#grading of student  

'''Marks =float(input("Marks : "))
if(Marks>=90):
    print("A")
elif(Marks>=80):
    print("B")
elif(Marks>=70):
    print("C")
else:
    print("FAILED")'''


            # Single line if / Ternary Operator
            # <var>=<val1>if<condition>else<val2>

"""food = input("food : ")
eat = "YES" if food == "Halwa" else "NO"
print(eat)"""

'''food = input("food : ")
eat = "YES" if food == "Halwa" else "NO"
print(eat)'''
  
#another way i.e statement form 

'''food = input("Food is : "
print("EAT") if food == "Cake" or food == "samosa" else  print("Dont Eat")'''

           #clever if ternary operator
    #<var> = (false_val, true_val)[<condition>]

"""age = int(input("age : "))
vote = ("No","Yes") [age>=18]
print(vote)

salary = float(input("salary : "))
Tax = salary*(0.1,0.2) [salary>=50000]
print(Tax)
"""


# date 10 january 2025 
# elif statement only proced when when if statement is false 
# as these 2 statement will be print because every if condition is checked 
'''sum = 5
if(sum>2):
    print(" Greater Than 2")
if(sum>3):
    print("Greater Than 3")'''

    # in this case elif statement wwill not run although it is true 
'''sum=5
if(sum>2):
    print("Graeter the 2")
elif(sum>3):
    print("greater then 3")'''

# here elif statement will be procedded cause if statement is false
'''    sum=5
if(sum<2):
    print("Graeter the 2")
elif(sum>3):
    print("greater then 3")'''

# when all above the statement is false then else statement work 
'''list = [1,2,30]
for i in list:
    print(i)'''



#NESTING        if(cond):
                    #if(cond 2):

'''age=int(input("Age of driver : "))
if(age>=18):
    if(age>=80):
        print("Can not drive")
    else:
        print("can drive")
else:
    print("Can not drive 1 ")
'''


        