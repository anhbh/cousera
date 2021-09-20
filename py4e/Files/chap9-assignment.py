import os
import re

#path='D:\\OneDrive - DZS\\03-Courses\\04-Python\\Files'
#
#print(os.getcwd())
#os.chdir(path)
#print(os.getcwd())

filename='D:\\OneDrive - DZS\\03-Courses\\04-Python\\Files\\regex_sum_1349618.txt'
fh=open(filename)

total=0

for line in fh:
    nums=re.findall("[0-9]+",line)
    for num in nums:
        num=int(num)
        total = total+num
        
print("Total:",total)
