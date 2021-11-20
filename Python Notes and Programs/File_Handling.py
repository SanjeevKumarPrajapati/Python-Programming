"""
    File Handling in Python enables us to create , update ,read and delete the file stored on the file system through our python program.
    1.) Open a File
    2.) Process file (perform read or write operation)
    3.) Close the file

"""
#file_name=open(file_name,access mode)
#w=writing only
#r=read only
#r+=reading as well as writing
#a=append
#a+=append and read
#read()
"""
a=open("abc.txt","r")
print(a.read())
a.close()
"""
#readlines()
"""
a=open("abc.txt","r")
print(a.readlines(10))
a.close()
"""
#create your own file
"""
a=open("python.txt","w")
a.write("Hii i am python programmer")
a.write("\nI am from UK")
a.write("I am 24 year old")
a.close()
"""
#open your own file
"""
a=open("python.txt","r")
print(a.read())
a.close()
"""
#append some data in existing file
"""
a=open("python.txt","a")
a.write("\nNo Data")
a.close()
"""
a=open("python.txt","r")
print(a.read())
a.close()













