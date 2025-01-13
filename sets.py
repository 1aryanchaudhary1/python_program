#set in python   {}
# only value no key value pair
# Set is the collection of the unordered intems
# each elemant in the set must be unique & immutble
#set is mutable but element of set are immutable
# dict and list can not be stored in set
# boolean int float str tuple can be dstored in set




'''collection = {1,2,3,4}
print(collection)
print(collection)
print(type(collection))
collection1 = { 1,1,2,3,4,"hello",2.5,True,False,False,"World","World"}

print(collection1)  # 
also when in a set 1 and True are present the it will also treated as same element and same in case of 0 and False  so that why here it is ignoring true and another 1 and giving us just 1
it does not give error in case of same value in set print output it will just ignore the repeated value like in this case world,1 output
print(len(collection1))

#empyt set
collection = {} #empty dict # syntax
print(type(collection))

collection = set() #syntax for creating a empty set
print(type(collection))'''



# Set methods


# Set.add(ele)  add an element
'''data = set()
data.add(2)
data.add(1)
data.add(3)
data.add("aryan")     # string
data.add((1,2,3,"aryan"))    # tuple
# data.add([1,2,3,4])          #   TypeError: unhashable type: 'list'       it givs error becauselist can not be in a set
print(data)  # output  {1, 2, 3}


# set.remove(el)  removes the element 
data.remove(2)
print(data)   # output {1, 3}
                        # print(data.remove(7))   #   KeyError: 7       it will give error because 7 is not the element of data'''


# set.clear()  empties the set
'''print(data.clear())  #none 
print(len(data))'''   # 0 output


# set.pop() removes a random value 
'''Set = {1,2,3,"Aryan","tashu"}
print(Set.pop())
print(Set.pop())
print(Set.pop())
print(Set.pop())'''

#set.union(set2) combines both set value & returns new 
set1 = {1,2,3}
set2 = {True,3,4,5}
print(set1.union(set2))    # output {1, 2, 3, 4, 5}  duplicate value count as one
set


# set.intersection(set2) common values & returns new

print(set1.intersection(set2))   # {1, 3}   common value from both set






#FIGURE OUT A WAY TO STORESEPARATE VALUES IN THE SET

set = {9,9.0}
print(set) # output = 9  9 and 9.0 consider to be samme 


# or 

set= {9,"9.0"}
print(set)

# or 

set = {
("float",9.0),
("int",9)
}
print(set)