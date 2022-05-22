

from cgi import test
from distutils.log import info
from doctest import testfile
import os, os.path
from pickletools import pybool

path1 = "/Users/monke/source/repos/Week 10 Thangs/"
file1 = "file1.txt"

firstdir = input('enter name of file you would like to create ')
if os.path.isdir(firstdir) == False:
   permission = 777
   os.mkdir(firstdir, permission)
   
   print("The directory has been CREATED")
   
else:
    print("The directory already exists, silly")

newfile = input('enter name of txt file ')


print("please input the following information")


name = input('name ')
address = input('address ')
phone = input('phone')

def output():
    return "{}, {}, {}".format(name, address, phone)

print(output())
print('The above will be saved to your file')


newfile = open('newfile.txt', mode ='w')
newfile.write(output())
newfile.close

newfile = open('newfile.txt', "r")
print("Pulled from file ", newfile.read())


print('Above is the proof from file')