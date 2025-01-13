#dictionary are used to store data values in key:value pairs
#they are unordered, mutable & dont allow duplictate key
#forexample
#NO INDEX IN DICTIONARY
"""dict = {
            "Name" : "Aryan", 
            "marks" : 78.6,
            "Age" : 19,
        }
print(dict)"""

'''info = {
    "key" : "value",
    "name" : "Aryan",
    "is_adult" : True, #boolean
    "marks" : 94.5,    #float
    "information__" : ["hindi","English","mAths",9.5,5,True], #list
    "key1" : ("dict","set",9.5,True,5)   # tuple
}'''

   #all the data types  are acceptable in the value of dictionary
   #but we cannot use dict and list as a key "KEY ARE HASHABLE WHICH MEAN IMMUTABLE and  CANNOT BE MODIFIED AFTER INTIALIZTION SO IT caanot have unhashable value such as list dict set etc"
   #and tuple can be a key because it is immutable
   #for example

''''\Data = {
      12.99 : 95.5,
      12  : 96.5,
      ("a") : 5,
      (2) : "b",
      (2,2.4,"b",True) : (1,2,3),
      True : 1,
      False : 0,    #and so on
   }
print(Data)
print(type(Data))
#print(dict[key])
print(Data[(2,2.4,"b",True)])'''
#to assign new value to a particular key
'''Data[("a")]= 6
print(Data)'''
# to add another pair of key and value 
# Data[key name] = value
'''Data["Caste"] = "JAAT"
print(Data)'''
  

# Data1 = {
#     {2:"a"} : 5,
#     [1,"a"] : 5,
#     }
# print(Data1) #this programm will not run because we had used dict and list as a key
# starting with null dict and then adding value according to need

'''null_dict = {}
print(null_dict)
null_dict["name"] = "Aryan"
print(null_dict)'''


#Nested Dictionaries  dict in dictionary taking key as a dictionary

student ={
    "Name" : "Aryan",
    "score": {
        "chem" : "85",
        "phy"  : "40",
        "maths": "85"
    }
}
print(student)

print(student["score"])

print(student["score"]["chem"])


#to find the ltotal number of key we an find the length 
print(len(student))

#dictionary method
#dict.keys return all keys
print(student.keys())


                                 #type casting
print(list(student.keys()))
print(len(list(student.keys())))


#dict.values return all value
print(student.values())
print(list(student.values()))    #type casting


# dict.items return all key vallue pair 
print(student.items())
print(list(student.items()))     #type cast


#dict.get("key")                 #return the key according to value
print(student["Name"])           # Aryan
print(student.get("Name"))       # Aryan   same value 

#but by a chance 
# print(student["score2"])           # give error  after this line rest of code will no run so to tackle this alternate method is given below 
print(student.get("score2"))      # give None mean no key exist  it help in large code not to error because it will help rest of code and also we get NONE to rectify mistake

#dict.update(newdict)            # insert the specified intems(key value pair) to the dictionary
student.update({"city" : "delhi"})
print(student)
#alternate method
new_dict = {"city" : "delhi"}
student.update(new_dict)
print(student)
