# List : A built in data type store set of values
# it can store elemnets of different type (int,float,string,etc)
#for example 

'''
List = [99,85.5,85,2,"A","verybad"]

#slincing Similar to the slcing of strings

print(List[1])
print(List[1:2])


#negative slicing

print(List[-1])
print(List(-3,-1))'''



#it is mutable means we can change the element in thie list 
# for example

"""student = ["karan",95.5,66,"etcetc"]
print(student[0])                      # output is karan

student[0] = "Aryan"
print(student)                          #karan is replaced with Aryan
print(student[0])

list=["Tashu"]
student += list
print(student)
student[4]=student[0]
print(student)
print(len(student))


List = ["std_name","aryan","tashu","vicky","shristi","nishika"]
#now i wanted to swap the student of idx number 1 and 4
a =List[1]
List[1] = List[4]
List[4] = a
print(List) """  


#NOTE WE CAN ONLY ACCESS IN THE RANGE OF INDICES



#function of list or list method 

'''list =  [2,6,3]
list.append(4)  #add for at the last of list
print(list)
list.sort()     # sorts in ascending order
print(list)
list.sort(reverse=True) #sorts in descending order
print(list)
list.reverse()   #reverse the list
print(list)
list.insert(3,"A") #insert element at index 
print(list)
List=[1,1,2,3,54,"A","Aryan","Aryan"]
List.remove(1)   #removes first occurence of elements 
print(List)      #[1, 2, 3, 54, 'A', 'Aryan', 'Aryan']
List.remove("Aryan")
print(List)      #[1, 2, 3, 54, 'A', 'Aryan']'''


'''Data=[1,1,2,3,54,"A","Aryan","Aryan"]
#Data.pop() removes elements at idx
Data.pop(2)
print(Data)'''




#practice question 
# Wap to ask user to enter name of their favorite movies & store them in list
'''movies = []
mov1 = input("Enter  fist movie : ")
mov2 = input("enter second movie: ")
mov3 = input("enter third movie : ")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)'''
        # ORR
'''movies = []
movies.append(input("enter 1st movie :"))
movies.append(input("enter 2nd movie :"))
movies.append(input("enter 3rd movie :"))
print(movies)'''
  


#WAP TO CHEC IF A LIST A PALINDROME OF ELEMENTS  

'''list = [1,"abc",1,"bcc"]
print(len(list))
a = len(list) + 1
list1 = list[-1:-a:-1]
print(list1)
if(list==list1):
    print("list is palendrome")
else:
    print("List is not a palendrome")'''



    # Another way
list = [1,2,3]
list1 = [1,2,1]
copy_list = list.copy()
copy_list.reverse()
copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list == list):
    print("palendrome")
else:
    print("not a palendrome")
    if(copy_list1 == copy_list1):
        print("palendrome")
    else:
        print("not a palendrome")
