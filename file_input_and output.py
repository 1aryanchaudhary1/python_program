#PYTHON CAN BE USED TO PERFORM OPERATION ON A FILE (READ & WRITE THE DATA)
# TYPE OF FILE
# 1. text Files: .txt, .docx, .log etc              #Data in character 
# 2. Binary Files: .mp4, .mov, .png, .jpeg  etc     


# Open, read & close file

# f =open("file_name","mode")   # mode what we want to do in file r:read mode, w: write mode etc

f=open("dtatatatatatat.txt", "r")
data=f.read()
print(data)
print(type(data))
f.close

'''
character            meaning
"r"                  open for reading
"w"                  open for writing, truncating the file first
"x"                  create new file and open it for writing
"a"                  open for writing , appending to the end of the file if it exists
"b"                  binary mode
"t"                  text mode(default)
"+"                  open a disk file for updating
'''



