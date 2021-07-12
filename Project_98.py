import sys
import time

def swapFiles(a,b):
    openFile1 = open(a,'r')
    openFile2 = open(b,'r')

    data_a = openFile1.read()
    data_b = openFile2.read()

    openFile1 = open(a,'w')
    openFile2 = open(b,'w')

    openFile1.write(data_b)
    openFile2.write(data_a)

file1 = input('Please enter the path of the first file you would like to swap... ')
file2 = input('Please enter the path of the second file you would like to swap... ')

swapFiles(file1,file2)
print('The files have been swapped successfully.')