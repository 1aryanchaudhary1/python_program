#print("Tashu")
# print ki command ke andr " " ke andr jo bhi likhenge vo as it is print ho  jaega 
'''name  = "Aryan"
age   = 19
price = 25.99'''
#right side se value left side m jake store hoti h equal nhi hoti 
#print("name")
#output will be name only but if we want to get the value of name which is Aryan the it will be
'''
print(name) 
print(age)
print(price)
'''
#these three only giving the value of thereself as it is
#Another way to print
'''print("My name is : ", name) 
age2 = age
print(age2)'''
#output will be 19
#identifier mean name of variables Rules for indentifiers identifier can be  combination of uppercase lowercase, digits or underscore. It can not start with digit we cannot use special characterr identifiers can be of any length 

#if we want to find the date type of a particular variable use this command 
'''print(type(name)) #string 
print(type(age))  #int
print(type(price)) #float'''

#integers int example 1 ,-1, string alphabets group of altphabet group of word sentence we can also write it in a single quote'',"",''' '''  float 3.65,4.54   {boolean have only to value True or False}   None data type a = none means there is no value assign to a 

'''old = False
b = None
print(type(old))
print(type(b))'''


#Addition
'''a = 2
b = 500
sum = a+b
print(sum)'''

#subtraction
'''a = 2
b = 5
c = a-b
print(c)'''

         #Expression Execution
         
#string& Numeric values can operate together with "*"
'''A,B=2,3
txt="@"
print(A*txt*B)
print(A*B*txt)
print(txt*A*B)'''
#output same i.e @@@@@@ 
#every print command give same answer also when we have the print something manytimes so then use * function in between that thing and no of times we want to print

# string & string can operate with "+"  called "concatenation"
'''A,B="2",3
txt="a"
print((A+txt)*B) # output 2@2@2@
print((txt+A)*B) # output @2@2@2 '''

#NUmeric values can operate with all arthematic operators for example  it follows BODMAS
'''a,b,c=3,4,5
print(a+b*c)'''

#arthematic expression with integers and float will result in float for example
'''A,B=2,5.0
c=A*B
print(c)''' #it will give output of 50.0 and not give 50

#Result of division operator with integers will be float  "/"
'''a,b=1,2
c=a/b 
d=b/a 
print(c)
print(d)'''
#integer division with float and int will give int displayed as float  "//" 
X,Y=1.5,3
Z=X//Y
print(Z,X/Y)  #output 0.0(comes after converting integer to float )  and 0.5 is printed as a  float only 

# floor gives cloeset integer which is lesser or equal to their float value 
A,B=12,5
C=A//B

print(C)  # as you can see here the answer should be 2.4 but as it gives the closet integers value i.e 2 in this case
a,b=-12,5
c=a//B

print(c) # as you can see here the answer should be -2.4 but as it gives the closet integers value i.e -3 in this case

# remainder is negative when denominator is negative 
'''a,b=-5,2
c=a%b 
print(c)
a,b=5,-2
c=a%b  
print(c)'''

