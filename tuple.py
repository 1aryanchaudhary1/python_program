#A built in ata type that lesta us cresate immutable sequence of values
#can not delete of add value
'''tuple= {2,3,5,6}
# tup[2]=4  # show error not allignment possible
tup = ()
print(tup)
print(type(tup))'''

#single value tup writning format
'''tup = (1,)
print(type(tup))

tup = (1)
print(type(1))'''   #<alss 'int'>      (1) it will consider it as a int

# Slicng is same as of list and srtring

#tuple method

'''tup.index(ele)  # returns index of first occurenece 
tup.count(element)  # count the total occurence'''


#wap to count the number of student with the "A" grade int he following tuple

grade = ("C","D","A","A","B","B","A")
print(grade.count("A"))


#store the above values in the list an sort them form "A" to "D"
grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade[0])
