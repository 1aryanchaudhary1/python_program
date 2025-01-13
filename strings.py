#string 
'''str1='this is a string'
str2="this is a string"
str3="""this is a string"""
str4="this is aryan's string" #str4="this is aryan"s string"  wrong way 
str5='this is aryan"s string' #str5='this is aryan's string'  wrong way'''



#BASIC OPERATIONS
#CONCATENATION "Aryan"+"Singh" --> " AryanSingh"

'''str1 = "Aryan"
str2 = "Singh"
final_str = str1+str2
print(final_str)  #output = Aryansingh
#CONCATENATION "Aryan"+"Singh" --> " AryanSingh"
final_str = str1+" "+str2 
print(final_str)'''


# to find the length of string
'''str1 = "Aryan"
str2 = "Singh"
final_str = str1+str2
print(len(str1))
print(len(str2))
print(len(final_str))
final_str = str1+" "+str2 
print(len(final_str))'''

#indexing

'''str= "I'm in love"
print(str[1]) #output = '
str[2] = "@"'''  # this will give error because in the form of string we can only access the character, we cant  manipulate means we can not modify the character 


"""data = "GEEKFORGEEKS"

print("Indices and Index value in the list:")

# display indices in the list
for i in range(len(data)):
    print(i, data[i])"""

#SLICING
#Accessing parts of string

# str[starting_index : ending_index]   #ending idx is not included
"""str = "I'm in love"
print(str[0:3]) # output = I'm    character of index number 3 i.e " "
print(str[5: len(str)])  # from idx to the last
print(str[5:])           # from idx to the last
print(str[:5])           # from idx no 0 to idx 4 bcs 5 not included
print(str[5:3])"""

# Slicing Negative Index
str = "Aryan"
print(str[-2:-4:-1])   # output = nay  to get output from right alphabet to left  (from_where_tostart:idx_of_)




#string function  ***** we should always use parenthisis() after every

'''str = "i am a coder"
print(str.endswith("er"))   #returns true if string ends with substr
print(str.capitalize())     #capatalize 1st char
print(str.replace("am","new"))  #replaces all occurences of old wih new
print(str.find("a"))       #returns 1st index of 1st occurrence
print(str.count("am"))      #counts the occurrence of substr in string '''









