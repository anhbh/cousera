import os, re, math
import random

# try with n sample
# in each sample, get random x, y in range of 0:1
# calculate the size = x^2 + y^2
# if size <=1 => count, else continue
# area=r*r*pi 
# square=2r*2r
# area=square*pi/4 => pi=4*area/square

sample=100000000
count=0
for i in range(0,sample):
	x=random.uniform(0,1)
	y=random.uniform(0,1)
	size=x**2 + y**2
	if size <=1 : count=count+1

pi=4*(float)(count/sample)
print(pi)