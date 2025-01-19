# '''function : block of staement that perfrom a specific task '''

# a = 5
# b = 10
# sum = a+b
# print(sum)

# '''more line of code
# again we need to sum of two number''' 

# a = 5
# b = 17
# sum = a+b
# print(sum)

# '''so here we need to write sam ecode 2 time or in any other example we need  it  more maybe it is called redundant of code repetion e=which is a bad effect or say time comsuming
# that why we we store that code in function'''


# SYNTAX  
# def func_name(parameter1,para2,......):   defining a function its work
# somework
# return val




# def calc_sum(a,b):
#     c=a+b
#     print(c)
#     return c

# '''more line of code
# again we need to sum of two number'''

# calc_sum(1,6)    '''writing function name is called calling    here 1 and 6 or anyother vaue called arguement''' 

# '''more line of code'''
# calc_sum(12,25)  
# '''it reduce redundancy''' 

'''def calc_multi(a,b): #parameters
    return a*b
# 
# 

c=calc_multi(5,6)    #function call; arguements
print(c)
# 
# 

d=calc_multi(88,10) #function call; arguements
print(d)'''


'''def how_r_u():   #no input(parameter)
    print("x")  # no return value means no output
output = how_r_u()
print(output)   #NONE because it return nothing '''


#avg of three number
'''def avg_of3(a,b,c):
    return (a+b+c)/3
avg = avg_of3(5,6,9,)
print(avg)


avg2 = avg_of3(55,45,50)
print(avg2)


# another way 
def avg_of3(a,b,c):
    avg = (a+b+c)/3
    print(avg)
    return avg
avg_of3(4,6,5)
avg_of3(46,54,20)'''



'''#now we will be shocked
# print("Halo world") hallo world is arguement print is inbuilt fxn which we are learing from 1st day 
print("Aryan","Singh")  #sep = " "space


print("aryan")    #end = "\n" 
print("Singgh")

print("Singh",end=" ") # here we had defined the ending parameter as just space
print("singh")


print("Aryan",end=" love ") ## here we had defined the ending parameter with " love "
print("Tashu")'''




"""def calc_prod(a,b):
    print(a*b)
    return a*b
calc_prod(1,)""" # TypeError: calc_prod() missing 2 required positional arguments: 'a' and 'b'
# it will give an error 
# so to avoid error when someone not given any arguement and we dont want any error in that case we can set default value 
'''def calc_prod(a=1,b=1):
    print(a*b)
    return a*b
calc_prod()'''  # output = 1*1=1 no error 



'''def calc_prod(a,b=1):
    print(a*b)
    return a*b
calc_prod(1)'''   #here prodcut of 1 with default value of b i.e 1 is given as output


# def calc_prod(a=1,b):
#     print(a*b)
#     return a*b
# calc_prod(1)  #SyntaxError: parameter without a default follows parameter with a default  
              #first value must be non default or both a default


# practice
#WAP TO PRINT THE LENGTH OF LIST.(LIST IS A PARAMETER)
'''def len_list(list1):
    print(len(list1))
    return len(list1)
len_list([1,23,3,4,6,7,4.5,"aryan",(1,2,3)])

def len_tuple(tuple1):
    print(len(tuple1))
    return len(tuple1)
len_tuple((1,23,3,4,6,7,4.5,"aryan",(1,2,3),{1,4,3,8,99,5,6,}))'''

#WAP TO PRINT ELEMENTS OF LIST IN A SINGLE LINE9LIST PARAMETER 
'''def ele_list(list):
    for i in range(len(list)):
        print(list[i],end=",")
    return len(list)
ele_list([1,2,3,4,6,"Aryan",2.5,(1,2,3.5,"tashu")])'''

# another way
'''def print_list(list):
    for item in list:
        print(list,end=",")
        return list
print_list([1,2,3,4,6,"Aryan",2.5,(1,2,3.5,"tashu")]) '''      

#WAF TO FIND THE FACTORIAL OF n.(n is the parameter)
'''def fact_n(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
    return fact
fact_n(6)'''

#recursion  when a function call itself repeatedly

'''def show(n):
    print(n)
show(5) '''   


# recursuive function
'''def show(n):
    if(n == 0):    # base case which decide when did recursion will stop
        return n    
    print(n)
    show(n-1)
    print('end')
show(5) 

def show(n):
    if(n == 10):
        return
    print(n)
    show(n+1)
show(5)'''

'''def show(n):
    if(n == 0):    # base case which decide when did recursion will stop
        return n    
    print(n)
    show(n-1)
    print('end')
show(5) 


def show(n):
    if(n == 0):    # base case which decide when did recursion will stop
        return n    
   
    show(n-1)
    print('end')
show(5) '''


#RECURSION N!

'''def fact(n):
    if(n == 1 or n==0):
        return 1
    return fact(n-1)*n
print(fact(4)) '''  
 

 #write a recursive funnction to calculate the sum of first n natural number
'''def calc_sum(n):
    if (n == 0):
        return 0
    return calc_sum(n-1) + n
sum = calc_sum(4)
print(sum)'''

#write a recursive program to print elements of list 
def ele_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx],end=" ")
    ele_list(list,idx+1)
list = [1,2,3,3.33,"Aryan"]    
ele_list(list)